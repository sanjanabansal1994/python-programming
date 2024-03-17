# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x in [0,1,2] and y in [0,1,2] and game_board[y][x]=="":
        game_board[y][x]=piece
        return True
    else:
        return False

# game_board = [['X', 'O', ''], ['', '', 'O'], ['O', 'X', 'O']]
# print(play_turn(game_board, 0, 0, "X"))
# print(game_board)