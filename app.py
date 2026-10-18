
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)

# Load the trained model
MODEL_PATH = Path(__file__).resolve().parent / "weather_model.joblib"
model = joblib.load(MODEL_PATH)


def predict_weather(data):
    """Validate inputs and predict the weather condition."""
    row = pd.DataFrame([{
        "temperature": float(data["temperature"]),
        "humidity": float(data["humidity"]),
        "wind_speed": float(data["wind_speed"]),
        "pressure": float(data["pressure"])
    }])

    return str(model.predict(row)[0])


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            prediction = predict_weather(request.form)
        except (ValueError, TypeError, KeyError):
            error = "Enter valid numeric values for every field."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None
    })


@app.route("/prediction", methods=["POST"])
def prediction_api():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required."}), 400

    try:
        prediction = predict_weather(data)
        return jsonify({"predicted_condition": prediction})

    except (ValueError, TypeError, KeyError):
        return jsonify({
            "error": (
                "Provide numeric values for temperature, humidity, "
                "wind_speed, and pressure."
            )
        }), 400


if __name__ == "__main__":
    # Required for access through Docker port mapping
    app.run(host="0.0.0.0", port=5000, debug=False)
