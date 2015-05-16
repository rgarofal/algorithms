__author__ = 'rgarofal'


def range_r(start, end, incr):
    """

    :rtype : generator
    """
    value = start
    while value < end:
        yield value
        value = value + incr


if __name__ == "__main__":
    print("My version of generator")
    for i in range_r(1, 101, 1):
        #mcm
        if i % 15 == 0:
            print('SpamEggs')
        elif i % 3 == 0:
            print('Spam')
        elif i % 5 == 0:
            print('Eggs')
        else:
            print i

