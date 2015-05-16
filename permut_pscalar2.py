__author__ = 'rgarofal'

import itertools
import operator

#
# This version read all the input file in memory and create a buffer for the output (since the output is not huge)
# and write in one shot all the result.
#
# Here the result of CProfile profiling:
#
#End of program
#         22957361 function calls in 18.792 CPU seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000   18.792   18.792 <string>:1(<module>)
#        1    3.885    3.885   18.791   18.791 permut_pscalar2.py:1(<module>)
# 11473176    5.722    0.000   14.660    0.000 permut_pscalar2.py:7(dot_product)
#        1    0.001    0.001   18.792   18.792 {execfile}
#       1    0.000    0.000    0.000    0.000 {iter}
#    2000    0.000    0.000    0.000    0.000 {len}
#     4000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2000    0.001    0.000    0.001    0.000 {method 'split' of 'str' objects}
#     2000    0.001    0.000    0.001    0.000 {method 'strip' of 'str' objects}
#        1    0.000    0.000    0.000    0.000 {method 'writelines' of 'file' objects}
#     1000    0.243    0.000    0.243    0.000 {min}
#        2    0.000    0.000    0.000    0.000 {open}
#        1    0.000    0.000    0.000    0.000 {range}
# 11473176    8.938    0.000    8.938    0.000 {sum}
#


def dot_product(vec1, vec2):
    return sum(itertools.imap(operator.mul, vec1, vec2))


if __name__ == '__main__':

    header_output = 'Case #%5d:   %d\n'

    #
    # Fixed name of files from input and output
    #

    with open('q6.in') as file_in:
        rows_output = []
        rows_input = []
        num_total_test = int(file_in.next())
        minimum = 0
        if num_total_test > 1000:
            print "The total number of test is over the maximum required = 1000"
            exit()
        # Read all the file in memory
        for rows_file in file_in:
            rows_input.append(rows_file)
        iter_buff = iter(rows_input)
        for num_test in range(num_total_test):
            num_elem = int(iter_buff.next())
            if 8 < num_elem or 1 > num_elem:
                print 'Case #%d: The number of vector elements exceed the limit = 8 ' % (num_test + 1)
                iter_buff.next()
                iter_buff.next()
                break
            v1 = [int(x) for x in iter_buff.next().strip().split() if -1000 <= int(x) <= 1000]
            v2 = [int(x) for x in iter_buff.next().strip().split() if -1000 <= int(x) <= 1000]
            if len(v1) != num_elem or num_elem != len(v2):
                print "Case #%d: Vector data are not between -1000 to 1000 or have different length expected %d" % (
                    (num_test + 1, num_elem))
                break

            # not compact code
            # all_product = [dot_product(v1,vp) for vp in itertools.permutations(v2)]
            # minimum = min(all_product)

            # Functional way
            minimum = min([dot_product(v1, vp) for vp in itertools.permutations(v2)])
            rows_output.append(header_output % ((num_test + 1), minimum))

    with open('q6.out', 'w') as file_out:
        file_out.writelines(rows_output)
    print "End of program"