import streamlit as st
from Section11_7 import section_11_7

# Set up page title
st.title("Calculus 3 Study Guide Messiah University")

# Sidebar Navigation
st.sidebar.title("Main Menu")
page = st.sidebar.radio("Select a Practice Section:", [
    "Section 11.7",
    "Section 12.1",
    "Section 12.2",
    "Section 12.3",
    "Section 12.4",
    "Section 12.5",
    "Section 13.1",
    "Section 13.2",
    "Section 13.3",
    "Section 13.4",
    "Section 13.5",
])

if page == "Section 11.7":
    section_11_7()
else:
    st.write("This section is under development. Stay tuned!")
