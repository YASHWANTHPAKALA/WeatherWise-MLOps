# WeatherWise — Weather Condition Classification

A Machine Learning and MLOps project that classifies weather conditions as Sunny, Cloudy, Rainy, or Foggy using temperature, humidity, wind speed, and pressure with a Decision Tree classifier.

## Features
- Machine learning model training and evaluation
- Flask web interface for weather classification
- Health-check and prediction API endpoints
- Docker containerization
- AWS EC2 deployment

## Technologies
- Python
- Scikit-learn
- Flask
- Docker
- AWS EC2

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Docker

Build the image:

```bash
docker build -t weatherwise:1.0 .
```

Run the container:

```bash
docker run -d --name weatherwise-app -p 5000:5000 weatherwise:1.0
```

## Health Check

Open `http://127.0.0.1:5000/health`.

## AWS Deployment

Application: http://13.236.9.132:5000

Health check: http://13.236.9.132:5000/health

**Note:** The AWS links work only while the EC2 instance is running and the required security-group rules permit access.
