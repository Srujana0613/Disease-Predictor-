import os
import pickle
import numpy as np

# Load both models with absolute model folder path
model_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(model_dir, 'diabetes_model.pkl'), 'rb') as f:
    diabetes_model = pickle.load(f)

with open(os.path.join(model_dir, 'heart_model.pkl'), 'rb') as f:
    heart_model = pickle.load(f)

def predict_diabetes(pregnancies, glucose, bp, skin, insulin, bmi, dpf, age):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = diabetes_model.predict(input_data)[0]
    probability = diabetes_model.predict_proba(input_data)[0]
    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        if confidence >= 80:
            risk = "High Risk 🔴"
        else:
            risk = "Medium Risk 🟡"
    else:
        risk = "Low Risk 🟢"

    tips = []
    if glucose > 140:
        tips.append("Reduce sugar and carbohydrate intake")
    if bmi > 30:
        tips.append("Maintain a healthy weight through diet and exercise")
    if bp > 80:
        tips.append("Monitor blood pressure regularly")
    if age > 45:
        tips.append("Get regular diabetes screenings")
    if not tips:
        tips.append("Keep up your healthy lifestyle! 🌟")

    return {
        "disease": "Diabetes",
        "result": "Diabetic ⚠️" if prediction == 1 else "Not Diabetic ✅",
        "risk": risk,
        "confidence": confidence,
        "tips": tips
    }

def predict_heart(age, sex, cp, trestbps, chol, fbs,
                  restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = heart_model.predict(input_data)[0]
    probability = heart_model.predict_proba(input_data)[0]
    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        if confidence >= 80:
            risk = "High Risk 🔴"
        else:
            risk = "Medium Risk 🟡"
    else:
        risk = "Low Risk 🟢"

    tips = []
    if chol > 200:
        tips.append("Reduce cholesterol — avoid fried and fatty foods")
    if trestbps > 130:
        tips.append("Control blood pressure with diet and medication")
    if thalach < 100:
        tips.append("Improve cardiovascular fitness with regular exercise")
    if fbs == 1:
        tips.append("Manage blood sugar levels carefully")
    if not tips:
        tips.append("Keep up your healthy heart habits! 💚")

    return {
        "disease": "Heart Disease",
        "result": "At Risk ⚠️" if prediction == 1 else "Healthy ✅",
        "risk": risk,
        "confidence": confidence,
        "tips": tips
    }