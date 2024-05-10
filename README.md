# Automated Sales Forecasting for Supply Chain Management with FBProphet, Python, and Streamlit
Over the past weeks, I've been diving deep into the intriguing realm of time-series forecasting. By combining the robustness of FBProphet and the interactivity of Streamlit, I've developed a dashboard that:

✅ Allows users to forecast sales for selected products and plants.  
✅ Visualizes the comparison between actual sales and forecasted figures.  
✅ Offers decomposition plots that unravel underlying trends and seasonality.  
✅ Utilizes Optuna's prowess for hyperparameter optimization.  
✅ Computes critical performance metrics like RMSE, MAE, and MAPE to evaluate forecasts.  
✅ Ensures results are stored seamlessly for subsequent analysis and insights.

## Table of Contents
- [Project Overview](#project-overview)
- [Key Components and Functionalities](#key-components-and-functionalities)
  - [User Interface](#user-interface)
  - [Data Handling and Preprocessing](#data-handling-and-preprocessing)
  - [Forecasting Model](#forecasting-model)
  - [Hyperparameter Optimization](#hyperparameter-optimization)
  - [Model Evaluation and Results](#model-evaluation-and-results)
  - [Streamlit App Integration](#streamlit-app-integration)
- [Technologies and Libraries Used](#technologies-and-libraries-used)
- [Benefits and Use Cases](#benefits-and-use-cases)
- [Potential Enhancements](#potential-enhancements)
- [Conclusion](#conclusion)
- [Advantages for Supply Chain Management](#advantages-for-Supply-Chain-Management)

## Project Overview
The Sales Forecasting Dashboard is an interactive web application developed using Streamlit. It is designed to forecast sales quantities using time series data, with the help of Facebook Prophet and Optuna for hyperparameter optimization. This dashboard provides users with visualizations of forecasted sales and key metrics, facilitating data-driven decision-making.

## Key Components and Functionalities
- **Hyperparameter Tuning**: Optuna optimizes Prophet's hyperparameters for improved forecasting accuracy.
- **User Interface**: Streamlit provides an intuitive interface for selecting plant-material combinations and viewing forecasts.
- **Forecasting**: Prophet forecasts future sales based on historical data.
- **Visualization**: The application displays interactive plots and metrics to evaluate the forecasts.
- **Tables**: Provides detailed tables comparing actual sales with forecasted sales.
- **Country-Specific Holidays**: Incorporates country-specific holidays and weekends for more accurate predictions.
- **Cross-Validation**: Provides cross-validation results for understanding the model's capabilities.

### User Interface
- **Streamlit Layout**: The app features a clean and interactive layout with buttons and dropdowns for user interaction.
- **File Upload**: (Assumed as part of initial setup) Users upload a CSV file containing sales data.
- **Model Training Button**: Users can initiate the model training process through a simple button click.
- **Selection Dropdown**: Allows users to select different plant and material combinations to view specific forecast results.

### Data Handling and Preprocessing
- **Data Loading**: Reads sales data from a CSV file and converts the 'Document Date' column to datetime format.
- **Data Filtering**: Filters data based on selected materials to focus the analysis.
- **Aggregation**: Aggregates sales quantity by day, plant, and material, preparing the data for time series forecasting.

### Forecasting Model
- **Facebook Prophet**: Utilizes Prophet for time series forecasting, which is well-suited for handling daily data with seasonality and holidays.
- **Seasonality and Trends**: Adds monthly seasonality to the model to capture periodic patterns.

### Hyperparameter Optimization
- **Optuna Integration**: Uses Optuna to optimize Prophet's hyperparameters, aiming to minimize the mean absolute error (MAE).
- **Parameter Suggestions**: Includes suggestions for seasonality mode, changepoint scales, Fourier orders, and seasonality types.
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

### Model Evaluation and Results
- **Evaluation Metrics**: Computes Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) to evaluate model performance.
- **Plotly Visualizations**: Generates interactive plots of the forecasted sales using Plotly.
- **Result Tables**: Provides a detailed table showing actual vs. predicted quantities, differences, and percentage differences.

### Streamlit App Integration
- **Session State Management**: Maintains model training state and results across user interactions.
- **Dynamic Content Display**: Updates plots and metrics based on user-selected plant and material combinations.

## Technologies and Libraries Used
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and preprocessing.
- **Plotly Graph Objects**: For creating interactive and visually appealing plots.
- **Facebook Prophet**: For robust time series forecasting.
- **Optuna**: For efficient hyperparameter optimization.
- **Scikit-learn**: For computing evaluation metrics.

## Benefits and Use Cases
- **User-Friendly Interface**: The dashboard is designed for ease of use, enabling non-technical users to perform sophisticated sales forecasting.
- **Accurate Forecasting**: Leveraging Prophet and Optuna ensures accurate and reliable forecasts, accommodating seasonal trends and changes.
- **Comprehensive Analysis**: Provides detailed insights into forecast performance through interactive plots and comprehensive tables.

## Potential Enhancements
- **Automated Data Upload**: Incorporate file upload functionality directly into the app.
- **Expanded Forecasting Options**: Add support for more complex seasonality and holidays.
- **Real-Time Data Integration**: Enable real-time data updates for continuous forecasting.
- **Enhanced Visualization**: Introduce additional chart types and customization options.

## Conclusion
The Sales Forecasting Dashboard is a powerful tool for businesses to forecast sales quantities effectively. By integrating advanced time series forecasting techniques with a user-friendly interface, it enables users to make informed decisions based on accurate predictions and comprehensive analysis.


## Advantages for Supply Chain Management

1. **Enhanced Demand Planning**: Precise forecasts facilitate better production and inventory planning.
2. **Optimized Inventory Levels**: Reduce stockouts and overstock scenarios, leading to substantial cost savings.
3. **Strategic Decision Making**: Leveraging insights for promotional strategies and capacity planning.
4. **Reduced Lead Time**: Efficiently manage and schedule shipments.
5. **Risk Mitigation**: Prepare for demand surges and market uncertainties.

For all my supply chain professionals out there, this tool might be the game-changer you've been waiting for! Let's chat if you're keen on exploring how this can transform your SCM strategy.


