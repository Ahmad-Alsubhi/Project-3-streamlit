import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
#import plotly.figure_factory as ff
#import matplotlib.pyplot as plt
url ='https://raw.githubusercontent.com/AbdullahSoli/Project-3-streamlit/main/cleaned_RiyadhVillasAqar2.csv'
#df= pd.read_csv('cleaned_RiyadhVillasAqar.csv')
df= pd.read_csv(url)
st.write('Hello world!')
st.write('Hello world!gjgjgjg')

st.image("riyadh.jpg", caption="Riyadh",width=40, height=30)
st.html(
    "<h1>Abdullah</h1>"
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

data = pd.DataFrame({
    'labels': ['A', 'B', 'C', 'D'],
    'sizes': [15, 30, 45, 10]
})

# Create an Altair pie chart
chart = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field='sizes', type='quantitative'),
    color=alt.Color(field='labels', type='nominal')
).properties(title='Pie Chart Example')

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

data = pd.DataFrame({
    'labels': ['Maid Room', 'Driver Room'],
    'sizes': [df['maidRoom'].sum(), df['driverRoom'].sum()]
})

# إنشاء مخطط دائري باستخدام Altair
chart = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field='sizes', type='quantitative'),
    color=alt.Color(field='labels', type='nominal'),
    tooltip=[alt.Tooltip(field='labels', type='nominal'), alt.Tooltip(field='sizes', type='quantitative')]
).properties(
    title='Maid Room and Driver Room'
)

# عرض المخطط في Streamlit
st.altair_chart(chart, use_container_width=True)
