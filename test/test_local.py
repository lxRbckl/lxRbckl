# import <
from os import path
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
   '''  '''

   result = getProjectPath(pProjectName = 'lxRbckl')
   assert(result == gPath)


def test_fileSetJSON():
   '''  '''
   
   result = fileSet(
      
      pData = {"json" : "example"},
      pFilepath = f'{gFilepath}/test/test.json'
      
   )
   
   assert(result == None)


def test_fileSetTXT():
   '''  '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pData = "this is an example",
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert(result == None)


def test_fileSetFilepath():
   '''  '''
   
   result = fileSet(
      
      pEnding = '.json',
      pData = "this is an example",
      pFilepath = f'${gFilepath}//test.txt'
      
   )
   
   assert(result == False)
   
   
def test_fileSetData():
   '''  '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pData = {"this" : "that"},
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert(result == False)

   

def test_fileSetOverride():
   '''  '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pOverride = False,
      pData = 'this is an example',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )
   
   assert(result == False)


def test_fileSetShowError():
   '''  '''
   
   result = fileSet(
      
      pEnding = '.txt',
      pOverride = False,
      pShowError = True,
      pData = 'this is an example',
      pFilepath = f'{gFilepath}/test/test.txt'
      
   )

   assert (type(result) == Exception)
   

# def test_fileGet():
#    '''  '''
   
#    pass


# def test_fileDel():
#    '''  '''
   
#    pass