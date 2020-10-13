""" Learn Python 3 The Hard Way """
from sys import argv

def playground():
    """ playground """
    filename = argv[1]
    txt = open(filename)
    print(f"\n{filename} \n\n{txt.read()}")

    filename_var = input("\nDo you want to open another file?\n"
    "If so, please enter it now, otherwise press return: ")
    if filename_var:
        try:
            txt2 = open(filename_var)
            print(f"\n{filename_var} \n\n{txt2.read()}")
        except FileNotFoundError:
            print('\nFile not found!')


playground()
