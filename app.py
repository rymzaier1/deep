import streamlit as st
import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms

# =====================================
# Classes alphabet
# =====================================

classes = {
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    6:'G',
    7:'H',
    8:'I',
    9:'J',
    10:'K',
    11:'L',
    12:'M',
    13:'N',
    14:'O',
    15:'P',
    16:'Q',
    17:'R',
    18:'S',
    19:'T',
    20:'U',
    21:'V',
    22:'W',
    23:'X',
    24:'Y'
}

# =====================================
# CNN MODEL
# =====================================

class CNNBaseline(nn.Module):

    def __init__(self):

        super(CNNBaseline, self).__init__()

        self.conv = nn.Sequential(

            nn.Conv2d(
                in_channels=1,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2)
        )

        self.fc = nn.Sequential(

            nn.Linear(64 * 7 * 7, 128),

            nn.ReLU(),

            nn.Dropout(0.5),

            nn.Linear(128, 25)
        )

    def forward(self, x):

        x = self.conv(x)

        x = torch.flatten(x, 1)

        x = self.fc(x)

        return x

# =====================================
# LOAD MODEL
# =====================================

model = CNNBaseline()

model.load_state_dict(
    torch.load(
        "model_final.pth",
        map_location=torch.device("cpu")
    )
)

model.eval()

# =====================================
# STREAMLIT INTERFACE
# =====================================

st.title("Sign Language Recognition")

st.write("Upload an image of a hand sign")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

# =====================================
# PREDICTION
# =====================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # preprocessing

    transform = transforms.Compose([

        transforms.Grayscale(),

        transforms.Resize((28, 28)),

        transforms.ToTensor(),

        transforms.Normalize((0.5,), (0.5,))
    ])

    img = transform(image)

    img = img.unsqueeze(0)

    # prediction

    with torch.no_grad():

        outputs = model(img)

        _, predicted = torch.max(outputs, 1)

        prediction = classes[predicted.item()]

    st.success(f"Prediction: {prediction}")