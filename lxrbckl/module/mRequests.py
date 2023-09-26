# import <
from json import loads
from requests import get

# >


def requestsGet(

        pLink: str,
        isJSON: bool = True

):
    '''  '''
    
    # if (loading JSON format) <
    # else (then other format) <
    try:
        
        return {
            
            False : lambda : get(pLink).text,
            True : lambda : loads(get(pLink).text)
            
        }[isJSON]()
    
    except: return False
    
    # >