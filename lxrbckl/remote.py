# import <
from sys import stderr
from requests import get
from json import loads, dumps
from json.decoder import JSONDecodeError
from requests.exceptions import MissingSchema

# >


def githubSet(
   
   pData,
   pFilename: str,
   pGithub: object,
   pRepository: str,
   
   isNew: bool = False,
   pBranch: str = 'main'
   
):
   '''  '''
   
   # try (if permitted) <
   # except (then not permitted) <
   try:
   
      repository = pGithub.get_repo(pRepository)
      
      # if (create) <
      # elif (update) <
      if (isNew): 
      
         repository.create_file(
            
            path = pFilename,
            branch = pBranch,
            content = dumps(pData),
            message = 'Automated Set'
            
         )
      
      elif (not isNew):
         
         data = str(pData).replace('\'', '\"').replace('None', 'null')
         content = repository.get_contents(path = pFilename, ref = pBranch)
         
         repository.update_file(
            
            content = data,
            branch = pBranch,
            sha = content.sha,
            path = content.path,
            message = 'Automated Update'
            
         )
      
      # >
      
   except: return {
      
      True : 'File already exists.',
      False : 'File does not exist.'
      
   }[isNew]
   
   # >
   

def githubGet(
   
   pFilename: str,
   pGithub: object,
   pRepository: str,
   
   pBranch: str = 'main'
   
):
   '''  '''
   
   # try (if existing) <
   # except (then non-existing) <
   try:
   
      # get repository <
      # get content from repository <
      repository = pGithub.get_repo(pRepository)
      content = repository.get_contents(path = pFilename, ref = pBranch)

      # >

      return loads(content.decoded_content.decode())

   except: return 'File does not exist.'

   # >


def githubDel(
   
   pGithub,
   pFilename: str,
   pRepository: str,
   
   pBranch: str = 'main',
   pMessage: str = 'Automated Deletion'
   
):
   '''  '''
   
   # try (if existing) <
   # except (then non-existing) <
   try:
   
      repository = pGithub.get_repo(pRepository)
      file = repository.get_contents(path = pFilename, ref = pBranch)
         
      repository.delete_file(
         
         sha = file.sha,
         path = pFilename,
         branch = pBranch,
         message = pMessage
         
      )
         
   except: return 'File does not exist.'
   
   # >
   

# def requestsGet(
   
#    pLink: str,
#    pShowError: bool = False

# ):
#    '''  '''

#    # try (if valid link) <
#    # except (then invalid query) <
#    try: 
      
#       return {
      
#          'txt' : lambda : get(pLink).text,
#          'json' : lambda : loads(get(pLink).text)
         
#       }[pLink.split('.')[-1]]()
   
#    except Exception as e:
      
#       if (pShowError): 
         
#          print('Error: ', e)
#          stderr.write(f"Error: {e}\n")
#          stderr.write(f"Link: {pLink}\n")
      
#       elif (not pShowError): pass
   
#    # >


def requestsGet(pLink: str, pShowError: bool = False):
   '''  '''

   # Try to get the response and handle exceptions
   try:
      # Send the request
      response = get(pLink)
      
      # Check if the response status code is 200 (OK)
      if response.status_code != 200:
            raise Exception(f"Error: Received status code {response.status_code} from {pLink}")
      
      # Debug the response text (for checking the content)
      print(f"Response content from {pLink}: {response.text[:100]}...")  # Print the first 100 chars of the response

      # Check if the response is expected to be in JSON format
      if pLink.split('.')[-1] == 'json':
            try:
               # Try parsing the response as JSON
               return {
                  
                  'txt': lambda: response.text, 
                  'json': lambda: response.json()
                  
               }[pLink.split('.')[-1]]()
            except ValueError as e:
               # Handle JSON parsing error
               if pShowError:
                  print(f"JSON parsing error: {e}")
                  stderr.write(f"JSON parsing error: {e}\n")
               return None

      # Default to returning text if the file extension isn't .json
      return response.text

   except Exception as e:
      # Handle the exception (invalid URL, connection error, etc.)
      if pShowError:
            print(f"Error: {e}")
            stderr.write(f"Error: {e}\n")
            stderr.write(f"Link: {pLink}\n")
      elif not pShowError:
            return None
