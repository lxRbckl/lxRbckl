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


def test_githubSet():
   ''' githubSet() Test Suite '''

   githubAdd(
         
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pData = '<insert data>',
      pRepository = gRepository
      
   )

   result = githubSet(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'test' : 'example'}
      
   )
   assert (result == None), 'Can update existing files.'

   githubDel(
      
      pBranch = gBranch,
      pGithub = gGithub,
      pFilename = gFilename,
      pRepository = gRepository
      
   )


# def test_githubGet():
#    ''' githubGet() Test Suite '''

#    githubAdd(
      
#       pBranch = gBranch,
#       pGithub = gGithub,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'test' : 'example'}
      
#    )
   
#    expected = {'test' : 'example'}
#    result = githubGet(
      
#       pBranch = gBranch,
#       pGithub = gGithub,
#       pFilename = gFilename,
#       pRepository = gRepository
      
#    )
#    assert(result == expected), 'Can load existing files.'
   
#    githubDel(
      
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository
      
#    )
   
#    expected = 'File does not exist.'
#    result = githubGet(
      
#       pBranch = gBranch,
#       pGithub = gGithub,
#       pFilename = 'dne.json',
#       pRepository = gRepository
      
#    )
#    assert (result == expected), 'Can detect non-existing files.'


# def test_githubAdd():
#    ''' githubAdd() Test Suite '''

#    result = githubAdd(
      
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'this' : 'example'}
      
#    )
#    assert (result == None), 'Can add new files.'
   
#    expected = 'File already exists.'
#    result = githubAdd(
   
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'this' : 'example'}
      
#    )
#    assert (result == expected), 'Can detect existing files.'
   

# def test_githubDel():
#    ''' githubDel() Test Suite '''
   
#    result = githubDel(
      
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository
      
#    )
#    assert (result == None), 'Can delete existing files.'
   
#    expected = 'File does not exist.'
#    result = githubDel(
      
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository
      
#    )
#    assert (result == expected), 'Can detect non-existing files.'


# def test_requestsGet():
#    '''  '''
   
#    pass