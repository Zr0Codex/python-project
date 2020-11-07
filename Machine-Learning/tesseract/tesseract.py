# adds more image processing capabilities
from PIL import Image, ImageEnhance
import pytesseract
# assigning an image from the source path
img = Image.open('img/test2.png')
result = pytesseract.image_to_string(img)
with open("textoutput/text_result2.txt", mode="w") as file:
  file.write(result)
  print("finished")