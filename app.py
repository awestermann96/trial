import streamlit as st
import plotly.express as px

st.title('This is an app')
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()
