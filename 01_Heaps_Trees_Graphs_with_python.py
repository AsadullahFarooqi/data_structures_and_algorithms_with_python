"""
#################################################################
############################  Heaps  ############################
#################################################################
"""
def parent(i_index):
    return i_index // 2

def left_child(i_index):
    return 2 * i_index

def right_child(i_index):
    return (2 * i_index) + 1

def max_heapify(heap_, i):
    left = left_child(i)
    right = right_child(i)
    largest = 0
    # print("Left  : ", left, "\nRight : ", right, "\n\n")
    if left <= len(heap_) and heap_[left-1] > heap_[i-1]:
        largest = left
    else:
        largest = i
    if right <= len(heap_) and heap_[right-1] > heap_[largest-1]:
            largest = right
    if largest != i:
        temp = heap_[i-1]
        heap_[i-1] = heap_[largest-1]
        heap_[largest-1] = temp
        max_heapify(heap_, largest)

def build_max_heap(array_):
    for i in range(len(array_) // 2, 0, -1):
        max_heapify(array_, i)

# list_ = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# print(list_)
# build_max_heap(list_)
# print(list_)
