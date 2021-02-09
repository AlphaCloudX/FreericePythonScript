import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PyDictionary import PyDictionary
import pyautogui
import random
import time

# zoom to 250%, freerice.com and has to be english

dictionary = PyDictionary()
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Michael\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# fullscreen
# im=ImageGrab.grab()
# im.show()

while True:
    # part of the screen
    im = ImageGrab.grab(bbox=(870, 200, 1670, 1000))  # x1, y1 | x2 y2
    im.save("img.jpg")
    img = cv2.imread("img.jpg")

    # Getting text from image
    text = pytesseract.image_to_string(img)
    print(text)

    # Breaking down the spaced out words into lists and strings
    possible_options = list(filter(None, text.split('\n')[:-1]))[1::]
    word_to_search = list(filter(None, text.split('\n')[:-1]))[0][:-7]
    possible_meanings = dictionary.synonym(word_to_search)

    print("----")
    print(word_to_search)
    print(possible_options)
    print(possible_meanings)
    print("----")

    # Checking against the dictionary

    wordFound = False
    if possible_meanings == None:
        possible_meanings = ['t']

    for i in range(len(possible_options)):
        for j in range(len(possible_meanings)):
            if possible_options[i] == possible_meanings[j]:
                position = i + 1
                wordFound = True

    # print(position)
    # print(wordFound)

    # Checking what box to click
    if not wordFound:
        position = random.randint(1, 4)

    if position == 1:
        pyautogui.moveTo(950, 450)
        pyautogui.click()

    if position == 2:
        pyautogui.moveTo(950, 600)
        pyautogui.click()

    if position == 3:
        pyautogui.moveTo(950, 750)
        pyautogui.click()

    if position == 4:
        pyautogui.moveTo(950, 900)
        pyautogui.click()

    time.sleep(4)
    print("DONE")