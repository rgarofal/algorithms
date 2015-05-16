__author__ = 'rgarofal'
import functools
import dis
import sys

def logger(function):
    @functools.wraps(function)
    def decorator(*args, **kargs):
        print "Sto eseguendo %s" % function.func_name
        desc = ["Value = %s " % str(arg) for arg in args]
        for s in desc:
            print s
        function(*args, **kargs)
        print "Finita esecuzione"
    return decorator

@logger
def somma (a,b):
    d = a+b
    raise Exception("pluto")
    return b

if __name__ == "__main__":

    try:
        somma(1,2)
    except Exception, e:
        print "eccezione", e
        print sys.exc_info()
