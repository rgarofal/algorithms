__author__ = 'rgarofal'

import itertools
import operator


def dot_product(vec1, vec2):
    return sum(itertools.imap(operator.mul, vec1, vec2))


if __name__ == '__main__':

    header_output = 'Case #%5d:   %d\n'

    # Reading the input file and open the output file
    # Fixed name of files
    #
    with open('q6.in') as file_in:
        with open('q6.out', 'w') as file_out:

            num_total_test = int(file_in.next())
            minimum = 0
            if num_total_test > 1000:
                print "The total number of test is over the maximum required = 1000"
                exit()
            for num_test in range(num_total_test):
                num_elem = int(file_in.next())
                if 8 < num_elem or 1 > num_elem:
                    print 'Case #%d: The number of vector elements exceed the limit = 8 ' % (num_test + 1)
                    file_in.next()
                    file_in.next()
                    break

                v1 = [int(x) for x in file_in.next().strip().split() if -1000 <= int(x) <= 1000]
                v2 = [int(x) for x in file_in.next().strip().split() if -1000 <= int(x) <= 1000]
                if len(v1) != num_elem or num_elem != len(v2):
                    print "Case #%d: Vector data are not between -1000 to 1000 or have different length expected %d" % (
                        (num_test + 1, num_elem))
                    break

                # not compact code
                # all_product = [dot_product(v1,vp) for vp in itertools.permutations(v2)]
                # minimum = min(all_product)

                # Functional way
                minimum = min([dot_product(v1, vp) for vp in itertools.permutations(v2)])

                file_out.writelines(header_output % ((num_test + 1), minimum))
    print "End of program"