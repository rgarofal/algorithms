__author__ = 'rgarofal'

import random
import unittest
import spameggs_new

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.sample = 100
        self.seq = range(self.sample)
        self.v1 = 3
        self.v2 = 5
        self.new_seq = [self.v1,2*self.v1,2*self.v2, self.v1*self.v2, 1]

    def sieve(x):
        a=range(2,x+1)
        for b in range(2,int(x**0.5)+1):
            for z in a:
                if z%b==0 and z!=b:
                   a.remove(z)
        return a

    def test_shuffle_multiple_number(self):
        # make sure the shuffled sequence does not lose any elements

        out = spameggs_new.print_weird(self.new_seq, self.v1, self.v2)
        self.assertEqual(out, ['Spam', 'Spam', 'Eggs', 'SpamEggs', 1])

if __name__ == '__main__':
    unittest.main()
