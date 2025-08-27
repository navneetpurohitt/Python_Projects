import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pandas import ExcelWriter

def read_data(file_path):
    """Reads data from a CSV file and returns a DataFrame."""
    return pd.read_excel(file_path, sheet_name='Sheet1')

# Metrics
def metrics(filtered_df):
      
    col1, col2, col3 = st.columns(3)

    # Total efforts
    total_efforts = filtered_df['Efforts (PH/Hour)'].sum()
    with col1:
        st.markdown(
            f'<div style="border: 2px solid black; padding: 10px; background-color: #e6f7ff;">'
            f'<span style="font-size: 16px; font-weight: bold;">Total Efforts (PH/Hour):</span> {total_efforts:.2f}'
            f'</div>',
            unsafe_allow_html=True
        )
        

    # Total automated efforts
    automated_efforts = filtered_df[filtered_df['Automation Status'].isin(['14. Implemented in Prod', '12. Implemented in Prod (Partially)'])]['Efforts (PH/Hour)'].sum()
    with col2:
        
        st.markdown(
        f'<div style="border: 2px solid black; padding: 10px; background-color: #e6f7ff;">'
        f'<span style="font-size: 16px; font-weight: bold;">Total Automated Efforts (PH/Hour):</span> {automated_efforts:.2f}'
        f'</div>',
        unsafe_allow_html=True
        )

    # Total number of items
    total_items = len(filtered_df)
    with col3:
        
        st.markdown(
        f'<div style="border: 2px solid black; padding: 10px; background-color: #e6f7ff;">'
        f'<span style="font-size: 16px; font-weight: bold;">Total Items:</span> {total_items:.2f}'
        f'</div>',
        unsafe_allow_html=True
        )

def filters(book_of_work_df):
    col1, col2 = st.columns(2)
    with col1:
        
    # Filters
        name_filter = col1.selectbox("Category", options=["All"] + book_of_work_df['Name'].unique().tolist(), key="name_filter")
    with col2:
        automation_status_filter = col2.selectbox("Select Automation Status", options=["All"] + book_of_work_df['Automation Status'].unique().tolist(), key="automation_status_filter")
    # Apply filters
    filtered_df = book_of_work_df.copy()

    if name_filter != "All":
        filtered_df = filtered_df[filtered_df['Name'] == name_filter]

    # Update automation status options based on name filter
    if name_filter != "All":
        automation_status_options = ["All"] + filtered_df['Automation Status'].unique().tolist()
    else:
        automation_status_options = ["All"] + book_of_work_df['Automation Status'].unique().tolist()
    if automation_status_filter != "All":
        filtered_df = filtered_df[filtered_df['Automation Status'] == automation_status_filter]
    return filtered_df

def display_df(filtered_df):
    st.dataframe(filtered_df.reset_index(drop=True))
    # Download button
    col1, col2 = st.columns(2)

    # Download as CSV
    with col1:
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        file_name = st.text_input("Enter CSV file name", value="filtered_data.csv")
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name=file_name,
            mime='text/csv',
        )

    # Download as Excel
    with col2:
        excel_file_name = st.text_input("Enter Excel file name", value="filtered_data.xlsx")
        sheet_name = st.text_input("Enter Excel sheet name", value="Sheet1")
        excel_buffer = ExcelWriter(excel_file_name, engine='xlsxwriter')
        filtered_df.to_excel(excel_buffer, index=False, sheet_name=sheet_name)
        excel_buffer.close()
        with open(excel_file_name, 'rb') as excel_file:
            st.download_button(
                label="Download data as Excel",
                data=excel_file,
                file_name=excel_file_name,
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
def display_charts(filtered_df):
    st.subheader("Charts")
    col1, col2 = st.columns(2)
    # Bar chart for Automation Status
    with col1:
        st.markdown("**Automation Status Distribution**")
        automation_status_counts = filtered_df['Automation Status'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=automation_status_counts.index, y=automation_status_counts.values, palette="viridis")
        plt.xlabel("Automation Status")
        plt.ylabel("Count")
        plt.title("Automation Status Distribution")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)
        
    # Pie chart for Name
    with col2:
        st.markdown("**Name Distribution**")
        name_counts = filtered_df['Name'].value_counts()
        plt.figure(figsize=(14, 7))
        plt.pie(name_counts, labels=name_counts.index, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        st.pyplot(plt)
def sync_details(filtered_df):
    # Save the updated DataFrame back to the Excel file
    with ExcelWriter('D:\\Projects\\Git\\Python_Projects\\Streamlit\\Streamlit\\ATS\\consolidated.xlsx', engine='xlsxwriter') as writer:
        filtered_df.to_excel(writer, index=False, sheet_name='Sheet1')
    # st.success("Data synchronized to Excel file.")
def add_details(filtered_df):
    if "show_form" not in st.session_state:
        st.session_state.show_form = False

    if st.button("Show/Hide Add Details Form"):
        st.session_state.show_form = not st.session_state.show_form

    if st.session_state.show_form:
        with st.form("add_details_form"):
            name = st.selectbox("Select Name", options=filtered_df['Name'].unique().tolist())
            gear_id = st.text_input("Enter GearID")
            sop_name = st.text_input("Enter SOP Name")
            description = st.text_area("Enter Description")
            efforts = st.number_input("Enter Efforts (PH/Hour)", min_value=0.0, step=0.1)
            automation_status = st.selectbox("Select Automation Status", options=filtered_df['Automation Status'].unique().tolist())
            remarks = st.text_area("Enter Remarks")
            submitted = st.form_submit_button("Add Details")

            if submitted:
                new_entry = {
                    'Name': name,
                    'GearID': gear_id,
                    'SOP Name': sop_name,
                    'Description': description,
                    'Efforts (PH/Hour)': efforts,
                    'Automation Status': automation_status,
                    'Remarks': remarks
                }
                filtered_df = pd.concat([filtered_df, pd.DataFrame([new_entry])], ignore_index=True)
                st.success("Details added successfully!")
                sync_details(filtered_df)
    return filtered_df

    
book_of_work_df = read_data('D:\\Projects\\Git\\Python_Projects\\Streamlit\\Streamlit\\ATS\\consolidated.xlsx')
print(book_of_work_df.columns)
# Columns:'Name', 'GearID', 'SOP Name', 'Description', 'Efforts (PH/Hour)', 'Automation Status', 'Remarks'
# Set Streamlit page configuration
st.set_page_config(layout="wide")
# Streamlit app
st.title("Book of Work")
st.markdown("-----------------------")
book_of_work_df = add_details(book_of_work_df)
# Display filtered data
st.markdown("-----------------------")
filtered_df = filters(book_of_work_df)

st.markdown("-----------------------")
metrics(filtered_df)
st.markdown("-------------------")
display_df(filtered_df)
st.markdown("-----------------------")
display_charts(filtered_df)





