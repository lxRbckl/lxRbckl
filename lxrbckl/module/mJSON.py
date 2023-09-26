# import <
from re import split
from os import remove
from json import dump, load
from json.decoder import JSONDecodeError

# >


def jsonLoad(

        pFile: str,
        pDelimeter: str = '/'

):
    '''  '''
    
    # try (if file exists) <
    # except (then invalid filepath) <
    # except (then invalid JSON structure) <
    try:
    
        file = pDelimeter.join(split(r'[/\\]+', pFile))
        with open(file, 'r') as fin: return load(fin)
    
    except FileNotFoundError: return False
    except JSONDecodeError: return False
    
    # >


def jsonDump(
    
    pData,
    pFile: str,
    pIndent: int = 3,
    pDelimeter: str = '/'
    
):
    '''  '''
    
    # try (if json format) <
    # except (then invalid format) <
    try:
        
        file = pDelimeter.join(split(r'[/\\]+', pFile))
        with open(file, 'w') as fout: 
            
            dump(
                
                fp = fout,
                obj = pData, 
                indent = pIndent
                
            )
            
            return True
    
    except TypeError: return False

    # >