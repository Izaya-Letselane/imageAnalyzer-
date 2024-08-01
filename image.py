import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

GOOGLE_API_KEY = "AIzaSyBikV0v1ltCUIsVoLProMqJgx88fXNr6T0"
os.environ["GOOGLE_API_KEY"] = "AIzaSyBikV0v1ltCUIsVoLProMqJgx88fXNr6T0"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# fUNCTION TO GEMINI PRO MODEL ANG GET RESPONSES
model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(input, image):
    if input!= "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


# initialize streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("Gemini Image Identificatfication Application")
input = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# When submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)

