import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # Activate the apikey

genai.configure(api_key=os.getenv('google_api_key'))

# Movie Recommender System

# Frontend
st.title('Movie Recommender System') # Main title
user_input = st.text_input('Enter the movie name')
submit = st.button('Submit')
st.balloons() # Balloons ui

model = genai.GenerativeModel(model_name='gemini-1.5-flash-002')

if submit:
    response = model.generate_content(f'Generate Movie Recommendations based on this movie: {user_input}')
    st.write(f'Recommendations:\n {response.text}')
else:
    st.warning('No requests entered')