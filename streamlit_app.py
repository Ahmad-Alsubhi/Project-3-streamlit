import streamlit as st
import pandas as pd
df= pd.read_csv('cleaned_RiyadhVillasAqar.csv')
st.write('Hello world!')
st.write('Hello world!gjgjgjg')


st.html(
    "<h1>Abdullah</h1>"
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['location', 'price'])

st.map(df)


