def square_matrix_multiplication(A, B):
    length = len(A)
    C = [[0 for x in range(length)] for y in range(length)]

    for i in range(length):
        for j in range(length):
            for k in range(length):
                C[i][j] += A[i][k]*B[k][j]
    print(C)

    return C



if __name__ == '__main__':
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    square_matrix_multiplication(A, B)