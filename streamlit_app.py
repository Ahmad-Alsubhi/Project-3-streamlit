import streamlit as st

st.write('Hello world!')
st.write('Hello world!gjgjgjg')


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from ipyvizzu import Chart, Data, Config

## This statement allows the visuals to render within your Jupyter Notebook.
df2 = pd.read_csv("RiyadhVillasAqar.csv")
profile_df2 = ProfileReport(df2, title="Profiling Report")
profile_df2
del df2['Unnamed: 0']
df2['lounges'] = df2['lounges'].fillna(0) #dealing with null in lounges
df2['streetWidth'] = df2['streetWidth'].fillna(0) #dealing with null in streetWidth
df2['price'] = df2['price'].fillna(0)   #dealing with null in price and price square 
df2['square price'] = df2['square price'].fillna(0)
df2['lounges'] = (df2['lounges'].astype(str).str.extract(r'(\d+)').astype(float).astype(int))
df2['bathrooms'] = (df2['bathrooms'].astype(str).str.extract(r'(\d+)').astype(float).astype(int))
df2['apartments'] = (df2['apartments'].astype(str).str.extract(r'(\d+)').astype(float).astype(int))
df2['apartments'] = df2['apartments'].astype('i')
df2['lounges'] = df2['lounges'].astype(int)
df2['bathrooms'] = df2['bathrooms'].astype(int)



# Sample data


# Create a pie chart using ipyvizzu
chart = Chart()
chart.add_data(df2)
chart.set_chart_type('pie')
chart.set_labels('Labels')
chart.set_values('Sizes')
chart.set_title('Maid Room and Driver Room')

# Display the chart using Streamlit
st.title('Interactive Pie Chart')
st.write('This is an interactive pie chart created with ipyvizzu and Streamlit.')
st.write(chart.to_html())  # Convert the chart to HTML for Streamlit



