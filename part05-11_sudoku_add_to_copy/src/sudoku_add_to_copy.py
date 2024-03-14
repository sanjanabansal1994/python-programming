# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy=[]
    for i in sudoku:
      l=[]
      for j in i:
        l.append(j)
      grid_copy.append(l)
    grid_copy[row_no][column_no]= number
    return grid_copy


# Model Solution
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
 
    new_list[row_no][column_no] = number
    return new_list