# import <
from json import dump, load

# >


def jsonLoad(

        pFile: str,
        pNew: bool = False,
        isWindows: bool = False

):
    '''  '''

    # if (new file) <
    # if (is windows) <
    # else then existing file <
    if (pNew):

        # initialize file <
        # reiterate <
        jsonDump(pFile = pFile, data = {})
        jsonLoad(pFile = pFile)

        # >

    if (isWindows): pFile = pFile.replace('/', '\\')

    else:

        # get file <
        # load data <
        with open(pFile, 'r') as f:

            return load(f)

        # >

    # >


def jsonDump(

        pData,
        pFile: str,
        pIndent: int = 3,
        isWindows: bool = False

):
    '''  '''

    # if (is windows) <
    if (isWindows): pFile = pFile.replace('/', '\\')

    # >

    # get file <
    # dump data <
    with open(pFile, 'w') as f:

        dump(pData, f)

    # >