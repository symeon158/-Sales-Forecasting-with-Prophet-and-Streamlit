import streamlit as st
import plotly.graph_objs as go
from sklearn.metrics import mean_absolute_error, mean_squared_error
from fbprophet import Prophet
from math import sqrt
import pandas as pd
from fbprophet.plot import plot_plotly
import optuna

# Load the Data
data = data = pd.read_csv('c:\\Users\\...\\...\\sales_data.csv')
data['Document Date'] = pd.to_datetime(data['Document Date'])

# Filter dataframe based on the given materials
selected_materials = [101, 102] #, 103, 104, 105
data = data[data['Material'].isin(selected_materials)]

# Drop any rows with NaN values
data = data.dropna()

# Aggregate data by day, plant, and material, summing up the quantity
grouped_data = data.groupby(['Document Date', 'Plant', 'Material']).agg({'Quantity':'sum'}).reset_index()
grouped_data.columns = ['ds', 'Plant', 'Material', 'y']

def objective(trial, data_subset):
    # Hyperparameter suggestions
    seasonality_mode = trial.suggest_categorical("seasonality_mode", ["additive", "multiplicative"])
    changepoint_prior_scale = trial.suggest_float("changepoint_prior_scale", 0.001, 0.01, 0.1, 0.5, log=True)
    seasonality_prior_scale = trial.suggest_float("seasonality_prior_scale", 0.01, 0.1, 1.0, 10, log=True)
    fourier_order_monthly = trial.suggest_int("fourier_order_monthly", 1, 3, 5, 7, 10)
    yearly_seasonality = trial.suggest_categorical("yearly_seasonality", [True, False])
    weekly_seasonality = trial.suggest_categorical("weekly_seasonality", [True, False])
    daily_seasonality = trial.suggest_categorical("daily_seasonality", [True, False])
    n_changepoints = trial.suggest_int("n_changepoints", 10, 40)
    changepoint_range = trial.suggest_float("changepoint_range", 0.8, 1.0)

    m = Prophet(
        seasonality_mode=seasonality_mode,
        changepoint_prior_scale=changepoint_prior_scale,
        seasonality_prior_scale=seasonality_prior_scale,
        yearly_seasonality=yearly_seasonality,
        weekly_seasonality=weekly_seasonality,
        daily_seasonality=daily_seasonality,
        n_changepoints=n_changepoints,
        changepoint_range=changepoint_range
    )

    m.add_seasonality(name='monthly', period=30.5, fourier_order=fourier_order_monthly)

    m.fit(data_subset)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    
    return mean_absolute_error(data_subset['y'], forecast['yhat'][:len(data_subset)])

def forecast_prophet_optimized(subset):
    study = optuna.create_study(direction="minimize")
    study.optimize(lambda trial: objective(trial, subset), n_trials=30)
    
    plant = subset['Plant'].iloc[0]
    material = subset['Material'].iloc[0]

    best_params = study.best_params

    # Ensure all the parameters you want to use are extracted from best_params
    prophet_params = {
        "seasonality_mode": best_params["seasonality_mode"],
        "changepoint_prior_scale": best_params["changepoint_prior_scale"],
        "seasonality_prior_scale": best_params["seasonality_prior_scale"],
        "yearly_seasonality": best_params["yearly_seasonality"],
        "weekly_seasonality": best_params["weekly_seasonality"],
        "daily_seasonality": best_params["daily_seasonality"],
        "n_changepoints": best_params["n_changepoints"],
        "changepoint_range": best_params["changepoint_range"]
    }

    prophet = Prophet(**prophet_params)
    
    fourier_order = best_params.get("fourier_order_monthly", 5)
    prophet.add_seasonality(name='monthly', period=30.5, fourier_order=fourier_order)

    prophet.fit(subset)
    
    future = prophet.make_future_dataframe(periods=30)

    forecast = prophet.predict(future)

    if plant == 101:
        forecast.loc[forecast['ds'].dt.weekday >= 5, 'yhat'] = 0
    else:
        forecast.loc[forecast['ds'].dt.weekday == 6, 'yhat'] = 0

    forecast.loc[forecast['yhat'] < 0, 'yhat'] = 0
    
    rmse = sqrt(mean_squared_error(subset['y'].iloc[-30:], forecast['yhat'].iloc[-len(subset):].iloc[:30]))
    mae = mean_absolute_error(subset['y'].iloc[-30:], forecast['yhat'].iloc[-len(subset):].iloc[:30])
    fig = plot_plotly(prophet, forecast)
    
    # Creating the table
    table_df = subset.copy()
    table_df['Predicted Quantity'] = forecast['yhat'].iloc[:len(subset)]
    table_df['Difference'] = table_df['y'] - table_df['Predicted Quantity']
    table_df['Percentage Difference'] = (table_df['Difference'] / table_df['y']) * 100
    table_df = table_df[['ds', 'Plant', 'Material', 'y', 'Predicted Quantity', 'Difference', 'Percentage Difference']]
    
    return fig, rmse, mae, best_params, table_df


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def compute_forecasts(data):
    results = {}
    for (plant, material), group in data.groupby(['Plant', 'Material']):
        key = f"{plant}_{material}"
        fig, rmse, mae, best_params, table_df = forecast_prophet_optimized(group)
        results[key] = {'Plot': fig, 'RMSE': rmse, 'MAE': mae, 'Best Parameters': best_params, 'Table': table_df}
    return results

# Initialize session state
if "trained" not in st.session_state:
    st.session_state.trained = False
if "results" not in st.session_state:
    st.session_state.results = {}

# Streamlit app layout and interactivity
st.title('Sales Forecasting')

# Button to trigger training
if st.button('Train Model'):
    st.session_state.results = compute_forecasts(grouped_data)
    st.session_state.trained = True

if st.session_state.trained:
    # Select plant and material
    all_keys = list(st.session_state.results.keys())
    selected_key = st.selectbox("Choose a Plant_Material combination:", all_keys)

    # Display results
    st.write(f"Selected combination: {selected_key}")
    st.plotly_chart(st.session_state.results[selected_key]['Plot'])
    st.write(f"RMSE: {st.session_state.results[selected_key]['RMSE']:.2f}")
    st.write(f"MAE: {st.session_state.results[selected_key]['MAE']:.2f}")
    st.write("Best Hyperparameters:", st.session_state.results[selected_key]['Best Parameters'])
    st.write("Best Hyperparameters:",st.session_state. results[selected_key]['Best Parameters'])
    st.table(st.session_state.results[selected_key]['Table'])
else:
    st.write("Please train the model first.")

if __name__ == '__main__':
    st.write("Run streamlit to view the dashboard!")
