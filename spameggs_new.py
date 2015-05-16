__author__ = 'rgarofal'
from fractions import gcd
'''
def compute_mcd(a, b):
    if b == 0:
        return a
    r = b % a
    while r != 0:
        if r == 0:
            return b
        else:
            a = b
            b = r
            r = b % a
    return r
'''

def compute_mcd(a,b):
    while b:
        a,b = b,a%b
    return a

def print_weird(n, div1, div2):
    ret = []
    for i in n:
        mcm = (div1 * div2) / gcd(div1, div2)
        if i % mcm == 0:
            print('SpamEggs')
            ret.append('SpamEggs')
        elif i % div1 == 0:
            print('Spam')
            ret.append('Spam')
        elif i % div2 == 0:
            print('Eggs')
            ret.append('Eggs')
        else:
            print i
            ret.append(i)
    return ret


if __name__ == "__main__":
    n = range(100)
    print_weird(n, 3, 5)