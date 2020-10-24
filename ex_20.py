""" Learn Python 3 The Hard Way """

from sys import argv

def playground():
    """ playground """

    def print_all(var_file):
        print(var_file.read())

    def rewind(var_file):
        var_file.seek(0)

    def print_a_line(line_count, var_file):
        print(line_count, var_file.readline())

    current_file = open(argv[1])

    print("First let's print the whole file:")

    print_all(current_file)

    print("Now let's rewind, kind of like a tape.")

    rewind(current_file)

    print("Let's print three lines:")

    current_line = 1

    print_a_line(current_line, current_file)
    current_line += 1

    print_a_line(current_line, current_file)
    current_line += 1

    print_a_line(current_line, current_file)


playground()
