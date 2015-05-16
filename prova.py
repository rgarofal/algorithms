__author__ = 'rgarofal'

orig = ['3\n', '1 -5 3\n', '-2 1 4\n', '5\n', '5 4 3 1 2\n', '1 1 0 1 0\n', '7\n', '677 463 -569 516 401 -998 882\n',
        '890 588 959 909 948 -617 -655\n']

if __name__ == '__main__':

    i = iter(orig)
    for val in i:
        num = int(val)
        v1 = i.next()
        v2 = i.next()
        print num
        print v1
        print v2
    print ' **** Accede con un generatore ****'
    for d in orig:
        print d

    
