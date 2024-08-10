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

import pydeck as pdk
df = pd.DataFrame(data)

# إنشاء الخريطة باستخدام Pydeck
map_deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=df['latitude'].mean(),
        longitude=df['longitude'].mean(),
        zoom=12,  # مستوى تكبير الخريطة
        pitch=0
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[longitude, latitude]',
            get_color='[255, 0, 0, 140]',  # لون النقاط مع الشفافية
            get_radius='value * 10',  # حجم النقاط بناءً على القيمة
            pickable=True,
            auto_highlight=True
        )
    ],
    tooltip={'text': '{location}\nValue: {value}'}  # عرض المعلومات عند المرور فوق النقاط
)

# عرض الخريطة في Streamlit
st.pydeck_chart(map_deck)
