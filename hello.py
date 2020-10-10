from __future__ import print_function
import sys


def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'world'

<<<<<<< HEAD
def noweHello(what):
    print('New Hello, {}!'.format(what))
=======
def hello2(what):
    print(what)
>>>>>>> eb4f302b030f80fa6f06aa2d125088742643b1ba

def main():
    hello(say_what())
    return 0


if __name__ == '__main__':
    sys.exit(main())
