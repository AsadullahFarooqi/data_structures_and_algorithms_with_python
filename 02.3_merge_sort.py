"""
#################################################################
#########################  Merge sort  ##########################
#################################################################
"""

def merge(A,first,middle,last):
    L = A[first:middle]
    R = A[middle:last+1]

    L.append(float("inf"))
    R.append(float("inf"))

    i = j = 0
    for k in range(first, last+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, first, last):
    if first < last:
        middle = (first+last)//2
        merge_sort(A, first, middle)
        merge_sort(A, middle+1, last)
        merge(A, first, middle+1, last)


if __name__ == '__main__':
    print([5,2,4,6,1,3,5,3,5], "\nMerge sort : ", merge_sort([5,2,4,6,1,3,5,3,5]))
