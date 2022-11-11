from PIL import Image
from pytesseract import pytesseract

class ImageCut(path):
    def cut(self):
        img = Image.open(self.path)
        text = pytesseract.image_to_string(img)
        return text

    def makePoetry(self,
                   verses_per_strophe=[4,3,4,3],
                   n_words_per_strophe,
                   strophes):
        words = self.cut.split(' ')
        poetry = []
        for stro in range(randint(strophes)):
            strophe = []
            verses = []
            if type(verses_per_strophe) == 'list':
                for verse in verses_per_strophe:
                    for word in range(verse*randint(n_words_per_strophe)):
                        verses.append(words[word])
                    strophe.append(verses)
                poetry.append(strophe)
            else:
                for verse in range(randint(verses_per_strophe)):
                    for word in range(randint(n_words_per_strophe)):
                        verses.append(words[word])
                    strophe.append(verses)
                poetry.append(strophe)

        text_poetry = ""
        for stro in poetry:
            for s in stro:
                for verse in s:
                    text_poetry + s + ' '
                text_poetry + '\n'
            text_poetry + '\n'

        return text_poetry
