import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('readmission_model.pkl')

st.title("🏥 Patient Readmission Predictor")

# Collect all required inputs
age = st.selectbox("Age", options=["18", "25", "32", "47", "52", "60", "72"])
gender = st.selectbox("Gender", options=["Male", "Female"])
primary_diagnosis = st.selectbox("Primary Diagnosis", options=["Diabetes", "Heart Disease", "COPD"])
num_procedures = st.number_input("Number of Procedures", min_value=0, max_value=20, value=2)
days_in_hospital = st.slider("Days in Hospital", min_value=1, max_value=30, value=5)
comorbidity_score = st.slider("Comorbidity Score", min_value=0, max_value=5, value=2)
discharge_to = st.selectbox("Discharge To", options=["Home", "Skilled Nursing Facility", "Rehabilitation Facility"])

# Prediction button
# Prediction button
if st.button("Predict Readmission Risk"):
    input_df = pd.DataFrame([{
        'age': age,
        'gender': gender,
        'primary_diagnosis': primary_diagnosis,
        'num_procedures': num_procedures,
        'days_in_hospital': days_in_hospital,
        'comorbidity_score': comorbidity_score,
        'discharge_to': discharge_to
    }])

    # Predict using model
    prob = model.predict_proba(input_df)[0][1]  # Probability of readmission (class 1)
    threshold = 0.4  # Custom threshold for sensitivity — feel free to adjust
    pred = int(prob > threshold)

    # Debug: Show raw prediction and probability
    st.write("### 🧪 Prediction Debug Info")
    st.write(f"Raw prediction (above threshold): `{pred}`")
    st.write(f"Risk score (probability): `{round(prob, 2)}`")

    # Visual display of risk score
    st.progress(prob)

    # Final output
   # Final output
st.write("### 🔍 Prediction Result:")

# Final output (tightened scale)
if prob < 0.15:
    st.success(f"✅ Very Low Risk of Readmission — Confidence: {round(prob, 2)}")
elif prob < 0.3:
    st.warning(f"⚠️ Moderate Risk — Confidence: {round(prob, 2)}")
elif prob < 0.45:
    st.error(f"❗ High Risk — Confidence: {round(prob, 2)}")
else:
    st.error(f"🚨 Critical Risk — Confidence: {round(prob, 2)}")
