<<<<<<< HEAD
# 🤟 Sign Language Recognition

Deep Learning project for recognizing sign language alphabet letters using CNN.

---

# 📌 Project Description

This project uses Deep Learning and Computer Vision to classify hand signs representing alphabet letters.

The model is trained on the Sign Language MNIST dataset.

---

# 📂 Dataset

Dataset used:

- Sign Language MNIST

Files:

- sign_mnist_train.csv
- sign_mnist_test.csv

---

# 🧠 Architectures Tested

## 1. CNN Baseline
Simple convolutional neural network.

## 2. CNN + Dropout
Added dropout for regularization.

## 3. ResNet18
Transfer learning using pretrained ResNet.

## 4. LSTM
Sequence-based model for comparison.

---

# 📈 Results

| Model | Validation Accuracy |
|---|---|
| CNN | 89% |
| ResNet18 | 96% |
| LSTM | 72% |

---

# 📊 Evaluations

- Accuracy
- Confusion Matrix
- Classification Report
- Learning Curves

---

# 🚀 Streamlit Application

The project includes a Streamlit app for online inference.

Users can upload an image and predict the sign letter.

---

# ▶️ Run Project

Install requirements:

```bash
pip install -r requirements.txt

