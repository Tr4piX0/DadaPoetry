from PIL import Image
from pytesseract import pytesseract
import os

path_img = '/home/arnaldo/Imagens/imgs/'

# img = Image.open(path_img)
# text = pytesseract.image_to_string(img)

for root, dirs, file_names in os.walk(path_img):
    for file_name in file_names:
        img = Image.open(path_img + file_name)
        text = pytesseract.image_to_string(img)

        print(text)
