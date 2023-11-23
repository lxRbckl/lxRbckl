# import <
from pyautogui import (
   
   ImageNotFoundException,
   click as pyautoguiClick,
   moveTo as pyautoguiMoveTo,
   locateCenterOnScreen as pyautoguiLocateCenterOnScreen
   
)

# >


class screen:
   
   def move(self, xy): 
      
      try: pyautoguiMoveTo(xy[0], xy[1])
      except TypeError: return None
   
   
   def click(self, xy, multiply = 1): 
      
      try: pyautoguiClick(x = xy[0], y = xy[1], clicks = multiply)
      except TypeError: return None


   def find(
      
      self,
      image,
      confidence,
      
      grayscale = True,
      isRetinaDisplay = True
      
   ):
      '''  '''
      
      # try (if exists) <
      # except (then does not exist) <
      try:
                  
         adjust = lambda i : (i / 2) if (isRetinaDisplay) else i
         return list(map(adjust, pyautoguiLocateCenterOnScreen(
            
            image = image,
            grayscale = grayscale,
            confidence = confidence
            
         )))
      
      except ImageNotFoundException: return None
      
      # >