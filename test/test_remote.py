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
gGithub = Github(auth = Auth.Token(gGithubToken))

# >


# def test_githubSet():
#    '''  '''

#    pass


# def test_githubGet():
#    '''  '''

#    pass


def test_githubAdd():
   '''
   Can add new files.
   Can detect existing files.
   '''

   result = githubAdd(
      
      pGithub = gGithub,
      pBranch = 'python2',
      pFilename = 'test.json',
      pData = {'this' : 'example'},
      pRepository = 'lxRbckl/lxrbckl'
      
   )
   assert(result == None)
   
   result = githubAdd(
   
      pGithub = gGithub,
      pBranch = 'python2',
      pFilename = 'test.json',
      pData = {'this' : 'example'},
      pRepository = 'lxRbckl/lxrbckl'
      
   )
   assert(result == False)
   

def test_githubDel():
   '''
   Can delete existing files.
   Can detect non-existing files.
   '''
   
   result = githubDel(
      
      pGithub = gGithub,
      pBranch = 'python2',
      pFilename = 'test.json',
      pRepository = 'lxRbckl/lxrbckl',
      
   )
   assert(result == None)
   
   result = githubDel(
      
      pGithub = gGithub,
      pBranch = 'python2',
      pFilename = 'test.json',
      pRepository = 'lxRbckl/lxrbckl',
      
   )
   assert(result == False)


# def test_requestsGet():
#    '''  '''
   
#    pass