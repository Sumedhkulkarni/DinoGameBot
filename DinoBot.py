from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time


class Cordinates:
    replayBtn = (340, 390)
    dinosaur = (171, 440)
    # 240 = will be the x-co-ordinate to check for tree
    # 420 = will be the y-co-ordinate to check for lowest obstacle


def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('Down')


def pressSpace():
    pyautogui.keyUp('Down')
    pyautogui.keyDown('space')
    # print("Jump")
    time.sleep(0.16)
    pyautogui.keyUp('space')
    pyautogui.keyDown('Down')


def imageGrab():
    # set co-ordinates for the box
    box = (Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1],  Cordinates.dinosaur[0] + 150, Cordinates.dinosaur[1] + 5)
    image = ImageGrab.grab(box)  # grap  the image in the box
    grayImage = ImageOps.grayscale(image)  # convert the image int  o GraysSale image for better results
    a = array(grayImage.getcolors())
    return a.sum()


def main():
    restartGame()
    while True:
         if imageGrab() != 697:
                 pressSpace()
                 time.sleep(0.07)


main()
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time


class Cordinates:
    replayBtn = (340, 390)
    dinosaur = (171, 440)
    # 240 = will be the x-co-ordinate to check for tree
    # 420 = will be the y-co-ordinate to check for lowest obstacle


def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('Down')


def pressSpace():
    pyautogui.keyUp('Down')
    pyautogui.keyDown('space')
    # print("Jump")
    time.sleep(0.16)
    pyautogui.keyUp('space')
    pyautogui.keyDown('Down')


def imageGrab():
    # set co-ordinates for the box
    box = (Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1],  Cordinates.dinosaur[0] + 150, Cordinates.dinosaur[1] + 5)
    image = ImageGrab.grab(box)  # grap  the image in the box
    grayImage = ImageOps.grayscale(image)  # convert the image int  o GraysSale image for better results
    a = array(grayImage.getcolors())
    return a.sum()


def main():
    restartGame()
    while True:
         if imageGrab() != 697:
                 pressSpace()
                 time.sleep(0.07)


main()
