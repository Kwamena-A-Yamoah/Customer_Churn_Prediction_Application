import streamlit as st
import pandas as pd

st.title("View Data")

# Load data
@st.cache_data(persist= True)
def load_data():
    data = pd.read_csv(r'data/cleaned_data.csv')
    return data

st.dataframe(load_data())

# st.write('Summary Statistics')
# st.write(load_data().describe())