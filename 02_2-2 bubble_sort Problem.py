"""
#################################################################
####################### Bubble sort  ############################
#################################################################
"""

def bubble_sort(array_):
    for j in range(len(array_)):
        for i in range(len(array_)-1):
            if array_[i] > array_[i+1]:
                array_[i+1], array_[i] = array_[i], array_[i+1]

    return array_


def bubble_sort_recursive(array_, l):
    if l <= 0: return array_
    for i in range(l-1):
        if array_[i] > array_[i+1]:
            array_[i+1], array_[i] = array_[i], array_[i+1]
    return bubble_sort_recursive(array_, l-1)


if __name__ == '__main__':
    a = [5,2,4,6,1,3,5,3,5]
    print(a)
    print(bubble_sort_recursive(a, len(a)))
    print("Bubble Sort : ", a)
