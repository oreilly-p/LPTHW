""" Learn Python 3 The Hard Way """
from sys import argv
from os.path import exists

def playground():
    """ playground """
    from_file = argv[1]
    to_file = argv[2]

    in_file = open(from_file)
    indata = in_file.read()

    print(f"The input file is {len(indata)} bytes long")

    print(f"Does the output file exist? {exists(to_file)}")
    print("Ready, hit RETURN to continue, CTRL-C to abort.")
    input()

    out_file = open(to_file, "w")
    out_file.write(indata)

    print("All done!")

    out_file.close()
    in_file.close()

playground()
