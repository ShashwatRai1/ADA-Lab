N=9

def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()

def crow(row,num):
    for i in range(N):
        if (sudoku[row]==num):
            return 0
        return 1

def ccol(col,num):
    for i in range(N):
        if (sudoku[col]==num):
            return 0
        return 1
     
def box(row,col,num):
    x=row-row%3
    y=col-col%3
    for i in range(3):
        for j in range(3):  
            if(sudoku[i+x][j+y]==num):
                return 0
            return 

def issafe(sudoku,row,col,num):
    crow(row,num)
    ccol(col,num)
    box(row,col,num)


def solveSudoku(sudoku, row, col):
    if (row==N-1 and col==N):
        return True
    if col == N:
        row += 1
        col = 0
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1)
    for num in range(1, N + 1, 1):
        if issafe(sudoku, row, col, num):
            sudoku[row][col] = num
            if solveSudoku(sudoku, row, col + 1):
                return True
        sudoku[row][col] = 0
    return False
sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
if (solveSudoku(sudoku, 0, 0)):
    print(sudoku)
else:
    print("no solution  exists ")

        