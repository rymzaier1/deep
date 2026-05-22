# 🤟 Sign Language Recognition

A deep learning application that recognizes American Sign Language (ASL) hand signs from images using a Convolutional Neural Network (CNN), with an interactive web interface built with Streamlit.

---

## 📌 Project Overview

This project trains a CNN model to classify hand sign images into one of **25 ASL alphabet letters** (A–Y, excluding J which requires motion). The trained model is then deployed via a simple web application where users can upload an image and get an instant prediction.

---

## 🗂️ Project Structure

```
├── final_notebook.ipynb   # Training notebook (data loading, model training, evaluation)
├── model_final.pth        # Trained PyTorch model weights
├── app.py                 # Streamlit web application
└── README.md
```

---

## 🧠 Model Architecture

The model (`CNNBaseline`) is a custom CNN built with PyTorch:

| Layer | Details |
|---|---|
| Conv2D (1 → 32) | kernel 3×3, padding 1 |
| ReLU + MaxPool2d | stride 2 |
| Conv2D (32 → 64) | kernel 3×3, padding 1 |
| ReLU + MaxPool2d | stride 2 |
| Flatten | — |
| Linear (3136 → 128) | ReLU + Dropout (0.5) |
| Linear (128 → 25) | Output (25 classes) |

**Input**: Grayscale 28×28 image  
**Output**: One of 25 ASL letter classes (A–Y)

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install torch torchvision streamlit Pillow
```

### 2. Run the Application

```bash
streamlit run app.py
```

Make sure `model_final.pth` is in the same directory as `app.py`.

### 3. Use the App

1. Open the Streamlit URL in your browser (usually `http://localhost:8501`)
2. Upload a hand sign image (JPG, JPEG, or PNG)
3. The predicted letter will be displayed instantly

---

## 🖼️ Preprocessing Pipeline

Before inference, images are transformed:

1. Convert to **grayscale**
2. Resize to **28×28 pixels**
3. Convert to **tensor**
4. Normalize with mean `0.5` and std `0.5`

---

## 📊 Classes

The model recognizes 25 letters: **A B C D E F G H I J K L M N O P Q R S T U V W X Y**

> ⚠️ The letter **Z** is excluded as it requires a dynamic gesture (motion-based).

---

## 📁 Dataset

The model was trained on the [Sign Language MNIST](https://www.kaggle.com/datasets/datamunge/sign-language-mnist) dataset — a 28×28 grayscale image dataset modeled after the classic MNIST format, containing 27,455 training and 7,172 test cases.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **PyTorch** — model definition and inference
- **Torchvision** — image transforms
- **Streamlit** — web interface
- **Pillow** — image loading

---

## 📄 License

This project is for educational purposes.
