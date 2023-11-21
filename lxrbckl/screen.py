# import <
from pyautogui import (
   
   click,
   moveTo,
   locateCenterOnScreen
   
)

# >


def move(
   
   x,
   y,
   isRetinaDisplay = True
   
):
   '''  '''
   
   fDisplay = lambda i : (i / 2) if (isRetinaDisplay) else i
   x, y = map(fDisplay, [x, y])
   
   moveTo(x, y)


def find(
   
   image,
   grayscale,
   confidence
   
):
   '''  '''
   
   return locateCenterOnScreen(
      
      image = image,
      grayscale = grayscale,
      confidence = confidence
      
   )


def click(
   
   x,
   y,
   times = 1
   
):
   '''  '''
      
   for i in range(times): click(x, y)