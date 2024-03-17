# Write your solution here
def transpose(matrix: list):
    for row in range(0, len(matrix)):
        for column in range(0, row):
            matrix[row][column], matrix[column][row]= matrix[column][row],matrix[row][column]
