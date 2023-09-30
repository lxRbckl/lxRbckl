# import <
from requests import get
from json import loads, dumps

# >


# declare <


# >


def githubSet(
   
   pData,
   pFile: str,
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
   content = repository.get_contents(path = pFile, ref = pBranch)

   # >

   repository.update_file(

      content = data,
      branch = pBranch,
      sha = content.sha,
      message = pMessage,
      path = content.path

   )

def githubGet():
   '''  '''
   
   pass


def githubAdd():
   '''  '''
   
   pass


def requestsGet():
   '''  '''
   
   pass