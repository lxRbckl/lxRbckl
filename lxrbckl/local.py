# import <
from re import split
from os import remove, path
from json import dump, load

# >


# declare <


# >


def getProjectPath(
   
   pProjectName: str,
   pDelimeter: str = '/'
   
):
   '''  '''
   
   # try (if ) <
   # except (then ) <
   try:
   
      projectPath = path.realpath(__file__).split(pDelimeter)
      projectBase = projectPath.index(pProjectName)

      return pDelimeter.join(projectPath[:(projectBase + 1)])

   except: return None
   
   # >


def fileSet(
   
   pData,
   pFilepath: str,
   pIndent: int = 3,
   pDelimeter: str = '/',
   pEnding: str = '.json',
   pOverride: bool = True,
   pShowError: bool = False
   
):
   '''  '''
      
   # try (if permitted) <
   # except (then not permitted) <
   try:

      file = pDelimeter.join(split(r'[/\\]+', pFilepath))

      # if (write to file) <
      # else (throw error) <
      if ((path.isfile(file) is False) or (pOverride)):
         
         with open(file, 'w') as fout:
            
            {
               
               '.txt' : lambda : fout.write(pData),
               '.json' : lambda : dump(
                  
                  fp = fout,
                  obj = pData,
                  indent = pIndent
                  
               )
               
            }[pEnding]()

      else: raise Exception(f'{file} already exists.')

      # >

   except Exception as e: return e if (pShowError) else False
   
   # >


def fileGet(
   
   pFilepath: str,
   pDelimeter: str = '/',
   pEnding: str = '.json',
   pShowError: bool = False
   
):
   '''  '''
   
   # try (if existing file) <
   # except (then non-existing file) <
   try:
   
      file = pDelimeter.join(split(r'[/\\]+', pFilepath))
      with open(file, 'r') as fin:
         
         return {
            
            '.txt' : lambda : fin.read(),
            '.json' : lambda : load(fin)
            
         }[pEnding]()
   
   except Exception as e: return e if (pShowError) else False
   
   # >


def fileDel(
   
   pFilepath: str,
   pShowError: bool = False
   
):
   '''  '''
   
   # try (if existing file) <
   # except (then non-existing file) <
   try: remove(pFilepath)
   except Exception as e: return e if (pShowError) else False
   
   # >