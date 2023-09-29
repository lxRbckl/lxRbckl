# import <
from re import split

# >


# declare <


# >


def setFile(
   
   pData,
   pFile: str,
   pDelimeter: str = '/'
   
):
   '''  '''
   
   # try (if valid object) <
   # except (then invalid object type) <
   try:
   
      file = pDelimeter.join(split(r'[/\\]+', pFile))
      with open(file, 'w') as fout: fout.write(pData)
      
      return True
   
   except Exception as e: print(e); return False
   
   # >


def getFile(
   
   pFile: str,
   pDelimeter = '/'
   
):
   '''  '''
   
   rData = ''
   file = pDelimeter.join(split(r'[/\\]+', pFile))
   with open(file, 'r') as fin:
      
      print(fin.read())


def delFile():
   '''  '''
   
   pass