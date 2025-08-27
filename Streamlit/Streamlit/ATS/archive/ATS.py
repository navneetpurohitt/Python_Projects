import streamlit as st
import pandas as pd

# Sample data for the first page
data = [
    {"Category": "Category1", "Sub-Category": "Sub1", "Business Unit": "BU1", "Gear ID": "G1", "SDM Name": "SDM1", "SME Name": "SME1"},
    {"Category": "Category2", "Sub-Category": "Sub2", "Business Unit": "BU2", "Gear ID": "G2", "SDM Name": "SDM2", "SME Name": "SME2"},
]
df = pd.DataFrame(data)
# Add cards for showing records at Category and Business Unit levels
st.subheader("Category Level Summary")
categories = df['Category'].value_counts()
for category, count in categories.items():
    st.info(f"**{category}:** {count} record(s)")

st.subheader("Business Unit Level Summary")
business_units = df['Business Unit'].value_counts()
for bu, count in business_units.items():
    st.info(f"**{bu}:** {count} record(s)")

# Add a button to toggle the visibility of the "Add New Record" form
if "show_add_record_form" not in st.session_state:
    st.session_state.show_add_record_form = False

if st.button("Add New Record"):
    st.session_state.show_add_record_form = not st.session_state.show_add_record_form

if st.session_state.show_add_record_form:
    with st.form("add_record_form"):
        new_category = st.text_input("Category")
        new_sub_category = st.text_input("Sub-Category")
        new_business_unit = st.text_input("Business Unit")
        new_gear_id = st.text_input("Gear ID")
        new_sdm_name = st.text_input("SDM Name")
        new_sme_name = st.text_input("SME Name")
        submitted = st.form_submit_button("Add Record")
        if submitted:
            new_record = {
                "Category": new_category,
                "Sub-Category": new_sub_category,
                "Business Unit": new_business_unit,
                "Gear ID": new_gear_id,
                "SDM Name": new_sdm_name,
                "SME Name": new_sme_name,
            }
            df = df.append(new_record, ignore_index=True)
            st.success("Record added successfully!")

sop_details = [
    {"SOP Name": "SOP1", "KA ID": "KA1", "SP Path": "/path1", "Manual Efforts": "10h", "Categories": "Cat1", "Sub Categories": "SubCat1"},
    {"SOP Name": "SOP2", "KA ID": "KA2", "SP Path": "/path2", "Manual Efforts": "15h", "Categories": "Cat2", "Sub Categories": "SubCat2"},
]

# Convert data to DataFrame
df = pd.DataFrame(data)
sop_df = pd.DataFrame(sop_details)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "SOP Details"])

if page == "Home":
    st.title("Home Page")
    st.subheader("Table View")
    st.dataframe(df)

    st.subheader("Card View")
    for index, row in df.iterrows():
        with st.expander(f"{row['Category']} - {row['Sub-Category']}"):
            st.write(f"**Business Unit:** {row['Business Unit']}")
            st.write(f"**Gear ID:** {row['Gear ID']}")
            st.write(f"**SDM Name:** {row['SDM Name']}")
            st.write(f"**SME Name:** {row['SME Name']}")
            if st.button(f"View SOP Details for {row['Category']}", key=index):
                st.session_state.selected_category = row['Category']
                st.session_state.page = "SOP Details"

    
elif page == "SOP Details":
    st.title("SOP Details Page")
    st.dataframe(sop_df)

    st.subheader("Add New SOP Record")
    with st.form("add_sop_form"):
        sop_name = st.text_input("SOP Name")
        ka_id = st.text_input("KA ID")
        sp_path = st.text_input("SP Path")
        manual_efforts = st.text_input("Manual Efforts")
        categories = st.text_input("Categories")
        sub_categories = st.text_input("Sub Categories")
        submitted = st.form_submit_button("Add SOP Record")
        if submitted:
            new_sop_record = {
                "SOP Name": sop_name,
                "KA ID": ka_id,
                "SP Path": sp_path,
                "Manual Efforts": manual_efforts,
                "Categories": categories,
                "Sub Categories": sub_categories,
            }
            sop_df = sop_df.append(new_sop_record, ignore_index=True)
            st.success("SOP Record added successfully!")