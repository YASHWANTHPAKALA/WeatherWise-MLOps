<<<<<<< HEAD
# WeatherWise — Weather Condition Classification

A small ML/MLOps prototype that predicts Sunny, Cloudy, Rainy, or Foggy from temperature, humidity, wind speed, and pressure using a Decision Tree classifier.

## Features
- Train/test split and evaluation report
- Saved scikit-learn model
- Flask web interface and `/health` endpoint
- Dockerfile for containerized execution

## Dataset caveat
This starter uses a tiny illustrative dataset embedded in `train.py`. It is for demonstrating the workflow only, not for trustworthy weather prediction. Replace it with a larger, documented, real dataset before making real-world claims.

## Run locallycode 
```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python train.py
python app.py
```
Open http://127.0.0.1:5000. Health endpoint: http://127.0.0.1:5000/health

## Docker
```bash
docker build -t weatherwise .
docker run --rm -p 5000:5000 weatherwise
```

## Deployment URLs
AWS: Add the actual working deployment URL here.
GCP: Add the actual working deployment URL here.

Do not represent placeholders as deployed URLs.
=======
# WeatherWise-MLOps
Weather condition classification using Machine Learning, Flask, Docker, and AWS EC2.
>>>>>>> f9d3f9e9ab2c89e2f95bacb69fe4e7ddfc7f9bcf
