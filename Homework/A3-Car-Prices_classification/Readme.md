
# Car Price Prediction Web Application - A2

This repository contains the continuation and improvements of the A1 project focused on predicting car prices for the Chaky company. In this iteration, we've enhanced the prediction model, performed detailed data analysis, and integrated new features for a more interactive user experience on the web application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Experiments](#experiments)
- [Preview](#preview)

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Getting Started
For the docker compose file you can use [docker-compose](https://github.com/Nutdanai1221/ML/blob/main/Homework/A1-Predicting_Car_Prices/docker-compose.yml) from last assignment to deploy website on your local host.
Follow these steps to set up and deploy the project on your local machine:

1. Clone this repository to your local machine by executing the following command in your terminal:

    ```bash
    git clone https://github.com/Nutdanai1221/ML.git
    ```

2. Navigate to the project directory for A2 using the command:

    ```bash
    cd ML/Homework/A2-Predicting_Car_Prices_From_Scratch
    ```

3. Deploy the website within a Docker container using `docker-compose`. Execute the following command to build and start the necessary containers, based on the configurations specified in the `docker-compose.yml` file:

    ```bash
    docker-compose up
    ```

4. Once the containers are up and running, access the website by opening your web browser and navigating to:

    [http://localhost:600](http://localhost:600)

Feel free to reach out if you encounter any issues or need further assistance.

## Project Structure

The project for A2 is organized similarly to A1 but contains enhanced scripts and additional analyses:

- **app/**: Holds the files for the updated web application, including `app.py`, `templates/`, and `static/`.
- **experiment/**: Contains the enhanced `Assignment.ipynb` file with detailed data analysis and more experiment.
- **model/**: Contains the updated machine learning model and the Scaler object.
- **Dockerfile**: Provides instructions for building a Docker container for the application.
- **requirements.txt**: Lists the required Python packages and their versions for reproducibility.
- **README.md**: The documentation you're currently reading, which provides an overview of the project.

## Experiments

In this section, we performed various experiments to optimize our model's performance. We experimented with different algorithms, feature selection methods, and hyperparameter tuning techniques. The detailed analysis and results of these experiments can be found in the `Assignment.ipynb` file.

## Preview

1. **Homepage Entry:**
   Upon opening the website at [https://st123055-a2.ml2023.cs.ait.ac.th/](https://st123055-a2.ml2023.cs.ait.ac.th/), you will be greeted with a homepage that provides insights into the fundamentals of linear regression. You can also navigate through the website using the navigation bar.
   ![Homepage Entry](https://github.com/Nutdanai1221/ML/blob/main/Homework/A2-Predicting_Car_Prices_From_Scratch/figure/homepage.png)
2. **Navigation Bar:**
   The navigation bar on the top of the website provides two main options:
   * A link to the original (A1) car price prediction page.
   * A link to the new car price prediction model page(A2).
You can easily switch between these pages using the navigation bar.   

3. **Input Feature Information:**
   On the webpage, provide information about the car you're interested in, including:
   - Engine size (CC)
   - Maximum power (bhp)
   - Year of manufacture
   
   ![Input Features](https://github.com/Nutdanai1221/ML/blob/main/Homework/A2-Predicting_Car_Prices_From_Scratch/figure/new_model_page.png)

   In the new website, a description is provided below the main topic.

5. **View Prediction and Suggestions:**
   After providing the car details, click the "Predict Price" button. The web app will then showcase:
   - The predicted car price
   - Suggestions for cars with similar features to the given price range
   
   ![View Prediction](https://github.com/Nutdanai1221/ML/blob/main/Homework/A2-Predicting_Car_Prices_From_Scratch/figure/result.png)
