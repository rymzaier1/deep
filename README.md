Sign Language Recognition using Deep Learning
Project Overview

This project focuses on recognizing American Sign Language (ASL) hand gestures using Deep Learning techniques.

The system can:

Predict sign language letters from images
Use a webcam in real time with Streamlit
Upload custom images for prediction

The project compares multiple Deep Learning architectures including:

CNN
ResNet18
LSTM

The final selected model is ResNet18 due to its superior accuracy.

Dataset

Dataset used:

Sign Language MNIST Dataset

The dataset contains:

28x28 grayscale hand gesture images
24 ASL classes (A–Y excluding J and Z)

Files:

sign_mnist_train.csv
sign_mnist_test.csv
Project Structure
SignLanguageRecognition/
│
├── drafts/
│   ├── draft_cnn.ipynb
│   ├── draft_resnet.ipynb
│   ├── draft_lstm.ipynb
│   └── hyperparameter_tuning.ipynb
│
├── final_notebook.ipynb
├── app.py
├── requirements.txt
├── model_final.pth
├── README.md
├── presentation.pptx
│
├── sign_mnist_train.csv
└── sign_mnist_test.csv
Deep Learning Pipeline
1. Data Preprocessing
CSV loading
Image normalization
Tensor conversion
Train/Test split
2. Data Augmentation
Random rotation
Horizontal flip
Random affine transformation
3. Models Tested
CNN Baseline

Simple convolutional neural network.

ResNet18

Transfer Learning using pretrained ResNet18.

LSTM

Sequence-based architecture tested for comparison.

Final Model

The final selected model:

ResNet18

Reasons:

Highest validation accuracy
Better generalization
Stable predictions

Final accuracy:

~98%
Evaluation Metrics

The project includes:

Accuracy curves
Loss curves
Confusion matrix
ROC Curve
Model comparison
Streamlit Application

The Streamlit app allows:

Image upload prediction
Run locally:

streamlit run app.py
Installation
Clone repository
git clone YOUR_GITHUB_LINK
cd SignLanguageRecognition
Install dependencies
pip install -r requirements.txt
