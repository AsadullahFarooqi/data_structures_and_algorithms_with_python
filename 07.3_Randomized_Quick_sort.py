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

def randomized_quicksort(arr, start, end):
	if start < end:
		mid = randomized_partition(arr, start, end)
		randomized_quicksort(arr, start, mid-1)
		randomized_quicksort(arr, mid+1, end)

if __name__ == '__main__':
	A = [1, 2, 4, 5, 7, 1, 2, 3, 6]
	randomized_quicksort(A, 0, len(A)-1)
	print(A)