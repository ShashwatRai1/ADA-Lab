def matrix_mult_strassen(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
    else:
        # split matrices into four quadrants
        a11, a12, a21, a22 = split_matrix(a)
        b11, b12, b21, b22 = split_matrix(b)

        # compute 7 intermediate matrices using Strassen's method
        m1 = matrix_mult_strassen(add_matrices(a11, a22), add_matrices(b11, b22))
        m2 = matrix_mult_strassen(add_matrices(a21, a22), b11)
        m3 = matrix_mult_strassen(a11, sub_matrices(b12, b22))
        m4 = matrix_mult_strassen(a22, sub_matrices(b21, b11))
        m5 = matrix_mult_strassen(add_matrices(a11, a12), b22)
        m6 = matrix_mult_strassen(sub_matrices(a21, a11), add_matrices(b11, b12))
        m7 = matrix_mult_strassen(sub_matrices(a12, a22), add_matrices(b21, b22))

        # compute quadrants of result matrix
        c11 = add_matrices(sub_matrices(add_matrices(m1, m4), m5), m7)
        c12 = add_matrices(m3, m5)
        c21 = add_matrices(m2, m4)
        c22 = add_matrices(sub_matrices(add_matrices(m1, m3), m2), m6)

        # combine quadrants into result matrix
        result = combine_matrices(c11, c12, c21, c22)
        return result


def split_matrix(m):
    n = len(m) // 2
    return m[:n], m[:n], m[n:], m[n:]

def add_matrices(a, b):
    n = len(a)
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

def sub_matrices(a, b):
    n = len(a)
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c

def combine_matrices(a11, a12, a21, a22):
    n = len(a11)
    m = [[0] * (n * 2) for i in range(n * 2)]
    for i in range(n):
        for j in range(n):
            m[i][j] = a11[i][j]
            m[i][j + n] = a12[i][j]
            m[i + n][j] = a21[i][j]
            m[i + n][j + n] = a22[i][j]
    return m

if __name__ == '__main__':
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = matrix_mult_strassen(a, b)
    print(result)
