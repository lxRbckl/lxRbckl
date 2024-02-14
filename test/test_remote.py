# import <
from os import environ
from github import (
   
   Auth,
   Github
   
)

from lxrbckl.remote import (
   
   githubSet, 
   githubGet,
   githubDel,
   requestsGet
   
)

# >


# declare <
gPyGitHubToken = environ.get('PYGITHUBTOKEN')

gBranch = 'python'
gFilename = 'test.json'
gRepository = 'lxRbckl/lxrbckl'
gGithub = Github(auth = Auth.Token(gPyGitHubToken))

# >


def test_githubSet():
   ''' githubSet() Test Suite '''
   
   # test <
   expected = 'File does not exist.'
   result = githubSet(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pData = {'test' : 'set'},
      pRepository = gRepository
      
   )
   assert (result == expected), 'Can detect non-existing files in repository.'

   result = githubSet(
      
      isNew = True,
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pData = {'test' : 'set'},
      pRepository = gRepository
      
   )
   assert (result == None), 'Can add new files to repository.'
   
   result = githubSet(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'test' : 'update'}
      
   )
   assert (result == None), 'Can update files in repository.'
   
   expected = 'File already exists.'
   result = githubSet(
      
      isNew = True,
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'test' : 'update'}
      
   )
   assert (result == expected), 'Can detect existing files in repository.'

   # >
   
   # deconstruct <
   githubDel(
      
      pGithub = gGithub,
      pFilename = gFilename,
      pRepository = gRepository
      
   )
   
   # >


def test_githubGet():
   ''' githubGet() Test Suite '''
   
   # construct <
   githubSet(
      
      isNew = True,
      pBranch = gBranch,
      pGithub = gGithub,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'test' : 'example'}
      
   )
   
   # >
   
   # test <
   expected = {'test' : 'update'}
   result = githubGet(
      
      pBranch = gBranch,
      pGithub = gGithub,
      pFilename = gFilename,
      pRepository = gRepository
      
   )
   assert(result == expected), 'Can retrieve existing files.'
   
   expected = 'File does not exist.'
   result = githubGet(
      
      pBranch = gBranch,
      pGithub = gGithub,
      pFilename = 'dne.json',
      pRepository = gRepository
      
   )
   assert (result == expected), 'Can detect non-existing files.'
   
   # >
   
   # deconstruct <
   githubDel(
      
      pGithub = gGithub,
      pBranch = gBranch,
      pFilename = gFilename,
      pRepository = gRepository
      
   )
   
   # >
   

def test_githubDel():
   ''' githubDel() Test Suite '''
   
   # construct <
   githubSet(
      
      isNew = True,
      pBranch = gBranch,
      pGithub = gGithub,
      pFilename = gFilename,
      pRepository = gRepository,
      pData = {'test' : 'example'}
      
   )
   
   # >
   
   # test <
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
   
   # >


# def test_requestsGet():
#    ''' requestsGet() Test Suite '''
   
#    # declare <
#    invalidLink = ''
#    txtLink = 'https://raw.githubusercontent.com/lxRbckl/lxRbckl/python/requirements.txt'
#    jsonLink = 'https://raw.githubusercontent.com/lxRbckl/Project-RCoD/main/setting.json'
#    brokenLink = 'https://raw.githubusercontent.com/lxRbckl/lxRbckl/python/test/broken.json'
   
#    # >
   
#    # test <
#    result = requestsGet(pLink = txtLink)
#    assert (type(result) == str), 'Can load .txt files.'
   
#    result = requestsGet(pLink = jsonLink)
#    assert (type(result) == dict), 'Can load .json files.'
   
#    expected = 'Invalid link.'
#    result = requestsGet(pLink = invalidLink)
#    assert (result == expected), 'Can detect invalid links.'
   
#    expected = 'Loaded data is broken.'
#    result = requestsGet(pLink = brokenLink)
#    assert (result == expected), 'Can detect broken .json data.'
   
#    # >