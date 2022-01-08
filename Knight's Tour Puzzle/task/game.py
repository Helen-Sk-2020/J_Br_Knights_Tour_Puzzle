class KnightTourPuzzle:
    def __init__(self):
        # starting position
        self.x = self.y = self.cell_size = 0
        
        # board settings
        self.column_n = self.row_n = 0
        self.board = []
        self.frame = self.markup = ''
        
    # determine the board's dimensions
    def board_dimensions(self):
        while True:
            dimensions = input('Enter your board dimensions:').split()
            self.check_input(dimensions)
            if self.column_n:
                break
        self.cell_size = len(str(self.column_n * self.row_n)) * '_'
        self.board = [[self.cell_size for j in range(self.column_n)] for i in range(self.row_n)]
        
    # set knight's position
    def set_position(self):
        while True:
            start = input("Enter the knight's starting position:").split()
            if self.check_input(start):
                break
        # mark starting position as "X"
        knight_position = ' ' * (len(str(self.cell_size)) - 1) + 'X'
        self.board[self.y][self.x] = knight_position
    
    def check_input(self, a):
        try:
            if len(a) != 2:
                raise IndexError
            x = int(a[0])
            y = int(a[1])
            if x < 1 or y < 1:
                raise ValueError
            
            if self.board:
                if x in range(1, self.column_n + 1) and y in range(1, self.row_n + 1):
                    self.x = x - 1
                    # self.y = len(self.board) - y
                    self.y = y - 1
                    return True

                else:
                    raise ValueError
            else:
                self.column_n = x
                self.row_n = y
                
        except (ValueError, IndexError):
            print('Invalid dimensions!')
    
    # determine the board's frame
    def board_frame(self):
        # row's length
        r_len = len(str(self.row_n))
        # cell's length
        c_len = len(str(self.cell_size))
        self.frame = f'{" " * r_len}' \
                     f'{"-" * self.column_n * (c_len + 1)}' \
                     f'{"-" * 3}'

        board_markup = []
        for i in range(1, self.column_n + 1):
            indent = ' ' * (1 + c_len - len(str(i)))
            board_markup.append(indent + str(i))
            
        self.markup = f'{" " * (r_len + 1)}{"".join(board_markup)}'
        
    # print board
    def display_board(self):
        print(self.frame)

        row = self.row_n
        while row > 0:
            for _ in self.board:
                if len(str(self.row_n)) == len(str(row)):
                    indent = ''
                else:
                    indent = ' ' * (len(str(self.row_n)) - len(str(row)))
                print(f'{indent}{row}|', *self.board[row - 1], '|')
                row -= 1
    
        print(self.frame)
        print(self.markup)
        
    # Check all 8 possible moving:
    def check_move(self):
        options = [2, 1, -2, -1, 2, -1, -2, 1, 2]
        pos_move = ' ' * (len(str(self.cell_size)) - 1) + 'O'
        n = 0
        while n < len(options):
            try:
                print(f'self.x{self.x}')
                x = self.y + options[n]
                n += 1
                y = self.x + options[n]
                if x < 0 or y < 0:
                    raise IndexError
                self.board[x][y] = pos_move
            except IndexError:
                continue
                
        print('\nHere are the possible moves:')
    
        
def main():
    game = KnightTourPuzzle()
    game.board_dimensions()
    game.set_position()
    game.check_move()
    game.board_frame()
    game.display_board()
    
    
if __name__ == "__main__":
    main()
    
 

    

            
            
            
            
    
