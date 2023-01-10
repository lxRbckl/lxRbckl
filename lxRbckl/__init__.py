# import <
from requests import get
from json import load, dump, loads, dumps

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
        pBranch: str = 'main',
        pMessage: str = 'Automated Action'

):
    '''  '''

    # get repository <
    # get content from repository <
    repository = pGithub.get_repo(pRepository)
    content = repository.get_contents(path = pFile, ref = pBranch)

    # >

    repository.update_file(

        branch = pBranch,
        sha = content.sha,
        message = pMessage,
        path = content.path,
        content = str(pData).replace('\'', '\"').replace('None', 'null')

    )


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


def githubCreate(

        pData,
        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main',
        pMessage: str = 'Automated Action'

):
    '''  '''

    # get repository <
    repository = pGithub.get_repo(pRepository)

    # >

    repository.create_file(

        path = pFile,
        branch = pBranch,
        message = pMessage,
        content = dumps(pData)

    )


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
