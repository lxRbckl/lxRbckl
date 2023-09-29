# import <
from json import dumps, loads

# >


def githubSet(

        pData,
        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main',
        pMessage: str = 'Automated Commit'

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


def githubAddFile(

        pData,
        pFile: str,
        pGithub: object,
        pRepository: str,
        pBranch: str = 'main',
        pMessage: str = 'Automated Commit'

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