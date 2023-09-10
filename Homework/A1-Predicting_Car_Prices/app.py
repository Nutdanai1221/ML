from flask import Flask, request, render_template
import pickle 
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
database = pd.read_csv('database.csv')


with open('./model/scaler2.pkl', 'rb') as file:
    loaded_scaler = pickle.load(file)

with open('./model/price_predict2.model', 'rb') as file:
    loaded_model = pickle.load(file)


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/receive_data', methods=['POST'])
def receive_data():
    engine = request.form.get('engine')
    power = request.form.get('maxpower')
    year = request.form.get('year')
    if not engine :
        engine = 1248 #from median
    if not power :
        power = 83.14 #from median
    if not year :
        year = 2016 #from median
    

    input_values = np.array([[float(engine), float(power), int(year)]])
    scaled = loaded_scaler.transform(input_values)
    predicted_price = loaded_model.predict(scaled)
    # target_values = np.array([float(engine), float(power), year, np.exp(predicted_price)], dtype=np.float64)\
    target_values = np.array([float(engine), float(power), year, np.exp(predicted_price)[0]], dtype=np.float64)
    # print(target_values)
    

    #database['distance'] = np.sqrt(np.sum((database[['engine', 'max_power', 'year', 'selling_price']].values - target_values) ** 2, axis=1))
    database['distance'] = np.sqrt(np.sum(((database[['engine', 'max_power', 'year', 'selling_price']].values - target_values) ** 2) * np.array([1, 1, 1, 0.01]), axis=1))
    
    most_similar_row = database[database['distance'] == database['distance'].min()]

    print(most_similar_row)
    try :
        
        query = most_similar_row['name'].iloc[0]
    except :
        query = database['name'][0]
    
    df_unique = most_similar_row.drop_duplicates(subset=['name'])

    search_query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={search_query}&tbm=isch"  # the URL of the search result page
    response = requests.get(url)  # make a GET request to the URL
    soup = BeautifulSoup(response.text, "html.parser")  # parse the HTML content with BeautifulSoup
    # find the first image link by searching for the appropriate tag and attribute
    img_tags = soup.find_all("img")
    img_links = [img["src"] for img in img_tags if img.has_attr("src")][1]


    return render_template('response.html', 
                       textbox1_data=np.exp(predicted_price),
                       car_name=df_unique['name'].item(),
                       max_power=df_unique['max_power'].item(),
                       engine=df_unique['engine'].item(),
                       car_year=df_unique['year'].item(),
                       car_price=df_unique['selling_price'].item(),
                       img = img_links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=600)