import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib

# Load Dataset
data = pd.read_csv("StudentsPerformance.csv")
print("Dataset Loaded Successfully")

# Separate categorical and numerical columns
cat_columns = data.select_dtypes(include="object").columns
num_columns = data.select_dtypes(include="number").columns

# Apply Label Encoding to all categorical columns
label_encoders = {}
for col in cat_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le  # Save encoders for future use

# Apply MinMaxScaler to numerical columns
scaler = MinMaxScaler()
data[num_columns] = scaler.fit_transform(data[num_columns])

# Feature-Target Split
X = data[['math score', 'reading score', 'writing score']]
y = data['race/ethnicity']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save Model and Preprocessors
model_dir = 'model'
os.makedirs(model_dir, exist_ok=True)

joblib.dump(model, os.path.join(model_dir, 'decision_tree_model.pkl'))
print("Model saved successfully.")

joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))
print("Scaler saved successfully.")

joblib.dump(label_encoders, os.path.join(model_dir, 'label_encoders.pkl'))
print("Label encoders saved successfully.")
