# AI_Development_Workflow
This AI-powered application predicts the likelihood of a patient being readmitted to the hospital within 30 days after discharge. Built using Python, Streamlit, and Scikit-learn, it enables healthcare practitioners to identify high-risk cases early.

# 🏥 Patient Readmission Risk Predictor

This is a Streamlit-based AI application that predicts the risk of a patient being readmitted within 30 days after hospital discharge. It uses machine learning to assist hospitals in identifying high-risk patients and improving post-discharge care.

---

## 📌 Features

- 🎯 Predicts 30-day readmission risk
- 📊 Supports 7 clinical features:
  - Age
  - Gender
  - Primary Diagnosis
  - Number of Procedures
  - Days in Hospital
  - Comorbidity Score
  - Discharge Destination
- 🚥 Displays risk levels:
  - ✅ Very Low
  - ⚠️ Moderate
  - ❗ High
  - 🚨 Critical
- 🔍 Confidence score shown with progress bar
- 💾 Trained using `RandomForestClassifier` with preprocessing pipeline

---

## 🚀 Getting Started

### 1. 📂 Clone the Repository

```bash
git clone https://github.com/your-username/hospital-readmission-ai.git
cd hospital-readmission-ai
```

### 2. 📦 Install Dependencies
Install required Python packages: 
```bash 
pip install streamlit pandas scikit-learn joblib
```

### 3. ▶️ Run the App 
```bash 
streamlit run app.py
```

### How It Works
- A pre-trained machine learning model (readmission_model.pkl) is loaded at runtime.

- User inputs are passed through a preprocessing pipeline (ColumnTransformer) which:

- Scales numeric features

- One-hot encodes categorical variables

- The model outputs a probability score of readmission.

- The app displays a prediction with color-coded severity level

### 🗂 Project Structure
📁 Hospital/
├── app.py                  # Streamlit app
├── readmission_model.pkl   # Trained model with pipeline
├── train_df.csv            # Training dataset
├── test_df.csv             # Test dataset
├── README.md               # You're here

### Example Output
Input:
- Age: 72
- Gender: Female
- Diagnosis: Heart Disease
- Days in hospital: 12
- Comorbidity: 4

Output:
🚨 Critical Risk of Readmission — Confidence: 0.79

⚠️ Disclaimer
This is a demo project trained on synthetic or publicly available healthcare data.
It is not intended for clinical use without further validation.

👨‍💻 Author
Luke Mbogo
🎓 ALX AI Engineering Track | 💻 Cybersecurity Enthusiast
🌍 Nairobi, Kenya | 💡 Founder @ Lumarah Tech

“Turning data into decisions — one patient at a time.”
