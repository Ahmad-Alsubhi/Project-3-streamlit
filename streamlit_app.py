import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
df= pd.read_csv('cleaned_RiyadhVillasAqar.csv')
st.write('Hello world!')
st.write('Hello world!gjgjgjg')


st.html(
    "<h1>Abdullah</h1>"
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)


duplex_counts = df['duplex'].value_counts()

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(duplex_counts, labels=['Duplex', 'not Duplex'], autopct='%1.1f%%')
ax.set_title('Distribution of Duplex Values')
ax.axis('equal')  # Equal aspect ratio ensures that pie is circular.

# Display the chart
plt.show()


