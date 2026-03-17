from flask import Flask, render_template, request
import sys
sys.path.append('model')
from predict import predict_diabetes, predict_heart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        disease = request.form['disease']

        if disease == 'diabetes':
            result = predict_diabetes(
                float(request.form['pregnancies']),
                float(request.form['glucose']),
                float(request.form['bp']),
                float(request.form['skin']),
                float(request.form['insulin']),
                float(request.form['bmi']),
                float(request.form['dpf']),
                float(request.form['age'])
            )

        elif disease == 'heart':
            result = predict_heart(
                float(request.form['age']),
                float(request.form['sex']),
                float(request.form['cp']),
                float(request.form['trestbps']),
                float(request.form['chol']),
                float(request.form['fbs']),
                float(request.form['restecg']),
                float(request.form['thalach']),
                float(request.form['exang']),
                float(request.form['oldpeak']),
                float(request.form['slope']),
                float(request.form['ca']),
                float(request.form['thal'])
            )

        return render_template('index.html',
            result   = result['result'],
            risk     = result['risk'],
            confidence = result['confidence'],
            tips     = result['tips'],
            disease  = result['disease']
        )

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)