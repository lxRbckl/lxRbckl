# import <
from pyautogui import (
   
   click as pyautoguiClick,
   moveTo as pyautoguiMoveTo,
   locateCenterOnScreen as pyautoguiLocateCenterOnScreen
   
)

# >


class screen:

   def move(self, x, y): pyautoguiMoveTo(x, y)


   def find(
      
      self,
      image,
      grayscale,
      confidence,
      
      isRetinaDisplay = True
      
   ):
      '''  '''
                  
      adjust = lambda i : (i / 2) if (isRetinaDisplay) else i
      x, y = map(adjust, pyautoguiLocateCenterOnScreen(
         
         image = image,
         grayscale = grayscale,
         confidence = confidence
         
      ))
      
      return x, y


   def click(
      
      self,
      x,
      y,
      times = 1
      
   ):
      '''  '''
         
      for i in range(times): pyautoguiClick(x, y)