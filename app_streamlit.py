
import streamlit as st
import numpy as np
import joblib

data = joblib.load('model.joblib')
pipe = data['model']
features = data['features']

st.set_page_config(page_title="Wine Quality Predictor", page_icon="🍷", layout="centered")

st.title("🍷 Wine Quality Predictor")
st.write("Enter physicochemical properties to predict quality (0–10). Model trained on the UCI Red Wine Quality dataset.")

defaults = {
    'fixed acidity': 7.4,
    'volatile acidity': 0.70,
    'citric acid': 0.00,
    'residual sugar': 1.90,
    'chlorides': 0.076,
    'free sulfur dioxide': 11.0,
    'total sulfur dioxide': 34.0,
    'density': 0.9978,
    'pH': 3.51,
    'sulphates': 0.56,
    'alcohol': 9.4,
}

vals = []
cols = st.columns(2)
for i, f in enumerate(features):
    with cols[i % 2]:
        step = 1.0 if f in ['free sulfur dioxide', 'total sulfur dioxide'] else 0.01
        val = st.number_input(f, value=float(defaults.get(f, 0.0)), step=step, format="%.5f" if step==0.01 else "%.2f")
        vals.append(val)

if st.button("Predict quality"):
    arr = np.array(vals).reshape(1, -1)
    pred = pipe.predict(arr)[0]
    score = float(np.round(pred, 1))
    st.metric("Predicted quality", score)
    if score < 5.0:
        label = "Poor"
    elif score < 6.0:
        label = "Acceptable"
    elif score < 7.0:
        label = "Good"
    else:
        label = "Excellent"
    st.success(f"Estimated rating: {label}")
