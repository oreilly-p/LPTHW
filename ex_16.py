""" Learn Python 3 The Hard Way """
from sys import argv

def playground():
    """ playground """
    filename = argv[1]
    print(f"We're going to erase {filename}")
    print("If you don't want that, hit CTRL-C (^C).")
    print("If you do want that, hit RETURN.")

    input("?")

    print("Opening and truncating the file...")
    target = open(filename, 'w')

    print("Now I'm going to ask you for three lines.")

    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")

    target.write(f"{line1}\n{line2}\n{line3}\n")

    print("And finally, we close it.")
    target.close()



playground()
