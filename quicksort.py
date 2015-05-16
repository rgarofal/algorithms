__author__ = 'rgarofal'

#
# La complessita' e' O(N*log(N))
# Il Caso pessimo e' quadratico O(N^2)
#
#


def change(v,i,j):
    val = v[i]
    v[i] = v[j]
    v[j] = val

def QSort (v, inf, sup):
    pivot = v[(inf+sup)/2]
    i = inf
    j = sup
    while i <= j :
        while v[i] < pivot:
              i= i+1
        while v[j] > pivot:
              j=j-1
        if i<j:
           change(v,i,j)
        if i<=j:
            i=i+1
            j=j-1
        if inf < j:
            QSort(v,inf,j)
        if i < sup:
            QSort(v,i,sup)
    return v
if __name__ == "__main__":

    data = [12,34,56,7,5,6,9,10,34,66,78,1,5,13,16,76,43,56,90,123,64,39,24,78]
    data = QSort(data,0,23)
    print data