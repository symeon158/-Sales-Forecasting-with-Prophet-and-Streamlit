# Sales Forecasting with Prophet and Streamlit

This project provides sales forecasting for various materials and plants using Facebook's Prophet model, enhanced with hyperparameter tuning using Optuna. The app is built using Streamlit.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Files and Code Explanation](#files-and-code-explanation)
    - [sales_forecasting](#sales_forecasting)
        - [app.py](#app-py)
        - [forecast.py](#forecast-py)
        - [objective.py](#objective-py)
    - [data](#data)
    - [notebooks](#notebooks)
    - [requirements](#requirements)
    - [readme](#readme)
    - [license](#license)
6. [License](#license)

## Features

- **Sales Data**: Uses historical sales data to predict future sales.
- **Hyperparameter Tuning**: Uses Optuna to optimize Prophet hyperparameters.
- **Streamlit Interface**: User-friendly interface for selecting plant-material combinations and viewing forecasts.

## Project Structure

- `sales_forecasting/` - [Core functionality](#sales_forecasting).
- `data/` - [Data files](#data).
- `notebooks/` - [Jupyter notebooks for data exploration](#notebooks).
- `requirements.txt` - [Project dependencies](#requirements).
- `README.md` - [Project documentation](#readme).
- `LICENSE` - [License file](#license).

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/sales-forecasting.git
    ```

2. **Install the requirements**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:

    ```bash
    streamlit run sales_forecasting/app.py
    ```

## Usage

1. **Train Model**: Click the "Train Model" button to train the Prophet model for selected plant-material combinations.
2. **View Results**: Use the dropdown menu to select a combination and view the forecast plot, error metrics, and hyperparameters.

## Files and Code Explanation

### sales_forecasting

This directory contains the core functionality of the project.

#### app.py

`app.py` is the main file for the Streamlit application. It initializes the app, handles user input, triggers model training, and displays the results. 

- **Functionality**:
    - The app initializes with an introduction and a button to train the model.
    - The `compute_forecasts` function is defined and cached to perform forecasting for each plant and material combination.
    - The function `forecast_prophet_optimized` is used for optimized forecasting.
    - The user can select from various plant-material combinations to view the corresponding forecast, error metrics, hyperparameters, and detailed table.

#### forecast.py

`forecast.py` contains functions for sales forecasting.

- **Functionality**:
    - The `forecast_prophet_optimized` function optimizes the hyperparameters of the Prophet model using Optuna and then fits and predicts future sales.
    - The function returns the forecast plot, RMSE, MAE, best parameters, and a detailed table with predictions.

#### objective.py

`objective.py` contains the Optuna objective function for hyperparameter tuning.

- **Functionality**:
    - The `objective` function defines the search space for hyperparameter tuning.
    - It builds and fits a Prophet model using the given hyperparameters and returns the mean absolute error as the optimization metric.

### data

This directory contains the data files for the project.

#### sales_data.csv

`sales_data.csv` is the historical sales data used for forecasting.

### notebooks

This directory contains Jupyter notebooks for data exploration.

#### data_exploration.ipynb

`data_exploration.ipynb` is a Jupyter notebook for exploring the sales data.

- **Functionality**:
    - The notebook imports the sales data and performs exploratory data analysis.
    - It provides insights into the data distribution, trends, and any potential anomalies.

### requirements

#### requirements.txt

`requirements.txt` contains the project dependencies.

- **Dependencies**:
    - The file includes necessary packages like Streamlit, Plotly, scikit-learn, pandas, fbprophet, and optuna.

### readme

#### README.md

`README.md` is this file containing the project documentation.

### license

#### LICENSE

`LICENSE` is the project license.

## License

This project is licensed under the MIT License.
