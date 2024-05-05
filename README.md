# Sales Forecasting with Prophet and Streamlit

This project provides sales forecasting for various materials and plants using Facebook's Prophet model, enhanced with hyperparameter tuning using Optuna. The app is built using Streamlit.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Files](#files)
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

## Files

### sales_forecasting

This directory contains the core functionality of the project.

- **[`app.py`](sales_forecasting/app.py)**: The main Streamlit app.
- **[`forecast.py`](sales_forecasting/forecast.py)**: Contains functions for sales forecasting.
- **[`objective.py`](sales_forecasting/objective.py)**: Contains the Optuna objective function for hyperparameter tuning.

### data

This directory contains the data files for the project.

- **[`sales_data.csv`](data/sales_data.csv)**: The historical sales data.

### notebooks

This directory contains Jupyter notebooks for data exploration.

- **[`data_exploration.ipynb`](notebooks/data_exploration.ipynb)**: Notebook for exploring the sales data.

### requirements

- **[`requirements.txt`](requirements.txt)**: The project dependencies.

### readme

- **[`README.md`](README.md)**: This file containing the project documentation.

### license

- **[`LICENSE`](LICENSE)**: The project license.

## License

This project is licensed under the MIT License.
