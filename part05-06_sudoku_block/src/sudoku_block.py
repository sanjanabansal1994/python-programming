# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers=[]
    for i in range(row_no,(row_no+3)):
        for j in range(column_no,(column_no+3)):
            number= sudoku[i][j]
            if number>0 and number in numbers:
                return False
            numbers.append(number)
    return True
