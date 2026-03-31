import matplotlib.pyplot as plt

# Sales Data Analysis Dashboard
# This script provides an interactive dashboard for analyzing sales data using Streamlit. 
# Users can upload a CSV file containing sales data, apply filters, and visualize various 
# aspects of the data through charts and metrics.
# Features:
# - Upload sales data in CSV format.
# - Apply filters based on date range, product category, and region.
# - Display key metrics such as total sales, total quantity sold, and total orders.
# - Visualize sales trends over time, sales by product line, top customers, sales by country, 
#     sales by year, and sales by month using various charts.
# - Export filtered data as a CSV file.
# Libraries Used:
# - matplotlib.pyplot: For creating plots.
# - seaborn: For advanced data visualization.
# - pandas: For data manipulation and analysis.
# - streamlit: For building the interactive dashboard.
# - numpy: For numerical operations.
# Columns in the Sales Data:
# - ORDERNUMBER, QUANTITYORDERED, PRICEEACH, ORDERLINENUMBER, SALES, ORDERDATE, STATUS, 
#     QTR_ID, MONTH_ID, YEAR_ID, PRODUCTLINE, MSRP, PRODUCTCODE, CUSTOMERNAME, PHONE, 
#     ADDRESSLINE1, ADDRESSLINE2, CITY, STATE, POSTALCODE, COUNTRY, TERRITORY, 
#     CONTACTLASTNAME, CONTACTFIRSTNAME, DEALSIZE.
# Usage:
# 1. Run the script in a Streamlit environment.
# 2. Upload a CSV file containing sales data.
# 3. Apply filters using the sidebar.
# 4. View metrics and charts in the main dashboard.
# 5. Export filtered data as a CSV file if needed.
# Note:
# Ensure the uploaded CSV file is encoded in 'latin1' and contains the required columns.
# """
# """
# Sales Data Analysis Dashboard
# This script provides an interactive dashboard for analyzing sales data using Streamlit. 
# Users can upload a CSV file containing sales data, apply filters, and visualize various 
# aspects of the data through charts and metrics.
# Features:
# - Upload sales data in CSV format.
# - Apply filters based on date range, product category, and region.
# - Display key metrics such as total sales, total quantity sold, and total orders.
# - Visualize sales trends over time, sales by product line, top customers, sales by country, 
#     sales by year, and sales by month using various charts.
# - Export filtered data as a CSV file.
# Libraries Used:
# - matplotlib.pyplot: For creating plots.
# - seaborn: For advanced data visualization.
# - pandas: For data manipulation and analysis.
# - streamlit: For building the interactive dashboard.
# - numpy: For numerical operations.
# Columns in the Sales Data:
# - ORDERNUMBER, QUANTITYORDERED, PRICEEACH, ORDERLINENUMBER, SALES, ORDERDATE, STATUS, 
#     QTR_ID, MONTH_ID, YEAR_ID, PRODUCTLINE, MSRP, PRODUCTCODE, CUSTOMERNAME, PHONE, 
#     ADDRESSLINE1, ADDRESSLINE2, CITY, STATE, POSTALCODE, COUNTRY, TERRITORY, 
#     CONTACTLASTNAME, CONTACTFIRSTNAME, DEALSIZE.
# Usage:
# 1. Run the script in a Streamlit environment.
# 2. Upload a CSV file containing sales data.
# 3. Apply filters using the sidebar.
# 4. View metrics and charts in the main dashboard.
# 5. Export filtered data as a CSV file if needed.
# Note:
# Ensure the uploaded CSV file is encoded in 'latin1' and contains the required columns.
# """
import seaborn as sns
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="Sales Data Analysis", layout="wide")
st.header("Sales Data Analysis Dashboard")
sales_data_path = st.file_uploader("Upload Sales Data CSV", type=["csv"])
# sales_data_path = './sales_data_sample.csv'
sales_data = pd.DataFrame()
if sales_data_path:
    # Load the sales data from the uploaded CSV file
    sales_data = pd.read_csv(sales_data_path, encoding='latin1')
    st.success("Data loaded successfully!")
   
    st.sidebar.header("Filters")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2003-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2005-12-31"))
    product_category = st.sidebar.multiselect("Product Category", options=sales_data['PRODUCTLINE'].unique(), default=sales_data['PRODUCTLINE'].unique())
    region = st.sidebar.multiselect("Region", options=sales_data['COUNTRY'].unique(), default=sales_data['COUNTRY'].unique())

    # Apply filters
    sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce')
    filtered_data = sales_data[
        (sales_data['ORDERDATE'] >= pd.to_datetime(start_date)) &
        (sales_data['ORDERDATE'] <= pd.to_datetime(end_date)) &
        (sales_data['PRODUCTLINE'].isin(product_category)) &
        (sales_data['COUNTRY'].isin(region))
    ]
    if not sales_data.empty:
        if sales_data is not None:
            sales_data = filtered_data
            column1, column2, column3 = st.columns([1,1,1])
            total_sales = sales_data['SALES'].sum()
            total_orders = sales_data['ORDERNUMBER'].nunique()
            total_quantity = sales_data['QUANTITYORDERED'].sum()
            with column1:
                st.subheader("Total Sales")
            
                st.metric(label="Total Sales", value=f"${total_sales:,.2f}")

            with column2:
                st.subheader("Total Quantity Sold")
                st.metric(label="Total Quantity Sold", value=f"{total_quantity:,}")
            with column3:
                st.subheader("Total Orders")
            
                st.metric(label="Total Orders", value=f"{total_orders:,}")
            

            st.subheader("Sales Over Time")
            st.write(sales_data)
            # Arrange all graphs in a horizontal sequence
            graph1, graph2 = st.columns(2)
            graph3, graph4 = st.columns(2)
            graph5, graph6  = st.columns(2)
            with graph1:
                sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce')
               
                sales_over_time = sales_data.groupby('ORDERDATE')['SALES'].sum().reset_index()
                sales_over_time = sales_over_time.dropna(subset=['ORDERDATE'])  # Remove rows with NaT values
                fig, ax = plt.subplots()
                sns.lineplot(data=sales_over_time, x='ORDERDATE', y='SALES', ax=ax)
                ax.set_title("Sales Over Time")
                ax.set_xlabel("Order Date")
                ax.set_ylabel("Sales")
                st.pyplot(fig)

            # Pie Chart: Sales by Product Line
            with graph2:
                sales_by_product_line = sales_data.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
                sales_by_product_line['Percentage'] = (sales_by_product_line['SALES'] / total_sales) * 100
                fig, ax = plt.subplots()
                sns.barplot(x='PRODUCTLINE', y='SALES', data=sales_by_product_line, ax=ax)
                ax.set_title("Sales by Product Line")
                ax.set_xlabel("Product Line")
                ax.set_ylabel("Sales")
                st.pyplot(fig)

            # Bar Chart: Top 10 Customers by Sales
            with graph3:
                top_customers = sales_data.groupby('CUSTOMERNAME')['SALES'].sum().reset_index()
                top_customers = top_customers.sort_values(by='SALES', ascending=False).head(10)
                fig, ax = plt.subplots()
                sns.barplot(x='SALES', y='CUSTOMERNAME', data=top_customers, ax=ax)
                ax.set_title("Top 10 Customers by Sales")
                ax.set_xlabel("Sales")
                ax.set_ylabel("Customer Name")
                st.pyplot(fig)

            # Bar Chart: Sales by Country
            with graph4:
                sales_by_country = sales_data.groupby('COUNTRY')['SALES'].sum().reset_index()
                sales_by_country = sales_by_country.sort_values(by='SALES', ascending=False)
                fig, ax = plt.subplots()
                sns.barplot(x='SALES', y='COUNTRY', data=sales_by_country, ax=ax)
                ax.set_title("Sales by Country")
                ax.set_xlabel("Sales")
                ax.set_ylabel("Country")
                st.pyplot(fig)

            # Bar Chart: Sales by Year
            with graph5:
                sales_data['YEAR_ID'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce').dt.year
                sales_by_year = sales_data.groupby('YEAR_ID')['SALES'].sum().reset_index()
                sales_by_year = sales_by_year.sort_values(by='YEAR_ID')
                fig, ax = plt.subplots()
                sns.barplot(x='YEAR_ID', y='SALES', data=sales_by_year, ax=ax)
                ax.set_title("Sales by Year")
                ax.set_xlabel("Year")
                ax.set_ylabel("Sales")
                st.pyplot(fig)

            # Bar Chart: Sales by Month
            with graph6:
                sales_data['MONTH_ID'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce').dt.month
                sales_by_month = sales_data.groupby('MONTH_ID')['SALES'].sum().reset_index()
                sales_by_month = sales_by_month.sort_values(by='MONTH_ID')
                fig, ax = plt.subplots()
                sns.barplot(x='MONTH_ID', y='SALES', data=sales_by_month, ax=ax)
                ax.set_title("Sales by Month")
                ax.set_xlabel("Month")
                ax.set_ylabel("Sales")
                st.pyplot(fig)
            graph7, graph8 = st.columns(2)
            # Bar Chart: Sales by Territory
            with graph7:
                sales_by_territory = sales_data.groupby('TERRITORY')['SALES'].sum().reset_index()
                sales_by_territory = sales_by_territory.sort_values(by='SALES', ascending=False)
                fig, ax = plt.subplots()
                sns.barplot(x='SALES', y='TERRITORY', data=sales_by_territory, ax=ax)
                ax.set_title("Sales by Territory")
                ax.set_xlabel("Sales")
                ax.set_ylabel("Territory")
                st.pyplot(fig)
            # Bar Chart: Sales by Deal Size
            with graph8:
                sales_by_dealsize = sales_data.groupby('DEALSIZE')['SALES'].sum().reset_index()
                sales_by_dealsize = sales_by_dealsize.sort_values(by='SALES', ascending=False)
                fig, ax = plt.subplots()
                sns.barplot(x='SALES', y='DEALSIZE', data=sales_by_dealsize, ax=ax)
                ax.set_title("Sales by Deal Size")
                ax.set_xlabel("Sales")
                ax.set_ylabel("Deal Size")
                st.pyplot(fig)
            graph9, graph10 = st.columns(2)
            # Histogram: Distribution of Sales
            with graph9:
                fig, ax = plt.subplots()
                sns.histplot(sales_data['SALES'], bins=30, kde=True, ax=ax)
                ax.set_title("Distribution of Sales")
                ax.set_xlabel("Sales")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
            # scatter plot: Sales vs Quantity Ordered  
            with graph10:
                fig, ax = plt.subplots()
                sns.scatterplot(data=sales_data, x='QUANTITYORDERED', y='SALES', ax=ax)
                ax.set_title("Sales vs Quantity Ordered")
                ax.set_xlabel("Quantity Ordered")
                ax.set_ylabel("Sales")
                st.pyplot(fig)
            graph11, graph12 = st.columns(2)
            # graph for items shipped
            with graph11:
                items_shipped = sales_data[sales_data['STATUS'] == 'Shipped'].groupby('ORDERDATE')['SALES'].sum().reset_index()
                items_shipped = items_shipped.dropna(subset=['ORDERDATE'])
                fig, ax = plt.subplots()
                sns.lineplot(data=items_shipped, x='ORDERDATE', y='SALES', ax=ax)
                ax.set_title("Items Shipped Over Time")
                ax.set_xlabel("Order Date")
                ax.set_ylabel("Sales")
                st.pyplot(fig)

        
        # Export filtered data as CSV
        st.subheader("Export Filtered Data")
        export_button = st.button("Export Filtered Data as CSV")
        if export_button:
            st.download_button(
                label="Download Filtered Data as CSV",
                data=filtered_data.to_csv(index=False).encode('utf-8'),
                file_name='filtered_sales_data.csv',
                mime='text/csv'
            )
            st.success("Filtered data exported successfully as 'filtered_sales_data.csv'.")