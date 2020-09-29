

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

class CellNotInBoard(Error):
    '''Input position is outside the chess board'''

class Piece:

    def __init__(self, cell, grid, allowed_spaces, can_move_across_board):

        if(cell.positionColumn > grid.width or cell.positionColumn < 1) or (cell.positionRow > grid.height or cell.positionRow < 1):
            raise CellNotInBoard
        else:
            self.grid = grid
            self.cell = cell
            self.allowed_spaces = allowed_spaces
            self.can_move_across_board = can_move_across_board

    def _check_limit(self, first, second, coordinates):
            if (65 <= first <= self.grid.height + 64) and (1 <= second <= self.grid.width):
                coordinates.append(str(chr(first)) + str(second))

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

    def check_limit(self, first, second, coordinates):
        super()._check_limit(first, second, coordinates)

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
            self.check_limit((self.cell.positionRow + 64 - self.allowed_spaces),(self.cell.positionColumn),print_list)
            self.check_limit((self.cell.positionRow + 64 + self.allowed_spaces), (self.cell.positionColumn), print_list)

        return print_list

    def check_limit(self, first, second, coordinates):
        super()._check_limit(first, second, coordinates)


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
            self.check_limit((self.cell.positionRow - self.allowed_spaces + 64),(self.cell.positionColumn - self.allowed_spaces), coords)
            self.check_limit((self.cell.positionRow + self.allowed_spaces + 64),(self.cell.positionColumn + self.allowed_spaces), coords)
            self.check_limit((self.cell.positionRow + self.allowed_spaces + 64),(self.cell.positionColumn - self.allowed_spaces), coords)
            self.check_limit((self.cell.positionRow - self.allowed_spaces + 64),(self.cell.positionColumn + self.allowed_spaces), coords)

        return coords

    def check_limit(self, first, second, coordinates):
        super()._check_limit(first, second, coordinates)

class Rook(HorizontalMovablePiece,VerticalMovablePiece):

    def __init__(self,cell,grid, allowed_spaces, can_move_across_board):
        super().__init__(cell, grid, allowed_spaces, can_move_across_board)

    def move(self,horizontalMovableObject,verticalMovableObject):
        return (horizontalMovableObject.move_horizontal() + verticalMovableObject.move_vertical())


class King(HorizontalMovablePiece,VerticalMovablePiece,DiagonalMovablePiece):

    def __init__(self,cell,grid, allowed_spaces, can_move_across_board):
        super().__init__(cell, grid, allowed_spaces, can_move_across_board)

    def move(self, horizontalMovableObject_k, verticalMovableObject_k, diagonalMovableObject_k ):
        return (horizontalMovableObject_k.move_horizontal() +verticalMovableObject_k.move_vertical() + diagonalMovableObject_k.move_diagonal())


class AnotherKing:

    def __init__(self,cell,grid, allowed_spaces, can_move_across_board):
        self.obj_horizontal = HorizontalMovablePiece(cell, grid, allowed_spaces, can_move_across_board)
        self.obj_vertical = VerticalMovablePiece(cell, grid, allowed_spaces, can_move_across_board)
        self.obj_diagonal = DiagonalMovablePiece(cell, grid, allowed_spaces, can_move_across_board)

    def moveKing(self):
        list_king = self.obj_horizontal.move_horizontal() + self.obj_vertical.move_vertical() + self.obj_diagonal.move_diagonal()
        return list_king

class Pawn:

    def __init__(self,cell,grid, allowed_spaces, can_move_across_board):
        self.obj_vertical = VerticalMovablePiece(cell,grid, allowed_spaces, can_move_across_board)

    def move_pawn(self):
        list_pawn = []
        #list_pawn = self.obj_vertical.move_vertical()
        # for item in list_pawn:
        #     row_char=(item[:1])
        #     row_no= ord(row_char)-64

        # if(row < self.obj_vertical.grid.height/2):
        #     list_pawn.append((row+1,col))
        # if(row >=  self.obj_vertical.grid.height):
        #     list_pawn.append((row-1),col)

        row = self.obj_vertical.cell.positionRow
        col = self.obj_vertical.cell.positionColumn
        if 1 <= row <= (self.obj_vertical.grid.height/2):
            row +=1
            list_pawn.append((chr(row+64),col))

        row = self.obj_vertical.cell.positionRow
        col = self.obj_vertical.cell.positionColumn
        if (self.obj_vertical.grid.height/2) < row <= self.obj_vertical.grid.height:
            row -=1
            list_pawn.append((chr(row+64),col))

        return list_pawn


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
        kingtwo
        king
        rook
        pawn
        exit
        ==============
        ''')

        choice = input('Enter piece name: ')

        if choice == 'kingtwo':
            try:
                obj_anotherKing = AnotherKing(cell, grid, 1, False)
                print(obj_anotherKing.moveKing())
            except CellNotInBoard:
                print(CellNotInBoard.__doc__)

        elif choice == 'pawn':
            try:
                obj_pawn = Pawn(cell, grid, -1, True)
                print(obj_pawn.move_pawn())
            except CellNotInBoard:
                print(CellNotInBoard.__doc__)

        elif choice == 'rook':
            try:
                horizontalMovableObject = HorizontalMovablePiece(cell,grid,-1,True)
                verticalMovableObject = VerticalMovablePiece(cell,grid,-1,True)

                obj_rook = Rook(cell,grid,-1,True)
                print(obj_rook.move(horizontalMovableObject,verticalMovableObject))
            except CellNotInBoard:
                print(CellNotInBoard.__doc__)

        elif choice == 'king':
            try:
                horizontalMovableObject_k = HorizontalMovablePiece(cell, grid, 1, False)
                verticalMovableObject_k = VerticalMovablePiece(cell, grid, 1, False)
                diagonalMovableObject_k = DiagonalMovablePiece(cell, grid, 1, False)

                obj_king = King(cell, grid, 1, False)
                print(obj_king.move(horizontalMovableObject_k,verticalMovableObject_k,diagonalMovableObject_k))
            except CellNotInBoard:
                print(CellNotInBoard.__doc__)

        elif choice == 'exit':
            exit()

if __name__ == "__main__":
        main()