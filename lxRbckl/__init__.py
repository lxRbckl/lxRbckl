# import <
from json import load, dump, loads

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


def githubSet(pGithub: object, pData: dict, pRepository: str, pFile: str):
    '''  '''

    # get repository <
    # get content from file in repository <
    repository = pGithub.get_repo(pRepository)
    content = repository.get_contents(pFile)

    # >

    # update file from repository <
    repository.update_file(

        sha = content.sha,
        path = content.path,
        message = 'automated update',
        content = str(pData).replace('\'', '\"')

    )

    # >


def githubGet(pGithub: object, pRepository: str, pFile: str):
    '''  '''

    # get content from file in repository <
    content = pGithub.get_repo(pRepository).get_contents(pFile)

    # >

    # try if structured then return decoded content <
    # except then unstructured and return decoded content <
    try: return loads(content.decoded_content.decode())
    except: return dict(content.decoded_content.decode())

    # >
