# **Face Mask Detection – OpenCV + Scikit-Learn**

This project is a simple **Face Mask Detection System** built using **OpenCV (cv2)** and **scikit-learn (SVM)**.
It detects whether a person is **wearing a mask or not** in real-time using a webcam.

The model is trained using your custom dataset stored in the `Dataset/` folder, which contains two categories:

* **with_mask**
* **without_mask**

---

## **📁 Project Structure**

```
Dataset/
   ├── with_mask/
   └── without_mask/

train_mask_model.py   → trains the SVM model  
mask_detect.py        → runs real-time mask detection  
mask_model.pkl        → trained classifier  
README.md             → project documentation
```

---

## **🧠 How It Works**

1. Images are loaded using **cv2**
2. All images are resized and converted to grayscale
3. Images are flattened into feature vectors
4. A **Support Vector Classifier (SVC)** is trained
5. Haarcascade is used to detect faces in real-time
6. For each detected face, the model predicts:

   * **With Mask**
   * **No Mask**

---

## **🔧 Technologies Used**

* **Python**
* **OpenCV (cv2)**
* **scikit-learn (SVM)**
* **joblib** (for saving model)
* **Haarcascade frontal face detector**

---

## **🚀 How to Run**

### **1. Train the Model**

* Place your dataset inside the `Dataset/` folder
* Run:

```
python train_mask_model.py
```

This will create `mask_model.pkl`.

---

### **2. Detect Masks in Real-Time**

Run:

```
python mask_detect.py
```

Your webcam will open and start predicting **Mask / No Mask**.

---

## **📊 Output Example**

Below is an example output from the real-time mask detector:

![Mask Detection Output](Screenshot%202025-11-13%20064815.png)

---
