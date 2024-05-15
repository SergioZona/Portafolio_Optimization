import streamlit as st  # library for building interactive web apps
import pandas as pd  # Pandas library for data manipulation and analysis
import numpy as np  # NumPy library for numerical computing
from datetime import date  # Importing date class from datetime module for handling dates

# Libraries for retrieving and downloading data
import requests  # Making HTTP requests
from io import BytesIO  # Working with binary data streams
import yfinance as yf  # Yahoo Finance library for retrieving financial data
import base64  # Encoding and decoding binary data to/from ASCII
# Plotting libraries
import plotly.express as px  # Plotly Express for creating interactive plots
import plotly.graph_objects as go  # Plotly Graph Objects for creating more customizable plots

class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
@st.cache(allow_output_mutation=True)
def get_session():
    return SessionState(df=pd.DataFrame())
session_state = get_session()
# Creating a dictionary with some data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 35, 40, 25]
}
# Creating a DataFrame with the data
df = pd.DataFrame(data)
# Assigning this DataFrame to session_state
session_state.df = df