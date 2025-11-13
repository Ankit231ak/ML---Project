# **Animal Classifier**

This project is a simple **Streamlit-based Animal Classifier** that identifies whether an image contains a **Cow** or a **Buffalo**.
The model is powered by **OpenCV HOG features** and an **SVM classifier** trained on a custom dataset.

---

## **🚀 Features**

* Upload an image for classification
* Capture a live image using your webcam
* Real-time prediction
* Lightweight and easy to run
* Works offline after setup

---

## **📁 Project Files**

```
c.py                      → Streamlit app  
cattle_vs_buffalo_svm.pkl → Trained SVM model  
Dataset/                  → Training images (not included here)
README.md                 → Documentation
```

---

## **🧠 How It Works**

1. The image is loaded (uploaded or captured).
2. Converted to grayscale and resized.
3. HOG (Histogram of Oriented Gradients) features are extracted.
4. The SVM model predicts whether it's a **cow** or **buffalo**.
5. Prediction is displayed along with the image.

---

## **▶️ How to Run**

1. Install required packages:

```
pip install streamlit opencv-python numpy joblib
```

2. Run the app:

```
streamlit run c.py
```

3. A browser window will open automatically.

---

## **📸 Output Preview**

Below is an example of how the application looks when running:

![App Screenshot](Screenshot%20\(238\).png)

