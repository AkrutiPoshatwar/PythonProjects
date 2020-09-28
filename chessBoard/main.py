

class Grid:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def display_grid(self,width,height):
        print_grid = []

        iterations_h = 1
        while(iterations_h <= height):
            iterations_w = 1
            while(iterations_w <= width):
                print(chr(iterations_h + 64), iterations_w, end = "   ")
                iterations_w+=1
            iterations_h+=1
            print("\n")

class Cell:

    def __init__(self, positionRow, positionColumn):
        self.positionRow = positionRow
        self.positionColumn = positionColumn

class Error(Exception):
    pass

class ValueOutOfLimit(Error):
    pass


class Piece:

    def __init__(self, cell, grid, allowed_spaces, can_move_across_board):

        if(cell.positionColumn > grid.width or cell.positionColumn < 1) or (cell.positionRow > grid.height or cell.positionRow < 1):
            raise ValueOutOfLimit
        else:
            self.grid = grid
            self.cell = cell
            self.allowed_spaces = allowed_spaces
            self.can_move_across_board = can_move_across_board

class HorizontalMovablePiece(Piece):

    def __init__(self, cell, grid, allowed_spaces, can_move_across_board):
        super().__init__(cell, grid, allowed_spaces, can_move_across_board)

    def move_horizontal(self):

        print_list = []

        if self.can_move_across_board:
            iterations = 1
            while(iterations <= self.grid.width):
                if(iterations != self.cell.positionColumn):
                    print_list.append(str(chr(self.cell.positionRow +64)+str(iterations)))
                iterations+=1
        else:
            self.check_limit((self.cell.positionRow +64 ), (self.cell.positionColumn - self.allowed_spaces), print_list)
            self.check_limit((self.cell.positionRow +64 ), (self.cell.positionColumn + self.allowed_spaces), print_list)
        return print_list

    def check_limit(self,first,second,coordinates):
        if (65 <= first <= self.grid.height + 64) and (1 <= second <= self.grid.width):
            coordinates.append(str(chr(first)) + str(second))

class VerticalMovablePiece(Piece):

    def __init__(self, cell, grid, allowed_spaces, can_move_across_board):
        super().__init__(cell, grid, allowed_spaces, can_move_across_board)

    def move_vertical(self):

        print_list = []

        if self.can_move_across_board:
            iteration=1
            while(iteration <= self.grid.height):
                if(iteration != self.cell.positionRow):
                    print_list.append(str(chr(iteration+64) + str(self.cell.positionColumn)))
                iteration+=1
        else:
            self.check_limit((self.cell.positionRow +64 - self.allowed_spaces),(self.cell.positionColumn),print_list)
            self.check_limit((self.cell.positionRow + 64 + self.allowed_spaces), (self.cell.positionColumn), print_list)

        return print_list

    def check_limit(self,first,second,coordinates):
        if (65 <= first <= self.grid.height + 64) and (1 <= second <= self.grid.width):
            coordinates.append(str(chr(first)) + str(second))

class DiagonalMovablePiece(Piece):

    def __init__(self, cell, grid, allowed_spaces, can_move_across_board):
        super().__init__(cell, grid, allowed_spaces, can_move_across_board)

    def move_diagonal(self):
        coords = []

        if self.can_move_across_board:

            row = self.cell.positionRow
            col= self.cell.positionColumn
            while 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                row -=1
                col -=1
                if 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                    coords.append((chr(row+64), col))

            row = self.cell.positionRow
            col = self.cell.positionColumn
            while 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                row += 1
                col += 1
                if 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                    coords.append((chr(row + 64), col))

            row = self.cell.positionRow
            col = self.cell.positionColumn
            while 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                row += 1
                col -= 1
                if 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                    coords.append((chr(row + 64), col))

            row = self.cell.positionRow
            col = self.cell.positionColumn
            while 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                row -= 1
                col += 1
                if 1 <= row <= self.grid.height and 1 <= col <= self.grid.width:
                    coords.append((chr(row + 64), col))

        else:
            self.AppendCheck((self.cell.positionRow - self.allowed_spaces + 64),(self.cell.positionColumn - self.allowed_spaces), coords)
            self.AppendCheck((self.cell.positionRow + self.allowed_spaces + 64),(self.cell.positionColumn + self.allowed_spaces), coords)
            self.AppendCheck((self.cell.positionRow + self.allowed_spaces + 64),(self.cell.positionColumn - self.allowed_spaces), coords)
            self.AppendCheck((self.cell.positionRow - self.allowed_spaces + 64),(self.cell.positionColumn + self.allowed_spaces), coords)

        return coords

    def AppendCheck(self, first, second,coordinates):
        if  (65 <= first <= self.grid.height + 64) and  (1 <= second <= self.grid.width):
            coordinates.append(str(chr(first))+str(second))

class Rook(HorizontalMovablePiece,VerticalMovablePiece):

    def __init__(self,cell,grid, allowed_spaces, can_move_across_board):

        HorizontalMovablePiece.__init__(self, cell, grid, allowed_spaces, can_move_across_board)
        VerticalMovablePiece.__init__(self, cell, grid, allowed_spaces, can_move_across_board)

    def move(self,horizontalMovableObject,verticalMovableObject):
        return (horizontalMovableObject.move_horizontal() + verticalMovableObject.move_vertical())

class King(HorizontalMovablePiece,VerticalMovablePiece,DiagonalMovablePiece):

    def __init__(self,cell,grid, allowed_spaces, can_move_across_board):

        HorizontalMovablePiece.__init__(self, cell, grid, allowed_spaces, can_move_across_board)
        VerticalMovablePiece.__init__(self, cell, grid, allowed_spaces, can_move_across_board)
        DiagonalMovablePiece.__init__(self, cell, grid, allowed_spaces, can_move_across_board)

    def move(self, horizontalMovableObject_k, verticalMovableObject_k, diagonalMovableObject_k ):

        return (horizontalMovableObject_k.move_horizontal() +verticalMovableObject_k.move_vertical() + diagonalMovableObject_k.move_diagonal())


def main():

    w = int(input("No of columns : "))
    h = int(input("No of rows : "))

    grid = Grid(w,h)
    grid.display_grid(w,h)

    row_input = int(input('row position: '))
    col_input = int(input('col position: '))

    cell = Cell(row_input,col_input)

    while(1):
        print('''
        ==============
        Choose piece :
        king
        rook
        exit
        ==============
        ''')

        choice = input('Enter piece name: ')

        if choice == 'rook':
            try:
                horizontalMovableObject = HorizontalMovablePiece(cell,grid,-1,True)
                verticalMovableObject = VerticalMovablePiece(cell,grid,-1,True)
                diagonalMovableObject = DiagonalMovablePiece(cell, grid, -1, True)

                obj_rook = Rook(cell,grid,-1,True)
                print(obj_rook.move(horizontalMovableObject,verticalMovableObject))
            except ValueOutOfLimit:
                print('Input position is out of chess board')

        elif choice == 'king':
            try:
                horizontalMovableObject_k = HorizontalMovablePiece(cell, grid, 1, False)
                verticalMovableObject_k = VerticalMovablePiece(cell, grid, 1, False)
                diagonalMovableObject_k = DiagonalMovablePiece(cell, grid, 1, False)

                obj_king = King(cell, grid, 1, False)
                print(obj_king.move(horizontalMovableObject_k,verticalMovableObject_k,diagonalMovableObject_k))
            except ValueOutOfLimit:
                print('Input position is out of chess board')

        elif choice == 'exit':
            exit()


if __name__ == "__main__":
        main()