# https://medium.com/@winston.smith.spb/python-ocr-for-pdf-or-compare-textract-pytesseract-and-pyocr-acb19122f38c

# All our wrappers, except of textract, can’t work with the pdf format, 
# so we should transform our pdf file to the image (jpg). We will use wand for this.

from wand.image import Image as Img
from PIL import Image



with Img(filename='Exakis.pdf', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='image_name.jpg')



img = Image.open('Exakis.jpg')
crop_img = img.crop((x1, y1, x2, y2))
crop_img.save('amount.jpg')