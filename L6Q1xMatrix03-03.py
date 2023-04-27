def search(mat, n, x):
    if(n == 0):
        return -1
 
    # Traverse through the matrix
    for i in range(n):
        for j in range(n):
 
            # If the element is found
            if(mat[i][j] == x):
                print("Element found at (", i, ",", j, ")")
                return 1
 
    print(" Element not found")
    return 0
 
 
# Driver code
if __name__ == "__main__":
    mat = [[-4,-3,-1,3,5],
[-3,-2,2,4,6],
[-1,1,3,5,8],
[3,4,7,8,9]]
 
    # Function call
    search(mat, 4, 3)