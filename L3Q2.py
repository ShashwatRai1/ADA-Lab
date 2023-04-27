N=9

def crow(row,num):      #Checking we find similar number in the row
    for i in range(N):
        if (sudoku[row][i]==num):
            return 1
        return 0

def ccol(col,num):      #Checking we find similar number in the coloumn
    for i in range(N):
        if (sudoku[i][col]==num):
            return 1
        return 0
     
def box(row,col,num):    #Checking we find similar number in another row an coloumn
    x=row-row%3
    y=col-col%3
    for i in range(3):
        for j in range(3):  
            if(sudoku[i+x][j+y]==num):
                return 0
            return 1

def issafe(sudoku, row, col, num):
    crow(row,num)
    ccol(col,num)
    box(row,col,num)
    

def solveSudoku(sudoku, row, col):
    if (row==N-1 and col==N):        
        return True
    if (col == N):
        row += 1
        col = 0
    if sudoku[row][col] > 0:
        return (solveSudoku(sudoku, row, col + 1))
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