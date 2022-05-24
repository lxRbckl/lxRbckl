# import <
from json import load, dump

# >


def jsonLoad(pFile: str = None, pNew: bool = False):
    '''  '''

    # if new file <
    # else then existing file <
    if (pNew):

        # initialize file <
        # reiterate <
        jsonDump(pFile = pFile, data = {})
        jsonLoad(pFile = pFile)

        # >

    else:

        # get file <
        # load data <
        with open(pFile, 'r') as f:

            return load(f)

        # >

    # >

def jsonDump(pFile: str = None, pData = None, pIndent: int = 3):
    '''  '''

    # get file <
    # dump data <
    with open(pFile, 'w') as f:

        dump(pData, f, pIndent)

    # >
