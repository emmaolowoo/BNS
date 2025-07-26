import numpy as np 
import pandas as pd 
import streamlit as st 
import altair as alt


def load_data():
    data = pd.read_csv("Electronic_sales_Sep2023-Sep2024.csv")
    data["Purchase Date"] = pd.to_datetime(data["Purchase Date"], format="mixed")
    data.loc[:,"Year"] = data["Purchase Date"].dt.year
    data.loc[:,"Month"] = data["Purchase Date"].dt.month

    return data

try:
    df = load_data()
    st.write("# Electronics Sales App")
# first 5 rows of the data
    st.dataframe(df.head())

#filter_df = df.filter("")

#multiselct for the products
# products = df['Product Type'].unique()

    st.write("## Sales by Products")
    prd_sales = df.groupby('Product Type')["Total Price"].sum().reset_index()
    prd_sales.columns = ["Product Type","Total Sales"]

    st.dataframe(prd_sales)

    st.write("## Sales by Products Chart")
    bar1 = alt.Chart(prd_sales).mark_bar().encode(
        x='Product Type',
        y='Total Sales'
    )
    st.altair_chart(bar1)

    st.write("### Purchase Date by Total Sales - Line chart")
    date_grp = df.groupby(["Purchase Date"])["Total Price"].sum().reset_index()
    date_grp.columns = ["Purchase Date", "Total Sales"]
    
    line1 = alt.Chart(date_grp).mark_line().encode(
        x='Purchase Date',
        y='Total Sales'
    )   

    st.altair_chart(line1)
except:
    pass