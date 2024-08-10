import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
#import matplotlib.pyplot as plt
#url ='https://raw.githubusercontent.com/AbdullahSoli/Project-3-streamlit/main/cleaned_RiyadhVillasAqar2.csv'
df= pd.read_csv('cleaned_RiyadhVillasAqar.csv')
#df= pd.read_csv(url)
st.write('Hello world!')
st.write('Hello world!gjgjgjg')


st.html(
    "<h1>Abdullah</h1>"
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)


import plotly.graph_objects as go
import streamlit as st

# Assume df2 is your DataFrame and 'duplex' is the column of interest
duplex_counts = df['duplex'].value_counts()

# Create the pie chart with Plotly
fig = go.Figure(data=[go.Pie(labels=duplex_counts.index, values=duplex_counts.values, hole=0.3)])

# Update layout for better appearance
fig.update_layout(
    title_text='Distribution of Duplex Values',
    annotations=[dict(text='Duplex', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

# Display the chart in a Streamlit app
st.plotly_chart(fig)
# Display the chart
#st.plotly_chart(fig)


