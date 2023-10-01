# import <
from github import (
   
   Auth,
   Github
   
)

from lxrbckl.remote import (
   
   githubSet, 
   githubGet, 
   githubAdd,
   requestsGet
   
)

# >


# declare <
gGithubToken = ''
gGithub = Github(auth = Auth.Token(gGithubToken))

# >


def test_githubSet():
   '''  '''
   
   pass


def test_githubGet():
   '''  '''
   
   repo = gGithub.get_repo('lxRbckl/lxrbckl')
   print(repo) # remove
   branch = repo.get_branch(branch = 'python2')
   print(branch) # remove
   x = repo.get_contents('setup.py')
   print(x) # remove
   
   assert(1 == 2)
   
   # expected = None
   # result = githubGet(
      
   #    pGithub = gGithub,
   #    pBranch = 'python2',
   #    pFilename = 'test.txt',
   #    pRepository = 'lxRbckl/lxrbckl',
      
   # )
   
   # print(result) # remove
   # assert(result == expected)


def test_GithubAdd():
   '''  '''
   
   pass


def test_requestsGet():
   '''  '''
   
   pass