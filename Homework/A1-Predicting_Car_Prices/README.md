# Car Price Prediction Web Application

This repository contains the implementation of a simple web-based car price prediction system for the Chaky company. The goal of this project is to develop a machine learning model that can predict car prices based on various features, analyze the data and deploy it as a web application for public use. This README provides an overview of the project structure, tasks performed, and instructions for setting up and running the application locally.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


## Getting Started

Follow these steps to set up and deploy the project on your local machine:

1. Clone this repository to your local machine by executing the following command in your terminal:

    ```bash
    git clone https://github.com/Nutdanai1221/ML.git
    ```

2. Navigate to the project directory using the command:

    ```bash
    cd ML/Homework/A1-Predicting_Car_Prices
    ```

3. Deploy the website within a Docker container using `docker-compose`. Execute the following command to build and start the necessary containers, based on the configurations specified in the `docker-compose.yml` file:

    ```bash
    docker-compose up
    ```

4. Once the containers are up and running, access the website by opening your web browser and navigating to:

    [http://localhost:600](http://localhost:600)

    This will direct you to the locally hosted instance of the website.

Feel free to reach out if you encounter any issues or need further assistance.

   
## Project Structure

The project is organized as follows:

- **app/**: Holds the files for the web application, including `app.py`, `templates/` and `static/`.
- **requirements.txt**: Lists the required Python packages and their versions for reproducibility.
- **README.md**: The documentation you're currently reading, which provides an overview of the project.
- i feel sleepy now maybe tomorrow

## Preview

1. **Homepage Entry:**
   To start using the web app, open your web browser and enter the following URL in the address bar: `http://127.0.0.1:600`.
   
   ![Homepage Entry](images/homepage.png)

2. **Input Feature Information:**
   On the web page, you'll see a form where you need to provide information about the car you're interested in. You'll be asked to enter the following details:
   - Engine size (CC)
   - Maximum power (bhp)
   - Year of manufacture

   Fill in these fields with the corresponding values for the car you want to predict the price for.
   
   ![Input Features](images/input_features.png)

3. **View Prediction and Suggestions:**
   After you've entered the required information, click the "Predict" button. The web app will process the data and provide you with the following results:
   - Predicted price of the car
   - Suggestions for cars with features similar to the predicted price
   
   You can use this information to get an idea of how much the car might cost and explore other cars with similar features.
   
   ![View Prediction](images/view_prediction.png)
