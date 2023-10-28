# import <
from source.local import (
   
   fileSet,
   fileGet,
   fileDel
   
)

# >


def test_fileSet():
   ''' fileSet() Test Suite '''

   # test <
   result = fileSet(
      
      pFile = 'test/test.json',
      pData = {"json" : "example"}
      
   )
   assert (result == None), 'Can establish .json files with data.'
   
   result = fileSet(
      
      pFile = 'test/test.txt',
      pData = "this is an example"
      
   )
   assert (result == None), 'Can establish .txt files with data.'

   expected = 'Invalid data for this filetype.'
   result = fileSet(
      
      pFile = 'test/test.txt',
      pData = {"this" : "that"}
      
   )
   assert (result == expected), 'Can detect invalid data for .txt files.'
   
   expected = 'File already exists.'
   result = fileSet(
      
      pOverride = False,
      pFile = 'test/test.txt',
      pData = 'this is an example'
      
   )
   assert (result == expected), 'Can prevent overwritten existing files.'
   
   # >
   
   # deconstruct <
   fileDel(pFile = 'test/test.json')
   fileDel(pFile = 'test/test.txt')
   
   # >


def test_fileGet():
   ''' fileGet() Test Suite '''
   
   # construct <
   fileSet(
      
      pFile = 'test/test.txt',
      pData = 'this is a test'
      
   )
   fileSet(
      
      pFile = 'test/test.json',
      pData = {'json' : 'example'}
      
   )
   
   # >

   # test <
   expected = {"json" : "example"}
   result = fileGet(pFile = 'test/test.json')
   assert (result == expected), 'Can load existing .json files.'
      
   expected = 'this is a test'
   result = fileGet(pFile = 'test/test.txt')
   assert (result == expected), 'Can load existing .txt files.'
   
   expected = 'Loaded data is broken.'
   result = fileGet(pFile = 'test/broken.json')
   assert (result == expected), 'Can detect broken .json data.'
   
   expected = 'File does not exist.'
   result = fileGet(pFile = 'test/broken.txt')
   assert (result == expected), 'Can detect non-existing files.'
   
   # >
   
   # deconstruct <
   fileDel(pFile = 'test/test.json')
   fileDel(pFile = 'test/test.txt')
   
   # >


def test_fileDel():
   ''' fileDel() Test Suite '''
   
   # construct <
   fileSet(
      
      pFile = 'test/test.json',
      pData = {'json' : 'test'}
      
   )
   fileSet(
      
      pData = 'txt test',
      pFile = 'test/test.txt'
      
   )
   
   # >
   
   # test <
   result = fileDel(pFile = 'test/test.json')
   assert (result == None), 'Can delete existing .json files.'
   
   result = fileDel(pFile = 'test/test.txt')
   assert (result == None), 'Can delete existing .txt files.'
   
   expected = 'File does not exist.'
   result = fileDel(pFile = 'test/broken.txt')
   assert (result == expected), 'Can detect non-existing files.'
   
   # >