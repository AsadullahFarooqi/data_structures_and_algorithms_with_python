import time
def peakfinding(array_):
    greatest = 0
    for i in array_:
        if i > greatest:
            greatest = i
    return greatest

def efficient_peakfinding(array_):
    mid = len(array_)//2
    greatest = array_[mid]
    if array_[mid] < array_[mid-1]:
        for i in array_[mid:]:
            if i > greatest:
                greatest = i
    else:
        for i in array_[:mid]:
            if i > greatest:
                greatest = i
    return greatest

def set_alg(array_):
    new_array = []
    for i in array_:
        if i in new_array:
            pass
        else:
            new_array.append(i)

    return new_array

long_list = [8, 2, 22, 97, 38, 15, 0, 40, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 49, 99, 17,
            81, 18, 57, 60, 87, 98, 43, 69, 48, 56, 62, 31, 73, 55, 79, 14, 29, 93, 71, 67, 53, 88,
            30, 3, 13, 36, 65, 70, 95, 23, 11, 42, 24, 68, 1, 32, 37, 16, 51, 63, 89, 41, 92, 54, 28,
            66, 33, 80, 47, 45, 44, 84, 20, 35, 64, 10, 26, 59, 94, 39, 21, 58, 96, 83, 34, 72, 9,
            76, 61, 85, 86, 19, 27, 46, 25, 82, 74, 90]

if __name__ == '__main__':

    # t1 = time.perf_counter()
    print("Brute Force peak finding :: ", peakfinding(long_list))
    # t2 = time.perf_counter()
    # print("BruteForce time :: ", t2 - t1)

    # start = time.perf_counter()
    print("efficient peak finding :: ", efficient_peakfinding(txt_form_matrix))
    # stop =  time.perf_counter()
    # print("Efficient peakfinder Time ", stop - start)

    print("Brute Force Algorithm to conv list into set\n", long_list , "\nconverted to set : ", set_alg(long_list))

    """ 2D peak finding:
    if (i,j) >= (i,j-1), (i,j+1) then (i,j) is 2D peak
    where i is row and j is the column
    """
