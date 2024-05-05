# Sales Forecasting with Prophet and Streamlit

This project is a sales forecasting application using Facebook's Prophet model, enhanced with hyperparameter tuning using Optuna, and built with a user-friendly interface in Streamlit.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Files and Code Explanation](#files-and-code-explanation)
    - [sales_forecasting](#sales_forecasting)
        - [app.py](#app-py)
        - [forecast.py](#forecast-py)
        - [objective.py](#objective-py)
    - [data](#data)
    - [notebooks](#notebooks)
    - [requirements](#requirements)
    - [readme](#readme)
    - [license](#license)
7. [License](#license)

## Overview

This project uses historical sales data to predict future sales for various materials and plants. It leverages the powerful Prophet forecasting tool from Facebook to model the data, using Optuna to optimize hyperparameters for the best possible model performance. The application is built using Streamlit, providing a clean and interactive user interface.

## Features

- **Hyperparameter Tuning**: Optuna optimizes Prophet's hyperparameters for improved forecasting accuracy.
- **User Interface**: Streamlit provides an intuitive interface for selecting plant-material combinations and viewing forecasts.
- **Forecasting**: Prophet forecasts future sales based on historical data.
- **Visualization**: The application displays interactive plots and metrics to evaluate the forecasts.
- **Tables**: Provides detailed tables comparing actual sales with forecasted sales.

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

`app.py` is the main Streamlit application that controls the user interface and functionality.

- **Train Model**:
    - The user clicks the "Train Model" button to initiate the forecasting process.
    - The `compute_forecasts` function generates forecasts for each plant-material combination.
    - The results, including plots, metrics, and tables, are stored in `st.session_state`.
  
- **Dropdown Menu**:
    - The user selects a plant-material combination from the dropdown menu to view specific results.

- **Visualization**:
    - The function `plotly_chart` displays interactive plots using Plotly.
  
- **Metrics**:
    - The application displays RMSE and MAE metrics for the forecasts.

- **Table**:
    - The application displays a table with the forecasted values, actual values, and differences.

#### forecast.py

`forecast.py` contains functions for sales forecasting using Prophet with hyperparameter tuning via Optuna.

- **forecast_prophet_optimized**:
    - This function performs optimized forecasting using Optuna.
    - It returns the forecast plot, RMSE, MAE, best hyperparameters, and a detailed table.

#### objective.py

`objective.py` contains the Optuna objective function for hyperparameter tuning.

- **Objective Function**:
    - The function defines the hyperparameters to be optimized:
        - `seasonality_mode`: Controls how seasonal effects are modeled (additive or multiplicative).
        - `changepoint_prior_scale`: Determines flexibility in detecting changes.
        - `seasonality_prior_scale`: Influences the strength of seasonal components.
        - `fourier_order_monthly`: Sets the number of terms in the Fourier series for monthly seasonality.
        - `yearly_seasonality`: Enables or disables yearly seasonality.
        - `weekly_seasonality`: Enables or disables weekly seasonality.
        - `daily_seasonality`: Enables or disables daily seasonality.
        - `n_changepoints`: Number of potential changepoints.
        - `changepoint_range`: Proportion of the history in which to look for changepoints.

    - The function fits a Prophet model and returns the mean absolute error as the optimization metric.

### data

This directory contains the data files for the project.

#### sales_data.csv

`sales_data.csv` is the historical sales data used for forecasting.

### notebooks

This directory contains Jupyter notebooks for data exploration.

#### data_exploration.ipynb

`data_exploration.ipynb` is a Jupyter notebook for exploring the sales data.

### requirements

#### requirements.txt

`requirements.txt` contains the project dependencies.

### readme

#### README.md

`README.md` is this file containing the project documentation.

### license

#### LICENSE

`LICENSE` is the project license.

## License

This project is licensed under the MIT License.
