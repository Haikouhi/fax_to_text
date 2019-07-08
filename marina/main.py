from PIL import Image
import pytesseract
"""
im = Image.open('bon_commande.jpeg')
text = pytesseract.image_to_string(im, lang="french")
#text = pytesseract.image_to_string(Image.open('bon_commande.jpeg'))
print(text)"""
<<<<<<< HEAD
text = pytesseract.image_to_string(Image.open("test.png"))
print(text)
print(pytesseract.image_to_string(Image.open("test.png")))

=======
text = pytesseract.image_to_string(Image.open("bon-de-commande.jpg"))
print(text)
#print(pytesseract.image_to_string(Image.open("fantastique.jpg")))
>>>>>>> 07fd66ddcf25a78d9fed518e5e0faa34c3d824aa
