import streamlit as st
import cv2
import numpy as np
import joblib

hog = cv2.HOGDescriptor()
clf = joblib.load("cattle_vs_buffalo_svm.pkl")
category_names = ["Cow 🐄", "Buffalo 🐃"]  

st.title("Animal Classifier 🐄🐃")

option = st.selectbox("Select one Option: ", ["Upload Image", "Capture Image"])
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
camera_image = st.camera_input("Capture an image")

img = None

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
elif camera_image is not None:
    file_bytes = np.asarray(bytearray(camera_image.getbuffer()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

if img is not None:
    img_resized = cv2.resize(img, (128, 128))
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    features = hog.compute(gray).flatten()
    
    prediction = clf.predict([features])[0]
    st.image(img, channels="BGR", caption="Uploaded Image")
    st.write("Prediction:", category_names[prediction])
