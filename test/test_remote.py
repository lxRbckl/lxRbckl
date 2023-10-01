# import <
from github import (
   
   Auth,
   Github
   
)

from lxrbckl.remote import (
   
   githubSet, 
   githubGet,
   githubDel,
   githubAdd,
   requestsGet
   
)

# >


# declare <
gGithubToken = ''

gBranch = 'python'
gFilename = 'test.json'
gRepository = 'lxRbckl/lxrbckl'
gGithub = Github(auth = Auth.Token(gGithubToken))

# >


# def test_githubSet():
#    '''  '''

#    pass


# def test_githubGet():
#    '''  '''

#    pass


def test_githubAdd():
   ''' githubAdd() Test Suite '''

   result = githubAdd(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'this' : 'example'}
      
   )
   assert (result == None), 'Can add new files.'
   
   expected = 'File already exists.'
   result = githubAdd(
   
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'this' : 'example'}
      
   )
   assert (result == expected), 'Can detect existing files.'
   

def test_githubDel():
   ''' githubDel() Test Suite '''
   
   result = githubDel(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository
      
   )
   assert (result == None), 'Can delete existing files.'
   
   expected = 'File does not exist.'
   result = githubDel(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository
      
   )
   assert (result == expected), 'Can detect non-existing files.'


# def test_requestsGet():
#    '''  '''
   
#    pass