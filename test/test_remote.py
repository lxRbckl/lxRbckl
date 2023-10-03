# # import <
# from os import environ
# from github import (
   
#    Auth,
#    Github
   
# )

# from lxrbckl.remote import (
   
#    githubSet, 
#    githubGet,
#    githubDel,
#    requestsGet
   
# )

# # >


# # declare <
# gPyGitHubToken = environ.get('PYGITHUB')
# print(gPyGitHubToken) # remove

# gBranch = 'python'
# gFilename = 'test.json'
# gRepository = 'lxRbckl/lxrbckl'
# gGithub = Github(auth = Auth.Token(gPyGitHubToken))

# # >


# def test_githubSet():
#    ''' githubSet() Test Suite '''

#    result = githubSet(
      
#       pSleep = 3,
#       isNew = True,
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pData = {'test' : 'set'},
#       pRepository = gRepository
      
#    )

#    assert (result == None), 'Can add new files to repository.'
   
#    result = githubSet(
      
#       pSleep = 3,
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'test' : 'update'}
      
#    )

#    assert (result == None), 'Can add to existing files in repository.'
   
#    expected = 'File already exists.'
#    result = githubSet(
      
#       pSleep = 3,
#       isNew = True,
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'test' : 'update'}
      
#    )

#    assert (result == expected), 'Can detect existing files in repository.'
   
#    githubDel(
      
#       pSleep = 3,
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository
      
#    )
   
#    expected = 'File does not exist.'
#    result = githubSet(
      
#       pSleep = 3,
#       pGithub = gGithub,
#       pBranch = gBranch,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'test' : 'update'}
      
#    )
   
#    assert (result == expected), 'Can detect non-existing files in repository.'


# def test_githubGet():
#    ''' githubGet() Test Suite '''
   
#    githubSet(
      
#       pSleep = 2,
#       isNew = True,
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
      
#       pSleep = 2,
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
   

# def test_githubDel():
#    ''' githubDel() Test Suite '''
   
#    githubSet(
      
#       pSleep = 2,
#       isNew = True,
#       pBranch = gBranch,
#       pGithub = gGithub,
#       pFilename = gFilename,
#       pRepository = gRepository,
#       pData = {'test' : 'example'}
      
#    )
   
#    result = githubDel(
      
#       pSleep = 3,
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
#    ''' requestsGet() Test Suite '''
   
#    link = ''
#    expected = 'Invalid link.'
#    result = requestsGet(pLink = link)
   
#    assert (result == expected), 'Can detect invalid links.'
   
#    link = 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/main/data.json'
#    expected = 'Cannot load broken data.'
#    result = requestsGet(pLink = link)

#    assert (result == expected), 'Can detect broken .json data.'
   
#    link = 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/main/requirements.txt'
#    result = requestsGet(
      
#       pLink = link,
#       isJSON = False
      
#    )
   
#    assert (type(result) == str), 'Can load .txt files.'
   
#    link = 'https://raw.githubusercontent.com/lxRbckl/Project-RCoD/main/setting.json'
#    result = requestsGet(pLink = link)
   
#    assert (type(result) == dict), 'Can load .json files.'