def find_max_crossing_subarray(array, low, mid, high):
	left_sum = float("-inf")
	sum_ = 0
	for i in range(mid,low-1, -1):
		sum_ += array[i]
		if sum_ > left_sum:
			left_sum = sum_
			max_left = i 
	right_sum = float("-inf")
	sum_ = 0
	for j in range(mid+1,high):
		sum_ = sum_ + array[j]
		if sum_ > right_sum:
			right_sum = sum_
			max_right = j
	return (max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(array, low, high):
	if high == low:
		return (low, high, array[low])
	else:
		mid = (low+high)

if __name__ == '__main__':
	l = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

	print(find_max_crossing_subarray(l, 0, len(l)//2, len(l)))