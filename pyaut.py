import pyautogui


print(pyautogui.size())
print(pyautogui.position())

#idle
# pyautogui.displayMousePosition()  

# pyautogui.moveTo(0,0,duration=3)

# pyautogui.dragTo(100,100,duration=4)
# pyautogui.dragRel(200,400,duration=4)

# pyautogui.scroll(225)

#### for opening drawing and closing paint application

pyautogui.click(x=2,y=1080,button='left',clicks=1,interval=2)

pyautogui.click(x=502,y=422,button='left',clicks=1,interval=3)



pyautogui.dragTo(235,570,duration=2)
pyautogui.dragTo(438,570,duration=2)
pyautogui.dragTo(235,438,duration=2)


pyautogui.click(x=1521,y=148,button='left',clicks=1)

































