import io
import json
import requests
import streamlit as st
from io import BytesIO
from PIL import Image

image = Image.open("webapp/logo.jpeg")
st.image(image, width=200)
st.markdown("AWS User Group Madurai")

st.header(f"Serverless AI Demo")
st.markdown("The Clip Crop Serverless AI Demo is an interactive application that combines the cutting-edge technology of serverless computing with the advanced image and text understanding of the CLIP model.")

api_url = st.text_input("Enter api url", placeholder="Enter api url..",)
image_url = st.text_input("Enter image url", placeholder="Enter image url..",)
search_query = st.text_input("Enter search query", placeholder="Enter your search query..")

with st.spinner("Running inference..."):
    if api_url and image_url and search_query:

        img_bytes = requests.get(image_url).content
        img = Image.open(BytesIO(img_bytes))

        # display the image
        st.image(img, caption="Input Image", use_column_width=True)

        payload = {"img_url":image_url,
                    "search_query":search_query}

        response = requests.post(api_url, data = json.dumps(payload))

        if response.status_code == 200:
            bbox = response.json()['bbox']

            img_bytes = requests.get(payload['img_url']).content
            img = Image.open(io.BytesIO(img_bytes))

            crop = img.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
            st.image(crop, caption="Cropped Image")
            st.success("Success")   
        else:
            print(response.status_code)
            st.error("Error")



