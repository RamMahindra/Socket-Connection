import pyautogui 
screenWidth, screenHeight = pyautogui.size()  
pyautogui.moveTo(screenWidth/2, screenHeight/2)
currentMouseX, currentMouseY = pyautogui.position()
##pyautogui.click() 
##pyautogui.moveRel(None, 10) # move mouse 10 pixels down 
##pyautogui.doubleClick() 
###pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad) # use tweening/easing function to move mouse over 2 seconds. 
##pyautogui.typewrite('Hello world!', interval=0.25) # type with quarter-second pause in between each key 
##pyautogui.press('esc') 
##pyautogui.keyDown('shift') 
##pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left']) 
##pyautogui.keyUp('shift') 
##pyautogui.hotkey('ctrl', 'c')

while True:
    currentMouseX1, currentMouseY1 = pyautogui.position()
    if ((currentMouseX1 - currentMouseX) or (currentMouseY1 - currentMouseY)):
        print pyautogui.position()
        currentMouseX, currentMouseY = currentMouseX1, currentMouseY1
