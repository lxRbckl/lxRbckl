# import <
from sys import stderr
from requests import get
from json import loads, dumps, load

# >


def githubSet(
   
   pData,
   pFilename: str,
   pGithub: object,
   pRepository: str,
   
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
         
   except: return 'File does not exist.'
   
   # >
   

def requestsGet(
   
   pLink: str,
   pDisplayError: bool = False

):
   ''' supports: (.json, .txt) '''
   
   # try (if ) <
   # except (then ) <
   try:
      
      ftype = pLink.split('.')[-1]
      
      if (ftype == 'txt'): return get(pLink).text
      if (ftype == 'json'): return loads(get(pLink).text)
   
   except Exception as e:
      
      if (pDisplayError): 
         
         print('Error: ', e)
         print('Link: ', pLink)
         stderr.write(f"Error: {e}\n")
         stderr.write(f"Link: {pLink}\n")
      
      else: pass
   
   # >