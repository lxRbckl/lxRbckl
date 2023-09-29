# import <
from ..module.mFile import (
   
   setFile,
   getFile,
   delFile
   
)

# >


# declare <
validPath = '/Users/highlander/lxRbckl/lxrbckl/data/valid.txt'
brokenPath = '/Users/highlander/lxRbckl/lxrbckl/data/broken.txt'
invalidPath = '/Users/highlander/lxRbckl/lxrbckl/data/invalid.txt'

# >


def test_setValid1():
   ''' Can write objects to files. '''
   
   data = 'this is a test'
   result = setFile(
      
      pData = data,
      pFile = validPath
      
   )
   
   assert (result == True)


def test_setInvalid1():
   ''' Can detect invalid objects. '''
   
   data = {'test' : 'this is a test'}
   result = setFile(
      
      pData = data,
      pFile = brokenPath
      
   )
   
   assert (result == False)


def test_getValid1():
   ''' Can retrieve existing files. '''
   
   expected = 'this is a test'
   result = getFile(pFile = validPath)
   
   assert (result == expected)


def test_getInvalid1():
   ''' Can detect non-existing files. '''
   
   pass


def test_delValid():
   ''' Can delete existing files. '''
   
   pass


def test_delInvalid():
   ''' Can detect non-existing files. '''
   
   pass