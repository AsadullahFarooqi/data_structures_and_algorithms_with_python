"""
#################################################################
####################### selection sort  #########################
#################################################################
"""

def selection_sort(array_):
    for i in range(len(array_)):
        smallest = i
        j = i+1
        while j <= len(array_):
            if array_[j] < array_[smallest]:
                smallest = j
            j+=1
        temp = array_[i]
        array_[i] = array_[smallest]
        array_[smallest] = temp

    return array_

if __name__ == '__main__':    

    print([5,2,4,6,1,3], "\nselection sort : ", selection_sort([5,2,4,6,1,3]))