# import <
from ..module.mJSON import (
   
   jsonLoad, 
   jsonDump

)

# >


# declare <
validPath = '/Users/highlander/lxRbckl/lxrbckl/data/valid.json'
brokenPath = '/Users/highlander/lxRbckl/lxrbckl/data/broken.json'
invalidPath = '/Users/highlander/lxRbckl/lxrbckl/data/invalid.json'

# >


def test_dumpValid():
   ''' Can write objects to files. '''
   
   result = jsonDump(
      
      pData = {'this' : 'is a test'},
      pFile = '/Users/highlander/lxRbckl/lxrbckl/data/test.json'
      
   )
   
   assert (result == True)


def test_dumpInvalid():
   ''' Can detect invalid JSON structures. '''
   
   result = jsonDump(
      
      pData = {'this', 'is a test'},
      pFile = '/Users/highlander/lxRbckl/lxrbckl/data/test.json'
      
   )
   
   assert (result == False)
   

def test_loadValid1():
   ''' Can load existing JSON files. '''
   
   expected = {'test' : 'this is a test'}
   result = jsonLoad(pFile = validPath)
   
   assert (result == expected)


def test_loadInvalid1():
   ''' Can detect invalid filepaths. '''
   
   result = jsonLoad(pFile = invalidPath)
   assert (result == False)


def test_loadInvalid2():
   ''' Can detect invalid JSON structures. '''
   
   result = jsonLoad(pFile = brokenPath)
   assert (result == False)