# import <
from requests import get
from json import load, dump, loads

# >


def jsonLoad(

        pFile: str,
        pNew: bool = False

):
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


def jsonDump(

        pData,
        pFile: str,
        pIndent: int = 3

):
    '''  '''

    # get file <
    # dump data <
    with open(pFile, 'w') as f:

        dump(pData, f, pIndent)

    # >


def githubSet(

        pData,
        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main',
        pMessage: str = 'Automated Update'

):
    '''  '''

    # get repository <
    # get content from repository <
    repository = pGithub.get_repo(pRepository)
    content = repository.get_contents(path = pFile, ref = pBranch)

    # >

    # update file from repository <
    repository.update_file(

        branch = pBranch,
        sha = content.sha,
        message = pMessage,
        path = content.path,
        content = str(pData).replace('\'', '\"')

    )

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


def requestsGet(pLink: str): return loads(get(pLink).text)
