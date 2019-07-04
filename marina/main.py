from PIL import Image
import pytesseract
"""
im = Image.open('bon_commande.jpeg')
text = pytesseract.image_to_string(im, lang="french")
#text = pytesseract.image_to_string(Image.open('bon_commande.jpeg'))
print(text)"""
text = pytesseract.image_to_string(Image.open("test.png"))
print(text)
print(pytesseract.image_to_string(Image.open("test.png")))

