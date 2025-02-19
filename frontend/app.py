import streamlit as st
import pandas as pd
import numpy as np
from widgets import element
from classes import data
import requests
import extra_streamlit_components as stx 


API_URL = "http://127.0.0.1:8000"
def get_cookie_manager():
    return stx.CookieManager()

cookie_manager = get_cookie_manager()

if cookie_manager.get("auth_token")==None:
    st.session_state.authenticated = False
if not cookie_manager.get("auth_token"):
    st.session_state.token = None

def login(username, password):
    response = requests.post(f"{API_URL}/login/", json={"username": username, "password": password})
    if response.status_code == 200:
        st.session_state.authenticated = True
        st.session_state.token = response.json()["token"]
        cookie_manager.set("auth_token", response.json()["token"]) 
        st.session_state.user = username
        st.success("Login successful! 🎉")
        st.rerun()
    else:
        st.error("Invalid credentials.")

def logout():
    st.session_state.authenticated = False
    st.session_state.token = None
    cookie_manager.set("auth_token", None) 
    st.rerun()
def signup(username, password):
    response = requests.post(f"{API_URL}/register/", json={"username": username, "password": password})
    if response.status_code == 200:
        st.session_state.authenticated = True
        st.session_state.token = response.json()["token"]
        st.session_state.user = username
        cookie_manager.set("auth_token", response.json()["token"]) 
        st.success("Login successful! 🎉")
        st.rerun()
    else:
        st.error("Invalid credentials.")

if not st.session_state.authenticated:
    st.title("Authentication")
    st.write(f"st.session_state.authenticated: {st.session_state.authenticated}")
    st.write(f"st.session_state.token: {st.session_state.token}")

    with st.form("login_form"):
     username = st.text_input("Username")
     password = st.text_input("Password", type="password")
    
     st.write("")  # Add spacing
     col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])  
    
     with col2:
        login_button = st.form_submit_button("Login", icon="🔑")
     with col4:
        signup_button = st.form_submit_button("Sign up", icon="📝")
    if login_button:
        login(username, password)
    elif signup_button:
        signup(username, password)
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









