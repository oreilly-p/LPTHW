""" Learn Python 3 The Hard Way """

def playground():
    """ playground """

    types_of_people = 10

    statement1 = f"There are {types_of_people} types of people."

    binary = "binary"
    do_not = "don't"
    statement2 = f"Those who know {binary} and those who {do_not}"

    print(statement1)
    print(statement1 + statement2 + '1')
    print(statement2)

    print(f"I said: {statement1}")
    print(f"I also said: {statement2}")

    hilarious = False
    joke_evaluation = "Isn't that joke so funny?! {}"

    print(joke_evaluation.format(hilarious))

    left_string = "This is the left side of..."
    right_string = "a string with a right side!"

    print(left_string + right_string)

playground()
