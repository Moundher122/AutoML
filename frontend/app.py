import streamlit as st
import pandas as pd
import numpy as np
from widgets import element
from classes import data
import streamlit as st

import streamlit as st

# Hardcoded users (Replace with a database later)
USERS = {
    "moundher@gmail.com": "123",
    "user@example.com": "mypassword"
}

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login function
def login(email, password):
    if email in USERS and USERS[email] == password:
        st.session_state.authenticated = True
        st.session_state.user = email
        st.success("Login successful! 🎉")
        st.rerun()
    else:
        st.error("Invalid email or password.")

def logout():
    st.session_state.authenticated = False
    st.rerun()

if not st.session_state.authenticated:
    st.title("Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    if login_button:
        login(email, password)

else:
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
 if page == "Profile":
    st.header("👤 Profile")
    st.markdown(f"**Email:** {st.session_state.user}")
    if st.button("🚪 Logout"):
       logout()  









