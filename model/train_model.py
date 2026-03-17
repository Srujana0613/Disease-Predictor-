import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np

# ── Diabetes Model ──────────────────────────
diabetes_df = pd.read_csv('model/diabetes.csv')

# Fix zero values (replace with median)
cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for col in cols:
    diabetes_df[col] = diabetes_df[col].replace(0, diabetes_df[col].median())

X_d = diabetes_df.drop('Outcome', axis=1)
y_d = diabetes_df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X_d, y_d, test_size=0.2, random_state=42)

diabetes_model = RandomForestClassifier(
    n_estimators=200, max_depth=6, random_state=42)
diabetes_model.fit(X_train, y_train)
acc = accuracy_score(y_test, diabetes_model.predict(X_test))
print(f"✅ Diabetes Accuracy: {acc*100:.2f}%")

with open('model/diabetes_model.pkl', 'wb') as f:
    pickle.dump(diabetes_model, f)
print("✅ diabetes_model.pkl saved!")

# ── Heart Disease Model ──────────────────────
heart_df = pd.read_csv('model/heart.csv')

X_h = heart_df.drop('target', axis=1)
y_h = heart_df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_h, y_h, test_size=0.2, random_state=42)

heart_model = RandomForestClassifier(
    n_estimators=200, max_depth=6, random_state=42)
heart_model.fit(X_train, y_train)
acc = accuracy_score(y_test, heart_model.predict(X_test))
print(f"✅ Heart Disease Accuracy: {acc*100:.2f}%")

with open('model/heart_model.pkl', 'wb') as f:
    pickle.dump(heart_model, f)
print("✅ heart_model.pkl saved!")