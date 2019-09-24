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


def quick_sort(A, low, high):
	if low < high:

		part_ = partition(A, low, high)
		
		quick_sort(A, low, part_-1)
		quick_sort(A, part_+1, high)
		# print(low, part_, high, A[low:high])

if __name__ == '__main__':
	A = [1, 2, 4, 5, 7, 1, 2, 3, 6]
	quick_sort(A, 0, len(A)-1)
	print(A)