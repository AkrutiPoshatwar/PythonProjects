
class Grid:

    numToAlpha = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h"
    }

    alphaToNum = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }

    w = int(input("how wide: "))
    h = int(input("how tall: "))

    columns = []
    rows = []

    iterations = 1
    while(iterations <= w):
        columns.append(iterations)
        iterations += 1

    iterations = 1
    while(iterations <= h):
        rows.append(numToAlpha[iterations])
        iterations += 1

    for alpha in rows:
        for num in columns:
            print(alpha,num,end = "   ")
        print("\n")


grid = Grid()

class Piece:

    def __init__(self, positionRow, positionColumn): #allowed_spaces, can_move_across_board):
        self.positionRow = positionRow
        self.positionColumn = positionColumn
       # self.allowed_spaces = allowed_spaces
       # self.can_move_across_board = can_move_across_board


class HorizontalMovablePiece(Piece):

    def __init__(self, positionRow, positionColumn):   # allowed_spaces, can_move_across_board):
        super().__init__(positionRow, positionColumn)  # allowed_spaces, can_move_across_board)


    def move(self):
        iterations = 1
        while(iterations <= grid.w):
            if(iterations != self.positionColumn):
                print(grid.numToAlpha[self.positionRow],iterations)
            iterations+=1


row_input = int(input('row position: '))
col_input = int(input('col position: '))

horizontalMovableObject = HorizontalMovablePiece(row_input,col_input)
horizontalMovableObject.move()


