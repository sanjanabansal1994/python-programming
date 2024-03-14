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

