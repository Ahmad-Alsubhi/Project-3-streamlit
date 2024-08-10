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

st.html(
    "<h1>الفلل في الرياض </h1>"
    "<p><span style='text-decoration: line-through double red;'>مقدمة</span>!</p>"
)

st.image("riyadh.jpg", caption="Riyadh",width=1000)

st.html(
    "<h1>الفلل في الرياض </h1>"
    "<p>مقدمة</p>"
)
st.html(
    "<h1>السؤال الاول ؟ </h1>"
    "<p>شرح</p>"
)
data = pd.DataFrame({
    'labels': ['Maid Room', 'Driver Room'],
    'sizes': [df['maidRoom'].sum(), df['driverRoom'].sum()]
})

st.html(
    "<h1>السؤال الثاني ؟ </h1>"
    "<p>شرح</p>"
)
chart = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field='sizes', type='quantitative'),
    color=alt.Color(field='labels', type='nominal'),
    tooltip=[alt.Tooltip(field='labels', type='nominal'), alt.Tooltip(field='sizes', type='quantitative')]
).properties(
    title='Maid Room and Driver Room'
)


st.altair_chart(chart, use_container_width=True)
