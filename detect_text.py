import cv2
import pytesseract
from PIL import Image
class Detect_text:
    def Detect_text_method(path):
        pytesseract.pytesseract.tesseract_cmd = 'E:\\tesseract\\installed_file\\tesseract.exe'

        img = cv2.imread(path)

        text = pytesseract.image_to_string(img)
        return text
