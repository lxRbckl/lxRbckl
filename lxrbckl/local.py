# import <
from re import split
from json.decoder import JSONDecodeError
from json import (
   
   dump,
   load
   
)
# from os import (
   
#    getcwd,
#    remove,
#    path as ospath
   
# )
from os import (
   
   getcwd,
   remove
   
)
from os.path import (
   
   isfile,
   dirname,
   basename
   
)

# >


# declare <

# print(path.dirname(getcwd())) # remove
# print(path.basename(getcwd())) # remove


# >


def getProjectPath(
   
   pFile: str = '',
   pDelimeter: str = '/'
   
):
   '''  '''
   
   return '{}{}'.format(
      
      f'{dirname(getcwd())}{pDelimeter}{basename(getcwd())}',
      pDelimeter.join(split(r'[/\\]+', pFile))
      
   )
   
print(getProjectPath(pFile = '\\this\\is\\a\\test')) # remove


def fileSet(
   
   pData,
   pFile: str,
   pIndent: int = 3,
   pOverride: bool = True,
   pShowError: bool = False
   
):
   '''  '''
      
   # try (if permitted) <
   # except (then not permitted) <
   try:

      # if (write to file) <
      # else (throw error) <
      if ((isfile(pFile) is False) or (pOverride)):
         
         with open(pFile, 'w') as fout:
            
            {
               
               '.txt' : lambda : fout.write(pData),
               '.json' : lambda : dump(
                  
                  fp = fout,
                  obj = pData,
                  indent = pIndent
                  
               )
               
            }[pEnding]()

      else: raise Exception('File already exists.')

      # >

   except Exception as e: return e if (pShowError) else False
   
   # >


def fileGet(
   
   pFile: str,
   pEnding: str = '.json'
   
):
   '''  '''
   
   # try (if existing file) <
   # except (then bad .json format) <
   # except (then non-existing file) <
   try:
   
      print(pFile) # remove
      with open(pFile, 'r') as fin:
         
         return {
            
            '.txt' : lambda : fin.read(),
            '.json' : lambda : load(fin)
            
         }[pEnding]()
   
   except JSONDecodeError: return 'Loaded data is broken.'
   except FileNotFoundError: return 'File does not exist.'
   
   # >


def fileDel(pFile: str):
   '''  '''
   
   # try (if existing file) <
   # except (then non-existing file) <
   try: remove(pFile)
   except FileNotFoundError: return False
   
   # >