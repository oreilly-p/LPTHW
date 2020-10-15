""" Learn Python 3 The Hard Way """
from sys import argv
from os.path import exists

def playground():
    """ playground """

    fi = open(argv[1]);fo = open(argv[2], 'w');fo.write(fi.read());fi.close();fo.close()

playground()
