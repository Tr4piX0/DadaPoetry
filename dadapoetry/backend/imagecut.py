from PIL import Image
from pytesseract import pytesseract
from random import randint
import psycopg2

conn = psycopg2.connect(
    database="db_name",
    host="db_host",
    user="db_user",
    password="db_pass",
    port="db_port",
)

poetry_structure = [0, 1, 2, 3, "\n",
                    4, 5, 6, "\n",
                    7, 8, 9, "\n",
                    "\n",
                    10, 11, 12, 13, "\n",
                    14, 15, 16, "\n",
                    17, 18, 19, 20, "\n",
                    "\n",
                    21, 22, 23, "\n",
                    24, 25, "\n",
                    26, 27, 28]

class Poetry(conn):
    def cut(self):
        img = Image.open(self.path)
        text = pytesseract.image_to_string(img)
        return text

    def structure(self, strophes=4):
        if strophes < 4:
            print(
                "your image \n does \n not contain enough \n \
                  words for a poetry"
            )

        text = self.cut().split(" ")
        words = []
        poetry = ""

        for ix in range(29):
            word = randint(1, len(text))
            words.append(text[word])

        for ix in poetry_structure:
            if ix == "\n":
                poetry + ix
            else:
                poetry + words[ix]

        return poetry
