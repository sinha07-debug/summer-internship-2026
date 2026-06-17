# Flight Price Prediction API

## Overview

This project is a Machine Learning based Flight Price Prediction API built using Flask and Random Forest Regressor.

The API accepts flight details such as airline, source city, destination city, total stops, duration, departure time, and arrival time, then predicts the estimated flight price.

---

## Features

* Flight fare prediction using Random Forest Regressor
* REST API built with Flask
* Handles categorical feature encoding using One-Hot Encoding
* Performs preprocessing identical to training pipeline
* Returns predictions in JSON format

---

## Dataset

The dataset contains flight information including:

* Airline
* Source
* Destination
* Total Stops
* Additional Information
* Journey Date
* Departure Time
* Arrival Time
* Duration
* Price (Target Variable)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Flask
* Joblib

---

## Project Structure

flight_price_predictor/

├── app.py

├── flight_rf_model.pkl

├── columns.pkl

├── requirements.txt

└── README.md

---

## API Endpoint

### Home Route

GET /

Returns:

Flight Price Prediction API Running

### Prediction Route

POST /predict

Sample Request:

```json
{
    "Airline": "IndiGo",
    "Source": "Delhi",
    "Destination": "Cochin",
    "Total_Stops": "1 stop",
    "Additional_Info": "No info",
    "Journey_Day": 15,
    "Journey_Month": 6,
    "Dep_Hour": 10,
    "Dep_Min": 30,
    "Arrival_Hour": 12,
    "Arrival_Min": 45,
    "Duration_Hours": 2,
    "Duration_Mins": 15
}
```

Sample Response:

```json
{
    "Predicted Price": 5423.71
}
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd flight_price_predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The API will start at:

http://127.0.0.1:5000

---

## Machine Learning Workflow

1. Data Cleaning and Preprocessing
2. Feature Engineering
3. One-Hot Encoding of Categorical Features
4. Random Forest Model Training
5. Model Serialization using Joblib
6. Deployment using Flask API

---
