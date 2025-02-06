from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_api_key"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="LLM using Gemini-1.5-Flash")
st.header(" Your personal Q&A, Text geneartor, Code Geneartor Assistant")
input=st.text_input("input: ",key="input")
submit=st.button("Submit")


if submit:
    response=get_response(input)
    st.subheader("Response")
    st.write(response)