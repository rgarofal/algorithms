__author__ = 'rgarofal'


def change(v, i, j):
    v[i], v[j] = v[j], v[i]
    return v


def qsort(v, inf, sup):
    i = inf
    j = sup
    med = v[(inf + sup) / 2]

    while i <= j:
        while v[i] < med:
            i += 1
        while v[j] > med:
            j -= 1
        if i <= j:
            change(v, i, j)
            i += 1
            j -= 1
        if inf < j:
            qsort(v, inf, j)
        if i < sup:
            qsort(v, i, sup)
    return v

def qsort_enh(v, inf, sup):
    i = inf
    j = sup
    med = v[(inf + sup) / 2]

    while i <= j:
        while v[i] < med:
            i += 1
        while v[j] > med:
            j -= 1
        change(v, i, j)
        i += 1
        j -= 1
        if inf < j:
            qsort_enh(v, inf, j)
        if i < sup:
            qsort_enh(v, i, sup)
    return v



if __name__ == '__main__':
    v = [10, 3, 2, 0, 23, 45,0]
    data = [12,34,56,7,5,6,9,10,34,66,78,1,5,13,16,76,43,56,90,123,64,39,24,78]
    dat2 = [1, 5, 5, 6, 7, 9, 10, 12, 13, 16, 24, 34, 34, 39, 43, 56, 56, 64, 66, 76, 78, 78, 90, 123]
    v = qsort(v, 0, 6)
    data = qsort(data,0,(len(data)-1))
    dat2 = qsort(dat2,0,(len(data)-1))
    print v
    print data
    print dat2
    v = qsort_enh(v, 0, 6)
    data = qsort_enh(data,0,(len(data)-1))
    dat2 = qsort_enh(dat2,0,(len(data)-1))
    print v
    print data
    print dat2