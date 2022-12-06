# import <
from requests import get
from json import load, dump, loads

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


def githubSet(

        pData,
        pFile: str,
        pGithub: object,
        pRepository: str,
        isNew: bool = False,
        pBranch: str = 'main',
        pMessage: str = 'Automated Update'

):
    '''  '''

    # get repository <
    # get content from repository <
    repository = pGithub.get_repo(pRepository)

    # >

    # if (is new) <
    # else (then not new) <
    if (isNew):

        # add file to repository <
        repository.create_file(

            path = pFile,
            content = pData,
            branch = pBranch,
            message = pMessage

        )

        # >

    else:

        # update file from repository <
        # get content from repository <
        content = repository.get_contents(

            path = pFile,
            ref = pBranch

        )
        repository.update_file(

            branch = pBranch,
            sha = content.sha,
            message = pMessage,
            path = content.path,
            content = str(pData).replace('\'', '\"')

        )

        # >

    # >


def githubGet(

        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main'

):
    '''  '''

    # get repository <
    # get content from repository <
    repository = pGithub.get_repo(pRepository)
    content = repository.get_contents(path = pFile, ref = pBranch)

    # >

    return loads(content.decoded_content.decode())


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
