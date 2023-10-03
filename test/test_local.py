# import <
import pytest

from lxrbckl.local import (
   
   fileSet,
   fileGet,
   fileDel,
   getProjectPath
   
)

# >


# declare <
gPath = getProjectPath()

# >


def test_fileSet():
   ''' fileSet() Test Suite '''

   # test <
   result = fileSet(
      
      pData = {"json" : "example"},
      pFile = f'{gPath}/test/test.json'
      
   )
   assert (result == None), 'Can establish .json files with data.'
   
   result = fileSet(
      
      pData = "this is an example",
      pFile = f'{gPath}/test/test.txt'
      
   )
   assert (result == None), 'Can establish .txt files with data.'

   result = fileSet(
      
      pData = "this is an example",
      pFile = f'${gPath}//test.txt'
      
   )
   assert (result == False), 'Can detect invalid filepaths.'

   result = fileSet(
      
      pData = {"this" : "that"},
      pFile = f'{gPath}/test/test.txt'
      
   )
   assert (result == False), 'Can detect invalid data for .txt files.'
   
   result = fileSet(
      
      pOverride = False,
      pData = 'this is an example',
      pFile = f'{gPath}/test/test.txt'
      
   )
   assert (result == False), 'Can prevent overwritten existing files.'
   
   result = fileSet(
   
      pOverride = False,
      pShowError = True,
      pData = 'this is an example',
      pFile = f'{gPath}/test/test.txt'
      
   )
   assert (type(result) == Exception), 'Can display undiagnosed errors to users.'
   
   # >
   
   # deconstruct <
   fileDel(pFile = f'{gPath}/test/test.json')
   fileDel(pFile = f'{gPath}/test/test.txt')
   
   # >


def test_fileGet():
   ''' fileGet() Test Suite '''
   
   # construct <
   fileSet(
      
      pData = 'this is a test',
      pFile = f'{gPath}/test/test.txt'
      
   )
   fileSet(
      
      pData = {'json' : 'example'},
      pFile = f'{gPath}/test/test.json'
      
   )
   
   # >

   # test <
   expected = {"json" : "example"}
   result = fileGet(pFile = f'{gPath}/test/test.json')
   assert (result == expected), 'Can load existing .json files.'
      
   expected = 'this is a test'
   result = fileGet(pFile = f'{gPath}/test/test.txt')
   assert (result == expected), 'Can load existing .txt files.'
   
   expected = 'Loaded data is broken.'
   result = fileGet(pFile = f'{gPath}/test/test.txt')
   assert (result == expected), 'Can detect broken .json data.'
   
   expected = 'File does not exist.'
   result = fileGet(pFile = f'{gPath}/test/dne.txt')
   assert (result == expected), 'Can detect non-existing files.'
   
   # >
   
   # deconstruct <
   fileDel(pFile = f'{gPath}/test/test.json')
   fileDel(pFile = f'{gPath}/test/test.txt')
   
   # >


# def test_fileDel():
#    ''' fileDel() Test Suite '''
   
#    # construct <
#    fileSet(
      
#       pData = {'test' : 'example'},
#       pFile = f'{}'
      
#    )
#    fileSet(
      
      
      
#    )
   
#    # >
   
#    # test <
#    result = fileDel(pFile = f'{gPath}/test/test.json')
#    assert (result == None), 'Can delete existing .json files.'
   
#    result = fileDel(pFile = f'{gPath}/test/test.txt')
#    assert (result == None), 'Can delete existing .txt files.'
   
#    result = fileDel(pFile = f'{gPath}/test/test.txt')
#    assert (result == False), 'Can detect non-existing files.'
   
#    # >