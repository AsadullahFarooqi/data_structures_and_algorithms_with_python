"""
#################################################################
######################  insertion_sort  #########################
#################################################################
"""
def insertion_sort(array_):
    for j in range(1, len(array_)):
        key = array_[j]
        i = j -1
        while i > - 1 and array_[i] > key:
            array_[i + 1] = array_[i]
            i = i - 1
        array_[i+1] = key

    return array_

if __name__ == '__main__':
	print([5,2,4,6,1,3], "\ninsertion sort : ", insertion_sort([5,2,4,6,1,3]))