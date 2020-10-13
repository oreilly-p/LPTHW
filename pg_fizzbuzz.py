""" Learn Python 3 The Hard Way """
from sys import argv

def playground():
    #Call the function in the command line followed by a number to fizzbuzz
    """ playground """

    fb_num = int(argv[1])
    fb_guess = input("Is the numbers fizzbuzz 'fizz', 'buzz', or nothing:\n")
    if_fizz = 'fizz' if fb_num % 3 == 0 else ''
    if_buzz = 'buzz' if fb_num % 5 == 0 else ''

    print('You Guesses Correctly' if fb_guess == if_fizz+if_buzz else 'You guessed incorrectly')

playground()
