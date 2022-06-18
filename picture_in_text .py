import pytesseract
import os
import pyautogui
from PIL import Image

# Делаем скриншот и считываем его с картинки
pyautogui.screenshot('C:\\Users\\Professional\\Desktop\\screen' + '.png', region=(0, 53, 1680, 890))
img = Image.open("screen.png")
pytesseract.pytesseract.tesseract_cmd = r"E:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(img, lang="rus")
print(text.strip())
# Запись текста в фаил
with open('Image document.txt', 'a') as f:
    f.write(text.strip()+"\n")
# Удаление скриншота
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'screen.png')
os.remove(path)
