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
st.html(
    "<h1>السؤال الثالث ؟ </h1>"
    "<p>شرح</p>"
)
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
st.altair_chart(chart, use_container_width=True)


avg_price_5_rooms = df[df['rooms'] == 5].groupby('location')['price'].mean().reset_index()
avg_price_5_rooms.columns = ['location', 'average_price']
bar_chart = alt.Chart(avg_price_5_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location', sort='-y'),
    y=alt.Y('average_price:Q', title='Average Price'),
    tooltip=['location:N', 'average_price:Q']  
).properties(
    title='Average Price for 5 Room Objects by Location',
    width=800,
    height=400
)
st.altair_chart(bar_chart, use_container_width=True)


avg_price_4_rooms = df[df['rooms'] == 4].groupby('location')['price'].mean().reset_index()
avg_price_4_rooms.columns = ['location', 'average_price']
bar_chart = alt.Chart(avg_price_4_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location', sort='-y'),
    y=alt.Y('average_price:Q', title='Average Price'),
    tooltip=['location:N', 'average_price:Q']  
).properties(
    title='Average Price for 4 Room Objects by Location',
    width=800,
    height=400
)
st.altair_chart(bar_chart, use_container_width=True)


st.html(
    "<h1>السؤال الرابع ؟ </h1>"
    "<p>شرح</p>"
)
duplex_counts = df['duplex'].value_counts().reset_index()
duplex_counts.columns = ['duplex', 'count']
pie_chart = alt.Chart(duplex_counts).mark_arc().encode(
    theta=alt.Theta(field='count', type='quantitative', title='Count'),
    color=alt.Color(field='duplex', type='nominal', title='Duplex'),
    tooltip=['duplex:N', 'count:Q']  
).properties(
    title='Distribution of Duplex Values',
    width=400,
    height=400
).configure_arc(
    outerRadius=150
)
st.altair_chart(pie_chart, use_container_width=True)
