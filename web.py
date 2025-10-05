import requests
import streamlit as st
import requests as reqs
from dotenv import load_dotenv
import os

load_dotenv()   #1) Parse a .env file and then load all the variables found as environment variables
nasa_api_key = os.getenv('NASA_API_KEY')

print(f"NASA API Key: {nasa_api_key}")
url=("https://api.nasa.gov/planetary/apod?api_key="+nasa_api_key)

try:
    response = reqs.get(url).json()
    title = response["title"]
    image_url = response["hdurl"]
    explanation = response["explanation"]

    local_image_url = f"{title}.png"

    with open(local_image_url, "wb") as file:
        file.write(requests.get(image_url).content)

    st.title(title)
    st.image(local_image_url)
    st.write(explanation)


except Exception as e:
    print(f"Exception: {e}")

