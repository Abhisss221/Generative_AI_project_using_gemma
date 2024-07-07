from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("app.py")) # as soon as our application will be initialized our api ki will be loaded
## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    
    response = model.generate_content(question)
    return response.text
##initialize our streamlit app

st.set_page_config(page_title=" chat bot")

st.header("Agile phase_1  : Ask me anything  ")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")
## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
