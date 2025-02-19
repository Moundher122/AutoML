import streamlit as st
import pandas as pd
import numpy as np
page = st.sidebar.radio("", [ "Models","New Model", "Profile"])
if page == "New Model":
    st.header("📈 Create a new model")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
      df = pd.read_csv(uploaded_file)
      st.write("📊 Preview of the uploaded file:")
      st.dataframe(df)
    st.text_input('entre target collumn name')
    option = st.selectbox("Select a category:", ["Regression", "Classification"])
    st.write('You selected:', option)
    if st.button('Create Model'):
       page = "Models"
       st.rerun()
