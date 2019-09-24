
def counting_sort(arr, k):
	arr_b = [0]*(len(arr)+1)
	print(arr_b)
	new_c = [0] * (k+1)
	for j in range(len(arr)):
		new_c[arr[j]] = new_c[arr[j]] + 1

	for i in range(1, k+1):
		new_c[i] = new_c[i] + new_c[i-1]

	for j in range(len(arr)-1, -1, -1):
		arr_b[new_c[arr[j]]] = arr[j]
		new_c[arr[j]] = new_c[arr[j]] -1

	return arr_b[1:]

if __name__ == '__main__':
	list_ = [4, 0,1, 3, 2, 16, 9, 10, 14, 8, 7]
	print(list_)
	
	print(counting_sort(list_, 16))