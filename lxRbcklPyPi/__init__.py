# import <
from json import load, dump

# >


def jsonLoad(

    directory: str = None,
    fileIn: str = None,
    isNew: bool = False

):

    # if new file <
    # else then existing file <
    if (isNew):

        # initialize file <
        # reiterate <
        jsonDump(

            directory = directory,
            fileOut = fileIn,
            data = {}

        )
        jsonLoad(

            directory = directory,
            fileIn = fileIn

        )

        # >

    else:

        # get file <
        # load data <
        with open(f'{directory}/{file}', 'r') as f:

            return load(f)

        # >

    # >

def jsonDump(

    directory: str = None,
    fileOut: str = None,
    data = None,
    indent = 3

):

    # get file <
    # dump data <
    with open(f'{directory}/{fileOut}', 'w') as f:

        dump(data, f, indent)

    # >
