""" Learn Python 3 The Hard Way """

from sys import argv

def playground():
    """ playground """

    def add(a_var, b_var):
        print(f"ADDING {a_var} + {b_var}")
        return a_var + b_var

    def subtract(a_var, b_var):
        print(f"SUBTRACTING {a_var} - {b_var}")
        return a_var - b_var

    def multiply(a_var, b_var):
        print(f"MULTIPLYING {a_var} * {b_var}")
        return a_var * b_var

    def divide(a_var, b_var):
        print(f"DIVIDING {a_var} / {b_var}")
        return a_var / b_var

    print("Let's do some math with just functions!")

    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)

    print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

    print("Here is a puzzle.")

    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

    print(f"That becomes: {what}. Can you do it by hand?")

playground()
