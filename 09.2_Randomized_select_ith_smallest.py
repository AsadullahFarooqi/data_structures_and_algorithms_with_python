import random

def partition(A, low, high):
	x = A[high]
	i = low - 1
	for j in range(low, high):
		if A[j] <= x:
			i += 1
			z = A[i]
			A[i] = A[j]
			A[j] = z
	y = A[i+1]
	A[i+1] = A[high]
	A[high] = y
	return i + 1

def randomized_partition(arr, start, end):
	i = random.randint(start, end)
	temp = arr[i]
	arr[i] = arr[end]
	arr[end] = temp
	return partition(arr, start, end)

def randomized_select(arr, start, end, ith):
	if start == end:
		return arr[start]
	pivot = randomized_partition(arr, start, end)
	kth = pivot - (start+1)
	if ith == kth:
		return arr[pivot]
	elif ith < kth:
		return randomized_select(arr, start, pivot-1, ith)
	else:
		return randomized_select(arr, pivot+1, end, ith-kth)

if __name__ == '__main__':
	
	arr = [11, 22, 34, 9, 10, 8, 1, 2, 4, 5, 7, 3, 6]
	print(randomized_select(arr, 0, 12, 6))