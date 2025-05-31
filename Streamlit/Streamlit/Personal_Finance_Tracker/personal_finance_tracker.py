import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title  = "Personal Finance Tracker", layout="wide")
st.title("Personal Finance Tracker")

finance_df = pd.read_csv("Finance_tracker.csv")

if finance_df.empty:
    st.warning("No data available. Please upload your finance tracker CSV file.")

else:
    
    st.subheader("Download Data")
    csv = finance_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='finance_tracker.csv',
        mime='text/csv',
    )
    st.subheader("Data Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Income", f"{finance_df['Price'].loc[finance_df['Money']== 'Credit'].sum()}")    
    with col2:
        st.metric("Total Expenditure", f"{finance_df['Price'].loc[finance_df['Money']== 'Debit'].sum()}")    
    st.dataframe(finance_df)
    st.subheader("Data Visualization")
    col1, col2, col3 = st.columns(3)
    with col1:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=finance_df, x='Category', y='Price', ax=ax)
        ax.set_title("Total Price by Item")
        ax.set_xlabel("Category")
        ax.set_ylabel("Price (Rupees)")
        for container in ax.containers:
            ax.bar_label(container, fmt='%.2f', label_type='edge')
        st.pyplot(fig)
   
   
    with col2:
        fig, ax = plt.subplots(figsize=(8, 6))
        plt.pie(finance_df['Category'].value_counts(), autopct='%1.1f%%', startangle=140, labels = finance_df['Category'].unique())
        ax.set_title("Category Distribution")
        st.pyplot(fig)
        st.caption("Pie chart showing the distribution of categories in the finance tracker.")
   
    
        

