import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value=1,max_value=5,
                 help = "Select the number of forecasted days")
option = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
dates = ["10-04-2023", "11-04-2023", "12-04-2023"]
temperature = ["32", "35", "40"]

figure = px.line(x=dates,y=temperature,labels={"x":"Date", "y":"Temperature"})
st.plotly_chart(figure)