# import <
from time import sleep
from requests import get
from json import loads, dumps
from json.decoder import JSONDecodeError
from requests.exceptions import MissingSchema

# >


def githubSet(
   
   pData,
   pFilename: str,
   pGithub: object,
   pRepository: str,
   
   pSleep: int = 3,
   isNew: bool = False,
   pBranch: str = 'main'
   
):
   '''  '''
   
   # try (if permitted) <
   # except (then not permitted) <
   try:
   
      repository = pGithub.get_repo(pRepository)
      
      # if (create) <
      # elif (update) <
      if (isNew): 
      
         repository.create_file(
            
            path = pFilename,
            branch = pBranch,
            content = dumps(pData),
            message = 'Automated Set'
            
         )
      
      elif (not isNew):
         
         data = str(pData).replace('\'', '\"').replace('None', 'null')
         content = repository.get_contents(path = pFilename, ref = pBranch)
         
         repository.update_file(
            
            content = data,
            branch = pBranch,
            sha = content.sha,
            path = content.path,
            message = 'Automated Update'
            
         )
      
      # >
   
      sleep(pSleep)
   
   except: return {
      
      True : 'File already exists.',
      False : 'File does not exist.'
      
   }[isNew]
   
   # >
   

def githubGet(
   
   pFilename: str,
   pGithub: object,
   pRepository: str,
   
   pBranch: str = 'main'
   
):
   '''  '''
   
   # try (if existing) <
   # except (then non-existing) <
   try:
   
      # get repository <
      # get content from repository <
      repository = pGithub.get_repo(pRepository)
      content = repository.get_contents(path = pFilename, ref = pBranch)

      # >

      return loads(content.decoded_content.decode())

   except: return 'File does not exist.'

   # >


def githubDel(
   
   pGithub,
   pFilename: str,
   pRepository: str,
   
   pSleep: int = 3,
   pBranch: str = 'main',
   pMessage: str = 'Automated Deletion'
   
):
   '''  '''
   
   # try (if existing) <
   # except (then non-existing) <
   try:
   
      repository = pGithub.get_repo(pRepository)
      file = repository.get_contents(path = pFilename, ref = pBranch)
         
      repository.delete_file(
         
         sha = file.sha,
         path = pFilename,
         branch = pBranch,
         message = pMessage
         
      )
      
      sleep(pSleep)
   
   except: return 'File does not exist.'
   
   # >
   

def requestsGet(pLink: str):
   '''  '''

   # try (if valid link) <
   # except (then invalid link) <
   # except (then invalid .json format) <
   try: 
      
      return {
      
         'txt' : lambda : get(pLink).text,
         'json' : lambda : loads(get(pLink).text)
         
      }[pLink.split('.')[-1]]()
   
   except KeyError: return 'Invalid link.'
   except MissingSchema: return 'Invalid link.'
   except JSONDecodeError: return 'Loaded data is broken.'
   
   # >