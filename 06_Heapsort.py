"""
#################################################################
########################## Heap Sort  ###########################
#################################################################
"""

# def parent(i_index):
#     return i_index // 2

# def left_child(i_index):
#     return 2 * i_index

# def right_child(i_index):
#     return (2 * i_index) + 1

# def max_heapify(heap_, i):
#     left = left_child(i)
#     right = right_child(i)
#     largest = 0
#     # print("Left  : ", left, "\nRight : ", right, "\n\n")
#     if left <= len(heap_) and heap_[left] > heap_[i]:
#         largest = left
#     else:
#         largest = i
#     if right <= len(heap_) and heap_[right] > heap_[largest]:
#             largest = right
#     if largest != i:
#         temp = heap_[i]
#         heap_[i-1] = heap_[largest]
#         heap_[largest-1] = temp
#         max_heapify(heap_, largest)

# def build_max_heap(array_):
#     for i in range((len(array_)-1) // 2, 0, -1):
#         max_heapify(array_, i)

# def heap_sort(array_):
#     build_max_heap(array_)
#     heap_size = len(array_)
#     for i in range(heap_size, 2, -1):
#         temp = array_[0]
#         array_[i-1] = array_[0]
#         array_[0] = temp
#         heap_size -=1
#         max_heapify(array_, 1)

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

def heap_sort(array_):
    build_max_heap(array_)
    heap_size = len(array_)-1
    for i in range(heap_size, 0, -1):
        temp = array_[0]
        array_[0] = array_[i]
        array_[i] = temp
        heap_size -=1
        m = max(array_[0], array_[1])
        max_heapify(array_, array_.index(m))

# def heap_sort(array_):
#     build_max_heap(array_)
#     heap_size = len(array_)-1
#     for i in range(heap_size, 1, -1):
#         array_[i], array_[0] = array_[0], array_[i]
#         max_heapify(array_, 1)


if __name__ == '__main__':
    list_ = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("HeapSort : \n",list_)
    
    heap_sort(list_)
    print("after sort: ",list_)
