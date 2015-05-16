__author__ = 'rgarofal'


def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_gen():
   fn0, fn1 = 0,1
   while 1:
       yield fn0
       fn1, fn0 = fn0 + fn1, fn1
       # equivalent to
       #temp = fn1
       #fn1 = fn0 + fn1
       #fn0 = temp


def fibo_iter(N):
    num = []
    i = 1
    while i <= N:
        if i == 1 or i == 2:
            num.append(1)
        else:
            num.append(num[i-3] + num[i-2])
        i += 1
    return num


if __name__ == '__main__':
    print 'Fibonacci iterative'
    succ = fibo_iter(8)
    for g in succ:
        print g

    print 'Fibonacci Recursive'
    i= 1
    while i <= 8:
        print fibo(i)
        i += 1
    print 'Fibonacci Generator'
    succ = fibo_gen()
    #succ.next()
    for i in range(8):
        print succ.next()