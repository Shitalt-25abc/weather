import streamlit as st
import requests 
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('WEATHER_AI_KEY')

st.set_page_config(page_title= 'weather ', page_icon= "⛅" )
st.title("Weather Budyyy ⛅")
st.write('Enter the city name and click on the button to fetch weather')
city=st.text_input('enter the city name')
if(st.button('fetch weather data')):
    API_URL=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    resonce=requests.get(API_URL)
    print(resonce.json())
    if(resonce.status_code==200):
        st.success('Weather data fetched successfully')
        data=resonce.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        country = data['sys']['country']
        condition= data['weather'][0]['main']
        name = data['name']
        st.header(f'{name},{country}')
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)

        col1.metric('temperature',f'{temperature} °C 🔥')
        col2.metric('humidity',f'{humidity} %💧')
        col3.metric('country',f'{country}🥇')
        col4.metric('condition',f'{condition}⛅')
    else:
        st.error('invalid city')
