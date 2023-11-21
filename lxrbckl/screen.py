# import <
from pyautogui import (
   
   size,
   click,
   moveTo,
   locateCenterOnScreen
   
)

# >


class screen:
   
   def __init__(
      
      self,
      isRetinaDisplay = True
      
   ):
      '''  '''
      
      self.isRetinaDisplay = isRetinaDisplay
   
   
   def move(
      
      self,
      x,
      y
      
   ):
      '''  '''
      
      fDisplay = lambda i : i / 2 if (self.isRetinaDisplay) else i
      x, y = map(fDisplay, [x, y])
      
      moveTo(x, y)
   
   
   def click(
      
      self,
      x,
      y,
      
      times = 1
      
   ):
      '''  '''
      
      for i in range(times): click(x, y)

   
   def locate(
      
      self,
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