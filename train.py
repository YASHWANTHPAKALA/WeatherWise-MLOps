import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Small illustrative classroom dataset; replace with real data for meaningful results.
rows = [
(30,35,8,1015,"Sunny"),(32,30,10,1014,"Sunny"),(28,40,7,1016,"Sunny"),
(34,32,12,1013,"Sunny"),(29,38,9,1015,"Sunny"),(31,33,11,1014,"Sunny"),
(24,55,12,1012,"Cloudy"),(22,60,14,1011,"Cloudy"),(26,58,10,1013,"Cloudy"),
(23,62,13,1010,"Cloudy"),(25,53,9,1012,"Cloudy"),(21,65,15,1011,"Cloudy"),
(22,88,20,1002,"Rainy"),(24,92,25,1000,"Rainy"),(20,90,18,1004,"Rainy"),
(26,85,22,1003,"Rainy"),(23,95,16,1001,"Rainy"),(21,87,24,1002,"Rainy"),
(16,80,5,1010,"Foggy"),(14,85,4,1011,"Foggy"),(18,78,6,1009,"Foggy"),
(15,82,3,1012,"Foggy"),(17,88,5,1010,"Foggy"),(13,84,4,1011,"Foggy"),
(33,42,8,1016,"Sunny"),(27,57,11,1013,"Cloudy"),(25,89,21,1001,"Rainy"),
(16,83,4,1010,"Foggy"),(31,36,9,1015,"Sunny"),(22,59,12,1012,"Cloudy"),
(24,91,23,1002,"Rainy"),(15,81,5,1011,"Foggy")
]
cols = ["temperature", "humidity", "wind_speed", "pressure", "condition"]
df = pd.DataFrame(rows, columns=cols)
X, y = df[cols[:-1]], df["condition"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(f"Test accuracy: {accuracy_score(y_test, pred):.2%}")
print(classification_report(y_test, pred, zero_division=0))
joblib.dump(model, "weather_model.joblib")
print("Saved weather_model.joblib")
