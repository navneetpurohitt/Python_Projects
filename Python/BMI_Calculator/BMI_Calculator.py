import streamlit as st
import pandas as pd

df = pd.read_csv("bmi_calc.csv")


st.title("BMI Calculator")
weight = st.sidebar.text_input("Enter  weight in kg")
height =st.sidebar.selectbox(
    "Select your height (in cm):", 
    list(range(100, 226))  # This creates a list from 100 to 225
)
submit = st.sidebar.button("Calculate BMI")
bmi = 0.0
if submit:
    try:
        weight = float(weight)
        height = float(height) / 100  # Convert cm to m
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}") 
# Classification,BMI_range_kg/m2
# Severe Thinness,<16
# Moderate Thinness,16 - 17
# Mild Thinness,17 - 18.5
# Normal,18.5 - 25
# Overweight,25 - 30
# Obese Class I,30 - 35
# Obese Class II,35 - 40
# # Obese Class III, > 40
        if bmi < 16:
            st.write("Classification: Severe Thinness")
        elif 16 <= bmi < 17:    
            st.write("Classification: Moderate Thinness")   
        elif 17 <= bmi < 18.5:  
            st.write("Classification: Mild Thinness")
        elif 18.5 <= bmi < 25:  
            st.write("Classification: Normal")
        elif 25 <= bmi < 30:
            st.write("Classification: Overweight")
        elif 30 <= bmi < 35:
            st.write("Classification: Obese Class I")
        elif 35 <= bmi < 40:
            st.write("Classification: Obese Class II")
        else:   
            st.write("Classification: Obese Class III")
        # Add the new entry to the DataFrame        
    except ValueError:
        st.error("Please enter valid numbers for weight and height.")
else:
    st.warning("Please enter your weight and height to calculate BMI.")

st.write(df)