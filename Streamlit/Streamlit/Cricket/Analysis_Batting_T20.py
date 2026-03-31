import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    url = 't20.csv'
    data = pd.read_csv(url)
    return data
data = load_data()
st.title('T20 Batting Analysis')

# data.drop(["Unnamed: 0","Unnamed: 15"], axis = 1, inplace=True)

# Data Cleaning
data.columns = data.columns.str.strip()

data["HS"] = data["HS"].apply((lambda x: x.split("*")[0] if isinstance(x, str) else x))
data["HS"] = data["HS"].replace("-", 0)

print(data.isnull().sum())
data["Runs"] = data["Runs"].replace("-", 0)
data["Ave"] = data["Ave"].replace("-", 0)
data["Runs"] = data["Runs"].astype(int)
data["Ave"] = data["Ave"].astype(float)
data["HS"] = data["HS"].astype(int)
data["SR"] = data["SR"].replace("-", 0)
data["SR"] = data["SR"].astype(float)
st.write(data)
col1, col2 = st.columns(2)
if col1:
    # total Runs

    col1.metric("Highest Runs", data["Runs"].max())
    highest_scorer = data.loc[data["Runs"].idxmax(), "Player"]
    col1.metric("Highest Runs", highest_scorer)

if col2:
    col2.metric("Highest Average", data["Ave"].max())
    highest_averager = data.loc[data["Ave"].idxmax(), "Player"]
    col2.metric("Highest Average", highest_averager)

st.write("--------------------------------------------------------------------------------")
col3, col4 = st.columns(2)
if col3:
    # total Matches
    col3.metric("Highest Individual Score", data["HS"].max())
    highest_score_player = data.loc[data["HS"].idxmax(), "Player"]
    col3.metric("Highest Individual Score", highest_score_player)
if col4:
    # Strike Rate
    col4.metric("Highest Strike Rate", data["SR"].max())
    highest_strike_rate_player = data.loc[data["SR"].idxmax(), "Player"]
    col4.metric("Highest Strike Rate", highest_strike_rate_player)

