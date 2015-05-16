__author__ = 'rgarofal'


class CountDown():

    def __init__(self, number):
        self.max = number

    def __iter__(self):
        return self

    def next(self):
        if self.max <= 0:
            raise StopIteration
        else:
            n = self.max
            self.max -= 1
        return n


if __name__ == '__main__':

    cc = CountDown(7)
    #cc.next()
    for i in cc:
        print i


