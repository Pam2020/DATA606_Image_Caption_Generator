
import streamlit as st 
from PIL import Image

import torch 
import import_ipynb
import Streamlit_functions
from Streamlit_functions import get_loader
from Streamlit_functions import CNNtoRNN
from Streamlit_functions import EncoderCNN
from Streamlit_functions import DecoderRNN

st.title("Image Caption Generator")

train_loader, dataset = get_loader(
        root_folder="/content/drive/MyDrive/DataSet/images",
        annotation_file="/content/drive/MyDrive/DataSet/captions.txt",
        transform=transform,
        num_workers=2,
    )

transform = transforms.Compose(
    [
        transforms.Resize((299, 299)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)

model = torch.load('/content/drive/MyDrive/image-captioning-model.pth')
model.eval()

def caption_custom_image(img_path):
    #count = 0
    #for img_path in image_paths:
    #count = count + 1
    #print("Image ")
    plt.figure(figsize=(6,4))
    full_path = '/content/' + img_path
    img = transform(Image.open(full_path).convert("RGB")).unsqueeze(0)
    caption = ' '.join(model.caption_image(img.to('cuda'), dataset.vocab)[1:-1])
    #read_img = plt.imread(full_path)
    #plt.imshow(np.real(read_img))
    #plt.axis("on")
    #plt.title(caption)
    #plt.show()
    #print("\n")
    return caption


uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Generating captions...")
    label = caption_custom_image(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))