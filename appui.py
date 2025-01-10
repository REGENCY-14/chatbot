import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY")

# System prompt
system_prompt = """
You are an AI assistant that is an expert in medical health and is part of a hospital system called medicare AI.
You know about symptoms and signs of various types of illnesses.
You can provide expert advice on self-diagnosis options in the case where an illness can be treated using a home remedy.
If a query requires serious medical attention with a doctor, recommend them to book an appointment with our doctors.
If you are asked a question that is not related to medical health respond with "I'm sorry but your question is beyond my functionalities."
Do not use external URLs or blogs to refer.
Format any lists on individual lines with a dash and a space in front of each line.
"""

# Streamlit UI
st.title("Medical Health Assistant")
st.write(
    "Welcome to the Medical Health Assistant powered by OpenAI. Ask your medical-related questions below."
)

# Input box
user_input = st.text_area("Enter your question:", "")

# Process user input when the button is clicked
if st.button("Get Advice"):
    if user_input.strip():
        try:
            # Call OpenAI API
            with st.spinner("Generating response..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input.strip()},
                    ],
                )
                # Extract and display the response
                reply = response["choices"][0]["message"]["content"].strip()
                st.success("Response:")
                st.write(reply)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before clicking the button.")