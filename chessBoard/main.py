
class Grid:

    def __init__(self,width,height):
        self.w = width
        self.h = height

    def create_grid(self,w,h):

        columns = []
        rows = []

        iterations = 1
        while(iterations <= w):
            columns.append(iterations)
            iterations += 1

        iterations = 1
        while(iterations <= h):
            rows.append(chr(iterations + 64))
            iterations += 1

        for alpha in rows:
            for num in columns:
                print(alpha,num,end = "   ")
            print("\n")

class Piece:

    def __init__(self, positionRow, positionColumn): #allowed_spaces, can_move_across_board):
        self.positionRow = positionRow
        self.positionColumn = positionColumn
       # self.allowed_spaces = allowed_spaces
       # self.can_move_across_board = can_move_across_board


class HorizontalMovablePiece(Piece):

    def __init__(self, positionRow, positionColumn):   # allowed_spaces, can_move_across_board):
        super().__init__(positionRow, positionColumn)  # allowed_spaces, can_move_across_board)

    def move(self,w,h):

        iterations = 1
        while(iterations <=w):
            if(iterations != self.positionColumn):
                print(chr(self.positionRow +64),iterations, '',end='')
            iterations+=1


    # def move(self, allowed_spaces,w):
    #
    #     iterations = 1
    #     while(iterations<=w):
    #         if(iterations != self.positionColumn):
    #             print(chr(self.positionRow+64),iterations)
    #         iterations+=1


class King():
    pass

def main():

    w = int(input("how wide: "))
    h = int(input("how tall: "))
    grid = Grid(w,h)
    grid.create_grid(w,h)

    row_input = int(input('row position: '))
    col_input = int(input('col position: '))
    horizontalMovableObject = HorizontalMovablePiece(row_input, col_input)
    horizontalMovableObject.move(2,w)


if __name__ == "__main__":
        main()
