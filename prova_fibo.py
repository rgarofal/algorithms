__author__ = 'rgarofal'

def fibo():
    fn0=0
    fn1=1
    while True:
        yield fn0
        temp = fn1
        fn1 = fn0+fn1
        fn0 = temp


if __name__ == "__main__":
    it = fibo()
    it.next()
    for i in range(5):
        print it.next()

    ff = fibo()
    ff.next()
    for i in range(8):
        value = next(ff)
        print value
    for i in range(8):
        print i