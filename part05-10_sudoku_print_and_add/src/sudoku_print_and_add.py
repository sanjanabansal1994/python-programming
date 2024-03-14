# Write your solution here
def print_sudoku(sudoku: list):
    for n in range(0,9,3):
        for i in range(n,n+3):
            for j in range(0,9):
                # print(i,j, end=" ")
                if sudoku[i][j]>0:
                    if j in [2,5,8]:
                        print(sudoku[i][j], end="  ")
                    else:
                        print(sudoku[i][j], end=" ")
                else:
                    if j in [2,5,8]:
                        print("_", end="  ")
                    else:
                        print("_",end=" ")
                # if j in [2,5,8]:
                #     print(" ")
            print(" ")
        print(" ")

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no]= number


# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# print_sudoku(sudoku)
# print(" ")
# add_number(sudoku, 2,3,5)
# print_sudoku(sudoku)

