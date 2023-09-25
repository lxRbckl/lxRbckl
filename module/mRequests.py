# import <
from json import loads
from requests import get

# >


def requestsGet(

        pLink: str,
        isJSON: bool = True

):
    '''  '''

    # if (.json) <
    # else (not .json) <
    if (isJSON): return loads(get(pLink).text)
    else: return get(pLink).text

    # >