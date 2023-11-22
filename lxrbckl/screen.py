# import <
from pyautogui import (
   
   click as pyautoguiClick,
   moveTo as pyautoguiMoveTo,
   locateCenterOnScreen as pyautoguiLocateCenterOnScreen
   
)

# >


class screen:

   def move(
      
      x,
      y,
      isRetinaDisplay = True
      
   ):
      '''  '''
      
      fDisplay = lambda i : (i / 2) if (isRetinaDisplay) else i
      x, y = map(fDisplay, [x, y])
      
      pyautoguiMoveTo(x, y)


   def find(
      
      image,
      grayscale,
      confidence
      
   ):
      '''  '''
      
      return pyautoguiLocateCenterOnScreen(
         
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
         
      for i in range(times): pyautoguiClick(x, y)