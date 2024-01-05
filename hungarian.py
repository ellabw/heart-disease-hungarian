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
  page_title="Heart Disease Oracle",
  page_icon=":crystal_ball:"
)

st.title("Heart Disease Oracle")
st.write("🔮 Predict the likelihood of heart disease based on mystical insights and user input.")

st.write(f"**Mystical Model:** XGBoost")
st.write(f"**Accuracy Enchantment:** {accuracy}%")
st.write(f"**Dataset Prophecy:** [Hungarian Heart Disease Dataset](source_link)")

tab1, tab2 = st.tabs(["Single Vision", "Batch Prophecy"])

with tab1:
  st.sidebar.header("User Incantation")
  st.sidebar.subheader("Single Vision")
  st.sidebar.write("Channel your energy and fill in the mystic details:")
  st.sidebar.write("")

  age = st.sidebar.number_input(label="Age (in lunar cycles)", min_value=df_final['age'].min(), max_value=df_final['age'].max())
  # ... (input lainnya)

  predict_btn = st.sidebar.button("Reveal Destiny", type="primary")

  st.subheader("User Input as Cosmic Scrolls")
  st.write("")
  st.dataframe(preview_df.iloc[:, :6])
  st.write("")
  st.dataframe(preview_df.iloc[:, 6:])
  st.write("")

  result = ":crystal_ball:"

  st.write("")
  st.write("")
  st.subheader("Prophecy Unveiled:")

  if predict_btn:
    inputs = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]]
    prediction = model.predict(inputs)[0]

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 101):
      status_text.text(f"{i}% transcendent")
      bar.progress(i)
      time.sleep(0.01)
      if i == 100:
        time.sleep(1)
        status_text.empty()
        bar.empty()

    if prediction == 0:
      result = ":sparkles: Healthy"
    elif prediction == 1:
      result = ":orange_heart: Heart Harmony"
    elif prediction == 2:
      result = ":heartbeat: Heart Harmony Intensifies"
    elif prediction == 3:
      result = ":revolving_hearts: Heart Discord"
    elif prediction == 4:
      result = ":broken_heart: Heart Catastrophe"

  st.subheader(result)

with tab2:
  st.header("Batch Prophecy")

  sample_csv = df_final.iloc[:5, :-1].to_csv(index=False).encode('utf-8')
  st.write("")
  st.download_button("Download Mystic CSV Example", data=sample_csv, file_name='sample_heart_disease_parameters.csv', mime='text/csv')

  st.write("")
  st.write("")
  file_uploaded = st.file_uploader("Upload a CSV of Crystal Ball Readings", type='csv')

  if file_uploaded:
    uploaded_df = pd.read_csv(file_uploaded)
    prediction_arr = model.predict(uploaded_df)

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 70):
      status_text.text(f"{i}% mystified")
      bar.progress(i)
      time.sleep(0.01)

    result_arr = []

    for prediction in prediction_arr:
      if prediction == 0:
        result = "Balance Restored"
      elif prediction == 1:
        result = "Harmonious Heart"
      elif prediction == 2:
        result = "Heart Harmony Ascendant"
      elif prediction == 3:
        result = "Heart Imbalance"
      elif prediction == 4:
        result = "Heart Catastrophe Warning"
      result_arr.append(result)

    uploaded_result = pd.DataFrame({'Prophecy Outcome': result_arr})

    for i in range(70, 101):
      status_text.text(f"{i}% unveiled")
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
