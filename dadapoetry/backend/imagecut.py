from PIL import Image
from pytesseract import pytesseract
from random import randint
import os

path_img = '/home/arnaldo/Imagens/imgs/'

def poetry(text):
    complete = []
    len_text = len(text)
    if len_text >= 29:
        words = []
        poetry_structure =[
            0, 1, 2, 3, '\n',
            4, 5, 6, '\n',
            7, 8, 9, '\n',
            '\n',
            10, 11, 12, 13, '\n',
            14, 15, 16, '\n',
            17, 18, 19, 20, '\n',
            '\n',
            21, 22, 23, '\n',
            24, 25, '\n',
            26, 27, 28]
        
        for ix in range(29):
            word = randint(len_text)
            words.append(text[word])

        for ix in poetry_structure:
            if ix == '\n':
                complete.append(ix)
            else:
                complete.append(words[ix])
    else:
        print("your image \n does \n not contain enough \n words for a poetry")          

    return complete

for root, dirs, file_names in os.walk(path_img):
    for file_name in file_names:
        img = Image.open(path_img + file_name)
        text = pytesseract.image_to_string(img)

        poetry(text)
