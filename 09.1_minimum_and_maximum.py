
def minimum(arr):
	min_ = arr[0]
	for i in range(1, len(arr)):
		if min_ > arr[i]:
			min_ = arr[i]
	return min_

def maximum(arr):
	max_ = arr[0]
	for i in range(1, len(arr)):
		if max_ < arr[i]:
			max_ = arr[i]
	return max_

if __name__ == '__main__':
	arr = [1, 2, 4, 5, 7, 1, 2, 3, 6]
	print(arr)
	print(minimum(arr))
	print(maximum(arr))