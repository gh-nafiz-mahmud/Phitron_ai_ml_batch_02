import streamlit as st

user_name = st.text_input("Enter your name: ")
user_age = st.
user_occupation = st.selectbox(
    "Choose your occupaton",
    ("Student",
     "Software Engineer",
     "Networking Engineer",
     "Data Scienctist",
     "ML Engineer",
     "AI Engineer"),
     index = None
     accept_new_option = True
)