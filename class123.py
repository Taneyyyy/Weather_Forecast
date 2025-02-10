import streamlit as st
import plotly.express as px
from backend import get_data
#title,text input,slider,selectbox and subheader
st.title("Weather Forecast for next days")
place=st.text_input("Place : ")
days=st.slider("Forecast Days", min_value=1,max_value=5,help="select the number of forecast days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")
# get the temperature/sky data
if place:
    try:
        filtered_data=get_data(place,days)
        if(option=="Temperature"):
            temperatures=[dict["main"]["temp"] for dict in filtered_data]
            dates=[dict["dt_txt"]for dict in filtered_data]
            #create a temperature plot
            figure=px.line(x=dates,y=temperatures,labels={"x":"Date","y":"temperature (c)"})
            st.plotly_chart(figure)
        if(option=="Sky"):
            images={"Clear":"images\clear.png","Clouds":"images\cloud.png",
                    "Rain":"images\hrain.png","Snow":"images\snow.png"}
            sky_conditions=[dict["weather"][0]["main"]for dict in filtered_data]
            image_path=[images[condition] for condition in sky_conditions]
            image_label=[dict["dt_txt"]for dict in filtered_data]
            st.image(image_path,width=100,caption=image_label)
    except KeyError:
        st.write("the city does not exist or not found in database used")
