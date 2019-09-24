def brute_force(array):
    elemets_dict = {}
    print(array)
    max_score = 0

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            s = array[i+1:j]
            sum_ = 0
            if sum(s) > max_score:
                max_score = sum(s)
                elemets_dict[i] = [array[i:j], max_score]
    print(elemets_dict)
    print(max_score)


def find_maximum_crossing_subarray(array, low, mid, high):
    left_sum = float("-inf")
    left_max = None
    temp_sum = 0
    for i in range(mid, low-1, -1):
        temp_sum += array[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            left_max  = i

    right_sum = float("-inf")
    right_max = None
    temp_sum = 0
    for i in range(mid+1, high):
        temp_sum += array[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            right_max  = i

    return left_max, right_max, left_sum+right_sum



def find_maximum_subarray(array, low, high):
    if low == high:
        return low, high, array[low]
    else:
        mid = (low+high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(array, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(array, mid+1, high)
        cross_low, cross_high, cross_sum = find_maximum_crossing_subarray(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum



def diff(array):
    ans = [0]
    for i in range(len(array)-1):
        ans.append(array[i+1]-array[i])
    # brute_force(ans)
    print(ans)
    print(find_maximum_subarray(ans, 0, len(ans)-1))

if __name__ == '__main__':
    l = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    # brute_force(l)
    diff(l)