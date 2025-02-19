import streamlit as st
import pandas as pd
import numpy as np
class element:
    def __init__(self,data):
        self.data=data
    def predict(self):
        with st.container():
         st.write('****')
         st.write("**predictname**")
    def accuracy(self):
        with st.container():
         st.write('****')
         st.write("**0.95**")
    def download(self):
       st.write('****')
       st.button("📥",key=2)
class data:
    def __init__(self,name,accuracy,link):
        self.name=name
        self.accuracy=accuracy
        self.link=link
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
if page == "Models":
   mo=data("moundher","0.90","link")
   wid=element(mo)
   st.header("Your models")
   col1, col2, col3 = st.columns(3)
   with col1:
    with st.container():
        st.markdown("### Name")
        wid.predict()
    with col2:
     with st.container():
        st.markdown("### Accuracy")
        wid.accuracy()
    with col3:
     with st.container():
        st.markdown("### Download")
        wid.download()







