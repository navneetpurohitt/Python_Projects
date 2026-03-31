Step-by-Step Plan to Build the Streamlit Application
Based on your requirements, I'll outline a comprehensive plan to build a multi-screen Streamlit application with database integration.

Phase 1: Planning and Database Design
1. Database Schema Design
Create SQL tables for each of your entities:

Book of Work

SOP Details

SOP Analysis

Development Tasks

Maintenance Tasks

Resources

etc.

2. Set Up Project Structure
text
project/
├── app.py
├── database.py
├── pages/
│   ├── book_of_work.py
│   ├── sop_details.py
│   ├── sop_analysis.py
│   └── ...
├── requirements.txt
└── utils.py
Phase 2: Environment Setup
3. Install Required Packages
Create a requirements.txt file:

txt
streamlit
sqlalchemy
pandas
plotly
streamlit-option-menu
Install dependencies:

bash
pip install -r requirements.txt
Phase 3: Database Implementation
4. Create Database Models (database.py)
python
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class BookOfWork(Base):
    __tablename__ = 'book_of_work'
    id = Column(Integer, primary_key=True)
    category = Column(String)
    subcategory = Column(String)
    business_unit = Column(String)
    portfolio = Column(String)
    gear_id = Column(String)
    sdn_name = Column(String)
    sme_name = Column(String)

class SOPDetails(Base):
    __tablename__ = 'sop_details'
    id = Column(Integer, primary_key=True)
    sop_name = Column(String)
    ka_id = Column(String)
    sp_path = Column(String)
    manual_effort = Column(Integer)
    category = Column(String)
    subcategory = Column(String)

# Add more models for other entities...

# Create engine and session
engine = create_engine('sqlite:///sop_automation.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
Phase 4: Streamlit Application Development
5. Create Main Application (app.py)
python
import streamlit as st
from streamlit_option_menu import option_menu
from database import Session, BookOfWork, SOPDetails  # Import your models
import pages.book_of_work as book_of_work
import pages.sop_details as sop_details
# Import other pages...

# Configure page
st.set_page_config(
    page_title="SOP Automation Platform",
    page_icon="📊",
    layout="wide"
)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Book of Work'

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Book of Work", "SOP Details", "SOP Analysis", "Development Task", 
         "Maintenance Task", "Task Status", "Analytics", "Task Assignment",
         "Resource Details"],
        icons=['book', 'file-text', 'graph-up', 'code', 'tools', 
               'clipboard-check', 'bar-chart', 'person-plus', 'people'],
        menu_icon="cast",
        default_index=0,
    )
    st.session_state.current_page = selected

# Display the selected page
if st.session_state.current_page == "Book of Work":
    book_of_work.show()
elif st.session_state.current_page == "SOP Details":
    sop_details.show()
# Add more elif statements for other pages...
6. Create Individual Page Modules (pages/book_of_work.py)
python
import streamlit as st
from database import Session, BookOfWork

def show():
    st.title("Book of Work")
    
    # Create form for new entry
    with st.form("book_of_work_form"):
        col1, col2 = st.columns(2)
        with col1:
            category = st.text_input("Category")
            business_unit = st.text_input("Business Unit")
            gear_id = st.text_input("Gear ID")
        with col2:
            subcategory = st.text_input("Subcategory")
            portfolio = st.text_input("Portfolio")
            sdn_name = st.text_input("SDN Name")
            sme_name = st.text_input("SME Name")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            session = Session()
            new_entry = BookOfWork(
                category=category,
                subcategory=subcategory,
                business_unit=business_unit,
                portfolio=portfolio,
                gear_id=gear_id,
                sdn_name=sdn_name,
                sme_name=sme_name
            )
            session.add(new_entry)
            session.commit()
            session.close()
            st.success("Entry added successfully!")
    
    # Display existing data
    st.subheader("Existing Entries")
    session = Session()
    entries = session.query(BookOfWork).all()
    session.close()
    
    if entries:
        # Convert to DataFrame for nice display
        import pandas as pd
        data = []
        for entry in entries:
            data.append({
                "Category": entry.category,
                "Subcategory": entry.subcategory,
                "Business Unit": entry.business_unit,
                "Portfolio": entry.portfolio,
                "Gear ID": entry.gear_id,
                "SDN Name": entry.sdn_name,
                "SME Name": entry.sme_name
            })
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No entries found.")
7. Create Similar Modules for Other Pages
Repeat the pattern for:

SOP Details

SOP Analysis

Development Task

Maintenance Task

etc.

Phase 5: Advanced Features
8. Add Analytics Page (pages/analytics.py)
python
import streamlit as st
import plotly.express as px
from database import Session, SOPDetails

def show():
    st.title("Analytics")
    
    session = Session()
    # Query data for visualization
    sop_data = session.query(SOPDetails).all()
    session.close()
    
    if sop_data:
        # Create a DataFrame
        import pandas as pd
        data = []
        for sop in sop_data:
            data.append({
                "SOP Name": sop.sop_name,
                "Manual Effort": sop.manual_effort,
                "Category": sop.category
            })
        df = pd.DataFrame(data)
        
        # Create visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            effort_by_category = df.groupby('Category')['Manual Effort'].sum().reset_index()
            fig = px.bar(effort_by_category, x='Category', y='Manual Effort', 
                         title="Manual Effort by Category")
            st.plotly_chart(fig)
        
        with col2:
            fig = px.pie(df, names='Category', title="SOP Distribution by Category")
            st.plotly_chart(fig)
    else:
        st.info("No data available for analytics.")
Phase 6: Deployment
9. Test the Application
bash
streamlit run app.py
10. Deploy the Application
Options for deployment:

Streamlit Sharing

Heroku

AWS/Azure/GCP

Docker containerization

Additional Considerations
Authentication: Add user authentication if needed

Data Validation: Implement input validation

Error Handling: Add proper error handling

Export Functionality: Add data export options

Notifications: Implement alerts for important events

This plan provides a comprehensive roadmap to build your multi-screen Streamlit application with database integration. Each step builds upon the previous one, creating a fully functional application.