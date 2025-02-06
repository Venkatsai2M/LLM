from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=st.secrets["Google_api_key"])

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(question):
    response = model.generate_content(question)
    return response.text

# Page configuration
st.set_page_config(page_title="Q&A BOT", page_icon="🤖", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #4A90E2;
        }
        .input-box {
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            width: 100%;
        }
        .submit-button {
            background-color: #4A90E2;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }
        .response-box {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main UI
st.markdown("<h1 class='main-title'>Your AI Assistant 🤖</h1>", unsafe_allow_html=True)

st.write("Ask me anything! I can help with Q&A, text generation, and code generation.")

# Input section
input_text = st.text_input("Enter your query:", key="input")

# Button with better styling
if st.button("Submit", key="submit", help="Click to generate a response"):
    if input_text.strip():
        response = get_response(input_text)
        st.subheader("Response")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a valid query.")
