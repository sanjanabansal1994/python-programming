# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row_cnt_list=[]
    for i in sudoku[row_no]:
        if i>0:
            row_cnt_list.append(sudoku[row_no].count(i))
    for i in row_cnt_list:
        if i>1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    l=[]
    for row in sudoku:
        if row[column_no]>0 and row[column_no] in l:
            return False
        l.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers=[]
    for i in range(row_no,(row_no+3)):
        for j in range(column_no,(column_no+3)):
            number= sudoku[i][j]
            if number>0 and number in numbers:
                return False
            numbers.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    result=[]
    for i in range(0,9):
        for j in range(0,9):
            if row_correct(sudoku, i) and column_correct(sudoku, j):
                print(i,j)
                result.append(1)
            if i in [0,3,6]and j in [0,3,6] and block_correct(sudoku, i , j):
                print(i,j)
                result.append(1)
    
    if sum(result)==90:
        return True
    else:
        return False
