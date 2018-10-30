"""
#################################################################
####################### Bubble sort  ############################
#################################################################
"""

def bubble_sort(array_):
    for j in range(len(array_)):
        for i in range(len(array_)-1):
            if array_[i] > array_[i+1]:
                temp = array_[i]
                array_[i] = array_[i+1]
                array_[i+1] = temp

    return array_

if __name__ == '__main__':
    print([5,2,4,6,1,3,5,3,5], "\nBubble Sort : ", bubble_sort([5,2,4,6,1,3,5,3,5]))
