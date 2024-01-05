import itertools
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score
import streamlit as st
import time
import pickle

# ... (kode lainnya tetap sama)

# ========================================================================================================================================================================================

# STREAMLIT
st.set_page_config(
  page_title="Heart Disease Prediction App",
  page_icon=":heart:"
)

st.title("Heart Disease Prediction App")
st.write("Predict the likelihood of heart disease based on user input.")

st.write(f"**Model Type:** XGBoost")
st.write(f"**Accuracy:** {accuracy}%")
st.write(f"**Dataset Source:** [Hungarian Heart Disease Dataset](source_link)")

tab1, tab2 = st.tabs(["Single Prediction", "Batch Prediction"])

with tab1:
  st.sidebar.header("User Input")
  st.sidebar.subheader("Single Prediction")
  st.sidebar.write("Fill in the following details:")
  st.sidebar.write("")

  age = st.sidebar.number_input(label="Age", min_value=df_final['age'].min(), max_value=df_final['age'].max())
  # ... (input lainnya)

  predict_btn = st.sidebar.button("Predict", type="primary")

  st.subheader("User Input as DataFrame")
  st.write("")
  st.dataframe(preview_df.iloc[:, :6])
  st.write("")
  st.dataframe(preview_df.iloc[:, 6:])
  st.write("")

  result = ":violet[-]"

  st.write("")
  st.write("")
  st.subheader("Prediction:")

  if predict_btn:
    inputs = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]]
    prediction = model.predict(inputs)[0]

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 101):
      status_text.text(f"{i}% complete")
      bar.progress(i)
      time.sleep(0.01)
      if i == 100:
        time.sleep(1)
        status_text.empty()
        bar.empty()

    if prediction == 0:
      result = ":green[**Healthy**]"
    elif prediction == 1:
      result = ":orange[**Heart disease level 1**]"
    elif prediction == 2:
      result = ":orange[**Heart disease level 2**]"
    elif prediction == 3:
      result = ":red[**Heart disease level 3**]"
    elif prediction == 4:
      result = ":red[**Heart disease level 4**]"

  st.subheader(result)

with tab2:
  st.header("Batch Prediction")

  sample_csv = df_final.iloc[:5, :-1].to_csv(index=False).encode('utf-8')
  st.write("")
  st.download_button("Download CSV Example", data=sample_csv, file_name='sample_heart_disease_parameters.csv', mime='text/csv')

  st.write("")
  st.write("")
  file_uploaded = st.file_uploader("Upload a CSV file", type='csv')

  if file_uploaded:
    uploaded_df = pd.read_csv(file_uploaded)
    prediction_arr = model.predict(uploaded_df)

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 70):
      status_text.text(f"{i}% complete")
      bar.progress(i)
      time.sleep(0.01)

    result_arr = []

    for prediction in prediction_arr:
      if prediction == 0:
        result = "Healthy"
      elif prediction == 1:
        result = "Heart disease level 1"
      elif prediction == 2:
        result = "Heart disease level 2"
      elif prediction == 3:
        result = "Heart disease level 3"
      elif prediction == 4:
        result = "Heart disease level 4"
      result_arr.append(result)

    uploaded_result = pd.DataFrame({'Prediction Result': result_arr})

    for i in range(70, 101):
      status_text.text(f"{i}% complete")
      bar.progress(i)
      time.sleep(0.01)
      if i == 100:
        time.sleep(1)
        status_text.empty()
        bar.empty()

    col1, col2 = st.columns([1, 2])

    with col1:
      st.dataframe(uploaded_result)
    with col2:
      st.dataframe(uploaded_df)
