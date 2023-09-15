from flask import Flask, request, render_template
import pickle 
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
database = pd.read_csv('database.csv')

loaded = pickle.load(open("data_picture.pkl", "rb"))
loaded_model = pickle.load(open('./model/price_predict2.model', 'rb'))
loaded_scaler = pickle.load(open('./model/scaler2.pkl', 'rb'))
newest_model = pickle.load(open('./model/new_model.pkl', 'rb'))
newest_model_scaler = pickle.load(open('./model/scaler_poly.pkl', 'rb'))
user_clicked = False  # Initialize user_clicked at the global scope

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/website1')
def website1():
    global user_clicked  # Use the global user_clicked variable
    user_clicked = request.args.get('user_clicked', default=None)
    return render_template('website1.html', user_clicked=user_clicked)

@app.route('/website2')
def website2():
    global user_clicked  # Use the global user_clicked variable
    user_clicked = request.args.get('user_clicked', default=None)
    return render_template('website2.html', user_clicked=user_clicked)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    engine = request.form.get('engine')
    power = request.form.get('maxpower')
    year = request.form.get('year')
    global user_clicked  

    if not engine:
        engine = 1248  # From median
    if not power:
        power = 83.14  # From median
    if not year:
        year = 2016  # From median

    input_values = np.array([[float(engine), float(power), int(year)]])

    if user_clicked == "website1" :
        scaled = loaded_scaler.transform(input_values)
        predicted_price = loaded_model.predict(scaled)


    elif user_clicked == "website2" :
        # scaled = newest_model_scaler.transform(input_values)
        scale = PolynomialFeatures(degree = 2, include_bias=False).fit_transform(input_values)
        scaled = newest_model_scaler.transform(scale)
        intercept = np.ones((scaled.shape[0], 1))
        scaled   = np.concatenate((intercept, scaled), axis=1)
        predicted_price = newest_model.predict(scaled)

    target_values = np.array([float(engine), float(power), year, np.exp(predicted_price)[0]], dtype=np.float64)
    database['distance'] = np.sqrt(np.sum(((database[['engine', 'max_power', 'year', 'selling_price']].values - target_values) ** 2) * np.array([1, 1, 1, 0.01]), axis=1))
    most_similar_row = database[database['distance'] == database['distance'].min()]

    try :    
        query = most_similar_row['name'].iloc[0]
    except :
        query = database['name'][0]
    
    binary_image_data = loaded[query]

    with open('static/suggest.jpg', 'wb') as f:
        f.write(binary_image_data)

    df_unique = most_similar_row.drop_duplicates(subset=['name'])
    return render_template('response.html', user_clicked=user_clicked,
                       textbox1_data=np.exp(predicted_price),
                       car_name=df_unique['name'].item(),
                       max_power=df_unique['max_power'].item(),
                       engine=df_unique['engine'].item(),
                       car_year=df_unique['year'].item(),
                       car_price=df_unique['selling_price'].item())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
