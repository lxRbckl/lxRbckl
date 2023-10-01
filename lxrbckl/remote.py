# import <
from requests import get
from json import loads, dumps

# >


# declare <


# >


def githubSet(
   
   pData,
   pFilename: str,
   pGithub: object,
   pRepository: str,
   isNew: bool = False,
   pBranch: str = 'main',
   pMessage: str = 'Automated Action'
   
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
            message = pMessage,
            content = dumps(pData)
            
         )
      
      elif (not isNew):
         
         data = str(pData).replace('\'', '\"').replace('None', 'null')
         content = repository.get_contents(path = pFilename, ref = pBranch)
         
         repository.update_file(
            
            content = data,
            branch = pBranch,
            sha = content.sha,
            message = pMessage,
            path = content.path
            
         )
      
      # >
   
   except: return {
      
      True : 'error 1',
      False : 'error 2'
      
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
   pRepository,
   pFilename: str,
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
   isJSON: bool = True
   
):
   '''  '''
   
   return {
      
      False : lambda : get(pLink).text,
      True : lambda : loads(get(pLink).text)
      
   }[isJSON]()