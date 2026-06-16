from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("flight_rf_model.pkl")
columns = joblib.load("columns.pkl")


@app.route("/")
def home():
    return "Flight Price Prediction API Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([data])

    df["Total_Stops"] = df["Total_Stops"].map({
        "non-stop": 0,
        "1 stop": 1,
        "2 stops": 2,
        "3 stops": 3,
        "4 stops": 4
    })

    df = pd.get_dummies(
        df,
        columns=[
            "Airline",
            "Source",
            "Destination",
            "Additional_Info"
        ]
    )

    df = df.reindex(
        columns=columns,
        fill_value=0
    )

    prediction = model.predict(df)

    return jsonify(
        {
            "Predicted Price": round(float(prediction[0]), 2)
        }
    )


if __name__ == "__main__":
    app.run(debug=True)