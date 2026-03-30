# 🩺 Disease Risk Predictor

> A Full Stack ML web app to predict Diabetes and Heart Disease risk with personalized health tips.

---

## 🚀 Live Demo
Run locally at `http://127.0.0.1:5000`

---

## ✨ Features
- 🩸 Diabetes risk prediction
- ❤️ Heart Disease risk prediction  
- 🔴 Risk level — High / Medium / Low
- 💡 Personalized health tips
- ✅ Form validation with jQuery
- 📱 Responsive Bootstrap UI

---

## 🛠️ Tech Stack
| | Technology |
|---|---|
| Frontend | HTML5, Bootstrap 5, jQuery |
| Backend | Flask (Python) |
| ML Model | Random Forest — Scikit-learn |
| Templating | Jinja2 |

---

## 🤖 Model Performance
| Disease | Accuracy |
|---|---|
| 🩸 Diabetes | 74% |
| ❤️ Heart Disease | 86% |

---

## ⚙️ Setup & Run
```bash
# 1. Clone the repo
git clone https://github.com/yourusername/Disease-Risk-Predictor.git
cd Disease-Risk-Predictor

# 2. Install dependencies
pip install flask scikit-learn pandas numpy

# 3. Train the models
python model/train_model.py

# 4. Run the app
python app.py
```
Open → `http://127.0.0.1:5000`

---

## 📁 Structure
```
Disease-Risk-Predictor/
├── app.py
├── model/
│   ├── train_model.py
│   ├── predict.py
│   ├── diabetes.csv
│   └── heart.csv
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    ├── js/script.js
    └── images/
```

---

## 🎯 SDG 3 — Good Health & Well-Being
This project supports early disease detection using ML — contributing to UN SDG Goal 3.

---

## 👩‍💻 Developed by Srujana
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

> ⚠️ For educational purposes only. Not a substitute for medical advice.
