import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
src_path = "C:/math exp/"


# Set the tesseract path in the script
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def get_string(img_path, tub_kernel):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones(tub_kernel, np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=2)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", gray)

    #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    _, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Write the image after apply opencv
    cv2.imwrite(src_path + "thres.png", gray)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    return result


print('--- Start recognize match ---')
img_path = src_path + "exp 5.jpeg"

# Extract text from image
result = get_string(img_path, (2, 3)).strip()

print("Text result:")
print(result)

print("------ Done -------")


