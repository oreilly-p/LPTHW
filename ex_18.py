""" Learn Python 3 The Hard Way """
def playground():
    """ playground """
    def print_two(*args):
        arg1, arg2 = args
        print(f"arg1: {arg1}, arg2: {arg2}")

    def print_two_again(arg1, arg2):
        """  ex18 function """
        print(f"arg1: {arg1}, arg2: {arg2}")

    def print_one(arg1):
        print(f"arg1: {arg1}")

    def print_none():
        print('I got nothin!')

    print_two('P', 'OR')
    print_two_again('p', 'OR')
    print_one('Only one!')
    print_none()

playground()
