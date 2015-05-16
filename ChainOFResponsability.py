__author__ = 'rgarofal'

import functools
class Event:
    def __init__(self):


#coroutine

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kargs):
        generator = function(*args, **kargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def handle(successor=None):
    while True:
        event = (yield)
        if event.kind == Event.MYEVENT:
            print "My Event"
        else:
            successor.send(event)

if __name__ == '__main__':

    result =
