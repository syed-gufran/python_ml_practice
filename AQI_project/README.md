# AQI Prediction Web App

This is a web application designed to predict the Air Quality Index (AQI) using a machine learning model. Users input relevant air quality parameters, and the application returns a predicted AQI value or category.

## Features

- User-friendly web interface
- Predicts AQI based on various pollutant levels
- Uses a pre-trained ML model (`aqi_model.sav`)

## Tech Stack

- Python
- Streamlit (web framework)
- scikit-learn (for model handling)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/aqi-prediction-webapp.git
cd aqi-prediction-webapp
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run (path of) web_app.py
```

### 4. Open in your browser

Navigate to:

```
http://127.0.0.1:5000/
```

## Files

- `web_app.py`: Main Flask app that handles routing and predictions
- `aqi_model.sav`: Trained machine learning model
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation
- 'city_day.csv' : contains the historical data
- 'air quality index(AQI) predictiom.ipynb' : contains data analysis and model building step

## Notes

- Ensure Python 3.7+ is installed.
- Do not modify the model file unless retraining is intended.
