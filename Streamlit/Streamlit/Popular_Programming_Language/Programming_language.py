import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.set_page_config(page_title="Programming Languages Data", layout="wide")
st.title("Popular Programming Languages Data")

st.sidebar.title("Filter")

# Sample data with the specified columns
# Convert the data into a DataFrame
df = pd.read_csv("Dataset.csv")


df['Date'] = pd.to_datetime(df['Date'], format='%B %Y', errors='coerce')

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m', errors='coerce')
# Display the DataFrame in the Streamlit app

st.sidebar.subheader("Filter by year")
# Create a slider to filter by year
year_filter = st.sidebar.slider(
    "Select Year Range",
    min_value=2004,
    max_value=2024,
    value= 2024,
    step=1
)
month_filter = st.sidebar.selectbox(
    "Select Month",
    options=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    index=0
)

filtered_month = df[df['Date'].dt.month_name() == month_filter]

st.sidebar.write(f"Selected Year: {year_filter}")
st.sidebar.write(f"Selected Month: {month_filter}")


# Filter the DataFrame based on the selected year
filtered_df = df[df['Date'].dt.year == year_filter]
filtered_df = filtered_df[filtered_df['Date'].dt.month_name() == month_filter]
st.write(f"Filtered Data for {year_filter}:")
# st.dataframe(filtered_df)

sum_row = filtered_df.sum(numeric_only=True, axis = 0).sort_values(ascending=True)
# Display the sum in the sidebar
# st.write(sum_row)
# Display the sum in the main area

import matplotlib.pyplot as plt
# Create a horizontal bar chart for sum_row
fig, ax = plt.subplots()
fig.set_figwidth(10 )  # Set the width of the figure
fig.set_figheight(10)  # Set the height of the figure
sum_row.plot(kind='barh', ax=ax, color='blue')
ax.set_title(f"{year_filter} Popular")
ax.set_xlabel("Sum")
ax.set_ylabel("Languages")

# Annotate the bars with their values (count)
for i, v in enumerate(sum_row):
    ax.text((v + 0.5), i, str(int(v)) + "%", color='black', va='center')

# Display the chart in the Streamlit app
st.pyplot(fig)

