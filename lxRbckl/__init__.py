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

    # try if structured content <
    # except then unstructured content <
    try:

        # get content from repository <
        # return structured content content <
        content = pGithub.get_repo(pRepository).get_contents(pFile)
        return loads(content.decoded_content.decode())

        # >

    except:

        # try if unstructured content then return content <
        # except then content does not exist then return None <
        try: return dict(content.decoded_content.decode())
        except: return None

        # >

    # >
