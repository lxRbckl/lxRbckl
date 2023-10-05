# import <
from re import split
from json.decoder import JSONDecodeError
from json import (
   
   dump,
   load
   
)
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


def getProjectPath(
   
   pFile: str = '',
   pDelimeter: str = '/'
   
):
   '''  '''
   
   cwd = getcwd()
   file = pDelimeter.join(split(r'[/\\]+', pFile))
   
   return pDelimeter.join([dirname(cwd), basename(cwd), file])
   

def fileSet(
   
   pData,
   pFile: str,
   pIndent: int = 3,
   pOverride: bool = True,
   pPath: str = getProjectPath()
   
):
   '''  '''
      
   # try (if permitted) <
   # except (then not permitted) <
   try:

      # if (write to file) <
      # else (throw error) <
      if ((isfile(f'{pPath}{pFile}') is False) or (pOverride)):
         
         with open(f'{pPath}{pFile}', 'w') as fout:
            
            {
               
               'txt' : lambda : fout.write(pData),
               'json' : lambda : dump(
                  
                  fp = fout,
                  obj = pData,
                  indent = pIndent
                  
               )
               
            }[pFile.split('.')[-1]]()

      else: return 'File already exists.'

      # >

   except TypeError: return 'Invalid data for this filetype.'
   
   # >


def fileGet(
   
   pFile: str,
   pPath: str = getProjectPath()
   
):
   '''  '''
   
   # try (if existing file) <
   # except (then bad .json format) <
   # except (then non-existing file) <
   try:
   
      with open(f'{pPath}{pFile}', 'r') as fin:
         
         return {
            
            'txt' : lambda : fin.read(),
            'json' : lambda : load(fin)
            
         }[pFile.split('.')[1]]()
   
   except JSONDecodeError: return 'Loaded data is broken.'
   except FileNotFoundError: return 'File does not exist.'
   
   # >


def fileDel(
   
   pFile: str,
   pPath: str = getProjectPath()

):
   '''  '''
   
   # try (if existing file) <
   # except (then non-existing file) <
   try: remove(f'{pPath}{pFile}')
   except FileNotFoundError: return 'File does not exist.'
   
   # >