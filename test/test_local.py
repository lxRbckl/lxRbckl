# import <
from os import path
from json.decoder import JSONDecodeError

from lxrbckl.local import (
   
   fileSet,
   fileGet,
   fileDel,
   getProjectPath
   
)

# >


# declare <
gPath = path.realpath(__file__).split('/test')[0]
gFilepath = getProjectPath(pProjectName = 'lxRbckl')

# >


def test_getProjectPath():
   ''' getProjectPath() Test Suite '''

   result = getProjectPath(pProjectName = 'lxRbckl')
   assert(result == gPath), 'Can find full project path.'
   
   
def test_fileSet():
   ''' fileSet() Test Suite '''

   result = fileSet(
      
      pData = {"json" : "example"},
      pFilepath = f'{gFilepath}/test/test.json'
      
   )
   
   assert (result == None), 'Can establish .json files with data.'
   
   result = fileSet(
      
      pEnding = '.txt',
      pData = "this is an example",
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert (result == None), 'Can establish .txt files with data.'

   result = fileSet(
      
      pEnding = '.json',
      pData = "this is an example",
      pFilepath = f'${gFilepath}//test.txt'
      
   )
   
   assert (result == False), 'Can detect invalid filepaths.'

   result = fileSet(
      
      pEnding = '.txt',
      pData = {"this" : "that"},
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert (result == False), 'Can detect invalid data for .txt files.'
   
   result = fileSet(
      
      pEnding = '.txt',
      pOverride = False,
      pData = 'this is an example',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert (result == False), 'Can prevent overwritten existing files.'
   
   result = fileSet(
   
      pEnding = '.txt',
      pOverride = False,
      pShowError = True,
      pData = 'this is an example',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )

   assert (type(result) == Exception), 'Can display undiagnosed errors to users.'


def test_fileGet():
   ''' fileGet() Test Suite '''

   expected = {"json" : "example"}
   result = fileGet(pFilepath = f'{gFilepath}/test/test.json')
   
   assert (result == expected), 'Can load existing .json files.'
   
   fileSet(
      
      pData = 'this is a test',
      pEnding = '.txt',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
      
   expected = 'this is a test'
   result = fileGet(
      
      pEnding = '.txt',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert (result == expected), 'Can load existing .txt files.'
   
   result = fileGet(
      
      pEnding = '.json',
      pShowError = True,
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   assert (type(result) == JSONDecodeError), 'Can detect non-existing files.'


def test_fileDel():
   ''' fileDel() Test Suite '''
   
   result = fileDel(pFilepath = f'{gFilepath}/test/test.json')
   assert (result == None), 'Can delete existing .json files.'
   
   result = fileDel(pFilepath = f'{gFilepath}/test/test.txt')
   assert (result == None), 'Can delete existing .txt files.'
   
   result = fileDel(
      
      pShowError = True,
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   assert (type(result) == FileNotFoundError), 'Can detect non-existing files.'