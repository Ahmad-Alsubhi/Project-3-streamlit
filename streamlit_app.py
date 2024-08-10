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
    "<p>مقدمة</p>"
)

st.image("riyadh2.jpg", caption="Riyadh",width=1000)


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

avg_price_rooms = df.groupby('location')['price'].mean().reset_index()

# Create the Altair bar chart
chart = alt.Chart(avg_price_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location'),
    y=alt.Y('price:Q', title='Average Price'),
    tooltip=['location:N', 'price:Q']
).properties(
    title='Average Price of Room Objects by Location'
).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)


map_chart = alt.Chart(df).mark_circle(size=100).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='price:Q',
    tooltip=['location:N', 'price:Q']
).properties(
    title='Distribution of Room Prices by Location'
).configure_view(
    stroke=None
)

# Display the map in Streamlit
st.altair_chart(map_chart, use_container_width=True)
