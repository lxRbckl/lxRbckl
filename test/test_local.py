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
   ''' Can find full project path. '''

   result = getProjectPath(pProjectName = 'lxRbckl')
   assert(result == gPath)


def test_fileSetJSON():
   ''' Can establish .json files with information. '''
   
   result = fileSet(
      
      pData = {"json" : "example"},
      pFilepath = f'{gFilepath}/test/test.json'
      
   )
   
   assert(result == None)


def test_fileSetTXT():
   ''' Can establish .txt files with information. '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pData = "this is an example",
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert(result == None)


def test_fileSetFilepath():
   ''' Can detect invalid filepaths. '''
   
   result = fileSet(
      
      pEnding = '.json',
      pData = "this is an example",
      pFilepath = f'${gFilepath}//test.txt'
      
   )
   
   assert(result == False)
   
   
def test_fileSetData():
   ''' Can detect invalid data for .txt files. '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pData = {"this" : "that"},
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert(result == False)

   

def test_fileSetOverride():
   ''' Can prevent overwritting existing files. '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pOverride = False,
      pData = 'this is an example',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert(result == False)


def test_fileSetShowError():
   ''' Can display undiagnosed errors to user. '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pOverride = False,
      pShowError = True,
      pData = 'this is an example',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )

   assert (type(result) == Exception)
   

def test_fileGetJSON():
   ''' Can load existing .json files. '''
   
   expected = {"json" : "example"}
   result = fileGet(pFilepath = f'{gFilepath}/test/test.json')
   
   assert (result == expected)


def test_fileGetTXT():
   ''' Can load existing .txt files. '''
   
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
   assert (result == expected)


def test_fileGetShowError():
   ''' Can detect non-existing files. '''
   
   result = fileGet(
      
      pEnding = '.json',
      pShowError = True,
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   assert(type(result) == JSONDecodeError)


def test_fileDel():
   '''  '''
   
   pass


def test_fileDelShowError():
   '''  '''
   
   pass