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
   pBranch: str = 'main',
   pMessage: str = 'Automated Commit'
   
):
   '''  '''
   
   # get repository <
   # format the data <
   # get content from repository <
   repository = pGithub.get_repo(pRepository)
   data = str(pData).replace('\'', '\"').replace('None', 'null')
   content = repository.get_contents(path = pFilename, ref = pBranch)

   # >

   repository.update_file(

      content = data,
      branch = pBranch,
      sha = content.sha,
      message = pMessage,
      path = content.path

   )
   

def githubGet(
   
   pFilename: str,
   pGithub: object,
   pRepository: str,
   pBranch: str = 'main'
   
):
   '''  '''
   
   # get repository <
   # get content from repository <
   repository = pGithub.get_repo(pRepository)
   content = repository.get_contents(path = pFilename, ref = pBranch)

   # >

   return loads(content.decoded_content.decode())


def githubAdd(

   pData,
   pFilename: str,
   pGithub: object,
   pRepository: str,
   pBranch: str = 'main',
   pMessage: str = 'Automated Commit'
        
):
   '''  '''
   
   # try (if ) <
   # except (then ) <
   try:
   
      # get repository <
      # add file to repository <
      repository = pGithub.get_repo(pRepository)
      repository.create_file(

         path = pFilename,
         branch = pBranch,
         message = pMessage,
         content = dumps(pData)

      )
      
      # >
   
   except: return 'File already exists.'

   # >


def githubDel(
   
   pGithub,
   pRepository,
   pFilename: str,
   pBranch: str = 'main',
   pMessage: str = 'Automated Deletion'
   
):
   '''  '''
   
   # try (if ) <
   # except (then ) <
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