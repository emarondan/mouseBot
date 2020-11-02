import pyautogui
import sys
import random
import time

def moveMouse():
    xOffset = random.randrange(100,1200)
    yOffset = random.randrange(100,1200)
    pyautogui.moveTo(xOffset,yOffset,1)

def KeyPress():
    randomkey= random.randrange(0,100)
    if randomkey < 50:
        pyautogui.press('shift')
    elif 50 < randomkey < 100:
        pyautogui.press('alt')

def change():
    timespress = random.randint(1, 5)
    pyautogui.keyDown('alt')
    for i in range(timespress):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.keyUp('alt')
    
def scroll():
    randomScroll = random.randint(-10, 10)
    pyautogui.scroll(randomScroll)

time.sleep(5)
while True:
    ActionTime= random.randint(0,3)
    time.sleep(ActionTime)
    try:    
        if sys.argv[1] == 'mouseonly':
            Action = 31
    except:
        Action = random.randrange(0,100)
    if Action < 40:
        moveMouse()
    if 40 < Action < 60:
        KeyPress()
    if 60 < Action < 80:
        change()
    if Action >80:
        scroll()




