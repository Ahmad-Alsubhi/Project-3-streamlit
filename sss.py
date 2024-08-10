# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title of the app
st.title('My Streamlit App')

# Subheader
st.subheader('This is a subheader')

# Text
st.write('This is a simple Streamlit app template with an interactive chart.')

# Adding an interactive widget: Slider
slider_value = st.slider('Select a value', 0, 100, 50)
st.write(f'The selected value is {slider_value}')

# Adding an interactive widget: Button
if st.button('Click me'):
    st.write('Button clicked!')

# Adding a DataFrame
data = {
    'Column A': np.random.randn(10),
    'Column B': np.random.randn(10)
}
df = pd.DataFrame(data)
st.write('Here is a DataFrame:', df)

# Adding a line chart with Streamlit
st.line_chart(df)

# Adding an interactive Plotly chart
fig = px.line(df, x=df.index, y=['Column A', 'Column B'], title='Interactive Line Chart')
st.plotly_chart(fig)

# Adding a file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write('File uploaded:', uploaded_file.name)
    uploaded_df = pd.read_csv(uploaded_file)
    st.write('Uploaded DataFrame:', uploaded_df)

# Sidebar with interactive widget
st.sidebar.header('Sidebar')
sidebar_option = st.sidebar.selectbox('Choose an option', ['Option 1', 'Option 2'])
st.sidebar.write(f'Selected option: {sidebar_option}')
