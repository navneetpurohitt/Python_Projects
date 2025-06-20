import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_data(file_path):
    try: 
        df = pd.read_csv(file_path)
        print("Dataframe loaded successfully.")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    
file_path = 'Finance_data.csv'
df = load_data(file_path)


st.set_page_config(page_title="Pandas Operations", layout="wide")
st.title("Pandas Operations with Streamlit")

st.write(df)


column1, column2  = st.columns(2)
# # "gender"
if column1:
    column1.write("Gender: ")
    column1.write(df["gender"].value_counts())
    
if column2:
    column2.write("Histogram of Age: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['gender'], ax=ax)
    column2.pyplot(fig)
    

# 1:"age"\
column3, column4 = st.columns(2)
if column3:
    column3.write("Age: ")
    column3.write(df["age"].value_counts())
    
if column4:
    column4.write("Histogram of Age: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['age'], ax=ax)
    column4.pyplot(fig)
# 2:"Investment_Avenues"

column5, column6 = st.columns(2)
if column5:
    column5.write("Investment Avenues: ")
    column5.write(df["Investment_Avenues"].value_counts())
if column6:
    column6.write("Histogram of Investment Avenues: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Investment_Avenues'], ax=ax)
    column6.pyplot(fig)
# 3:"Mutual_Funds"
column7, column8 = st.columns(2)
if column7:
    column7.write("Mutual Funds: ")
    column7.write(df["Mutual_Funds"].value_counts())
if column8:
    column8.write("Histogram of Mutual Funds: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Mutual_Funds'], ax=ax)
    column8.pyplot(fig)
# 4:"Equity_Market"

column9, column10 = st.columns(2)
if column9:
    column9.write("Equity Market: ")
    column9.write(df["Equity_Market"].value_counts())
if column10:
    column10.write("Histogram of Equity Market: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Equity_Market'], ax=ax)
    column10.pyplot(fig)
# 5:"Debentures"
column11, column12 = st.columns(2)
if column11:
    column11.write("Debentures: ")
    column11.write(df["Debentures"].value_counts())
if column12:
    column12.write("Histogram of Debentures: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Debentures'], ax=ax)
    column12.pyplot(fig)

# 6:"Government_Bonds"

column13, column14 = st.columns(2)
if column13:
    column13.write("Government Bonds: ")
    column13.write(df["Government_Bonds"].value_counts())
if column14:    
    column14.write("Histogram of Government Bonds: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Government_Bonds'], ax=ax)
    column14.pyplot(fig)
# 7:"Fixed_Deposits"

column15, column16 = st.columns(2)
if column15:
    column15.write("Fixed Deposits: ")
    column15.write(df["Fixed_Deposits"].value_counts())
if column16:
    column16.write("Histogram of Fixed Deposits: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Fixed_Deposits'], ax=ax)
    column16.pyplot(fig)
# 8:"PPF"
column17, column18 = st.columns(2)
if column17:
    column17.write("PPF: ")
    column17.write(df["PPF"].value_counts())
if column18:
    column18.write("Histogram of PPF: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['PPF'], ax=ax)
    column18.pyplot(fig)
# 9:"Gold"

column19, column20 = st.columns(2)
if column19:
    column19.write("Gold: ")
    column19.write(df["Gold"].value_counts())
if column20:
    column20.write("Histogram of Gold: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Gold'], ax=ax)
    column20.pyplot(fig)
# 10:"Stock_Marktet"

column21, column22 = st.columns(2)
if column21:
    column21.write("Stock Market: ")
    column21.write(df["Stock_Marktet"].value_counts())
if column22:
    column22.write("Histogram of Stock Market: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Stock_Marktet'], ax=ax)
    column22.pyplot(fig)
# 11:"Factor"

column23, column24 = st.columns(2)
if column23:
    column23.write("Factor: ")
    column23.write(df["Factor"].value_counts())
    
if column24:
    column24.write("Histogram of Factor: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Factor'], ax=ax)
    column24.pyplot(fig)
# 12:"Objective"

column25, column26 = st.columns(2)
if column25:
    column25.write("Objective: ")
    column25.write(df["Objective"].value_counts())
if column26:
    column26.write("Histogram of Objective: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Objective'], ax=ax)
    column26.pyplot(fig)
# 13:"Purpose"
column27, column28 = st.columns(2)
if column27:
    column27.write("Purpose: ")
    column27.write(df["Purpose"].value_counts())
    
if column28:
    column28.write("Histogram of Purpose: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Purpose'], ax=ax)
    column28.pyplot(fig)
# 14:"Duration"

column29, column30 = st.columns(2)
if column29:
    column29.write("Duration: ")
    column29.write(df["Duration"].value_counts())
if column30:
    column30.write("Histogram of Duration: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Duration'], ax=ax)
    column30.pyplot(fig)
# 15:"Invest_Monitor"
column31, column32 = st.columns(2)
if column31:
    column31.write("Investment Monitor: ")
    column31.write(df["Invest_Monitor"].value_counts())
if column32:
    column32.write("Histogram of Investment Monitor: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Invest_Monitor'], ax=ax)
    column32.pyplot(fig)
# 16:"Expect"
column33, column34 = st.columns(2)
if column33:
    column33.write("Expect: ")
    column33.write(df["Expect"].value_counts())
if column34:
    column34.write("Histogram of Expect: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Expect'], ax=ax)
    column34.pyplot(fig)
# 17:"Avenue"
column35, column36 = st.columns(2)
if column35:
    column35.write("Avenue: ")
    column35.write(df["Avenue"].value_counts())
if column36:
    column36.write("Histogram of Avenue: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Avenue'], ax=ax)
    column36.pyplot(fig)
# 18:"What are your savings objectives?"
column37, column38 = st.columns(2)
if column37:
    column37.write("Savings Objectives: ")
    column37.write(df["What are your savings objectives?"].value_counts())
if column38:
    column38.write("Histogram of Savings Objectives: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['What are your savings objectives?'], ax=ax)
    column38.pyplot(fig)
# 19:"Reason_Equity"
column39, column40 = st.columns(2)
if column39:
    column39.write("Reason for Equity: ")
    column39.write(df["Reason_Equity"].value_counts())
if column40:

    column40.write("Histogram of Reason for Equity: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Reason_Equity'], ax=ax)
    column40.pyplot(fig)
    
# 20:"Reason_Mutual"
column41, column42 = st.columns(2)
if column41:
    column41.write("Reason for Mutual Funds: ")
    column41.write(df["Reason_Mutual"].value_counts())
if column42:
    column42.write("Histogram of Reason for Mutual Funds: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Reason_Mutual'], ax=ax)
    column42.pyplot(fig)
    
# 21:"Reason_Bonds"
column43, column44 = st.columns(2)
if column43:
    column43.write("Reason for Bonds: ")
    column43.write(df["Reason_Bonds"].value_counts())
if column44:
    column44.write("Histogram of Reason for Bonds: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Reason_Bonds'], ax=ax)
    column44.pyplot(fig)
# 22:"Reason_FD"
column45, column46 = st.columns(2)
if column45:
    column45.write("Reason for Fixed Deposits: ")
    column45.write(df["Reason_FD"].value_counts())
if column46:
    column46.write("Histogram of Reason for Fixed Deposits: ")
    fig, ax = plt.subplots(figsize=(6, 1.5))
    sns.histplot(df['Reason_FD'], ax=ax)
    column46.pyplot(fig)
# 23:"Source"
column47, column48 = st.columns(2)
if column47:
    column47.write("Source: ")
    column47.write(df["Source"].value_counts()) 
if column48:
    column48.write("Histogram of Source: ")
    fig, ax = plt.subplots(figsize=(8, 1.5))
    sns.barplot(x=df['Source'].value_counts().index, y=df['Source'].value_counts().values, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    column48.pyplot(fig)
   
df1 = df.groupby(['gender','Reason_Mutual']).size().reset_index(name='counts')
st.write(df1)
    
    # plot a graph as per gender and Mutual Funds
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(df1, x = 'gender', y = 'counts', hue = 'Reason_Mutual', ax=ax)
st.pyplot(fig)

df1 = df.groupby(['gender', 'Objective']).size().reset_index(name = 'counts')

   # plot a graph as per gender and Mutual Funds
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(df1, x = 'gender', y = 'counts', hue = 'Objective', ax=ax)
st.pyplot(fig)