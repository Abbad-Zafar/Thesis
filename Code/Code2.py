import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# read the image using OpenCV
image = cv2.imread("image63_1.jpeg")
# or you can use Pillow
#image = Image.open("image63_1.jpeg")

# get the string
string = pytesseract.image_to_string(image)
# print it
print("str = ", string)