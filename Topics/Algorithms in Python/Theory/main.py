def check_move(board, a, b):
    options = [2, 1, -2, -1, 2, -1, -2, 1, 2]
    moves = 0
    pos_move = f"{' ' * (len(str(cell_size)) - 1)}{moves}"
    n = 0
    
    while n < len(options):
        try:
            x = a + options[n]
            n += 1
            y = b + options[n]
            if x < 0 or y < 0:
                raise IndexError
            else:
                moves += 1
                if moves == 3:
                    board[x][y] = pos_move
                    print(board)
                    return x, y
                return check_move(board, x, y)
        
        except IndexError:
            continue


cell_size = '__'
my_board = [[cell_size for j in range(6)] for i in range(7)]
my_board[4][2] = ' X'
print(check_move(my_board, 4, 2))
