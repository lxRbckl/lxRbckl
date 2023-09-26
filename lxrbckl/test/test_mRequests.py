# import <
from ..module.mRequests import requestsGet

# >


# declare <
linkStr = 'https://raw.githubusercontent.com/lxRbckl/lxRbckl/main/README.md'
linkInvalid = 'https://raw.githubusercontent.com/lxRbckl/Project-Heimir/main/data.json'
linkJSON = 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/main/backend/data/badge.json'

# >


def test_getValid1():
    ''' Can retrieve json formats. '''
    
    result = requestsGet(pLink = linkJSON)
    assert (result != False)
    

def test_getValid2():
    ''' Can retrieve non-json formats. '''
    
    result = requestsGet(
        
        pLink = linkStr,
        isJSON = False
        
    )
    
    assert (result != False)
    

def test_getInvalid1():
    ''' Can catch invalid load types. '''
    
    result = requestsGet(pLink = linkInvalid)
    assert (result == False)