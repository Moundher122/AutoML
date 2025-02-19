import streamlit as st
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
    
   