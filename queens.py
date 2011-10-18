'''
********************************************************************************
****   queens.py: Implementations of the 8 queens problem stating           ****
****              that it is possible to place 8 queens on a chess          ****
****              board so that no queen can take another.                  ****
****              Converted from queen.java and coord.java.                 ****
********************************************************************************
****   Author     : Sergey Zhuravlev                                        ****
****   Java Aythor: Vic Berry                                               ****
****   Python Date: 10/12/11                                                ****
****   Java Date  : 10/11/11                                                ****
****   Course     : MET CS 664                                              ****
********************************************************************************
****   Bugs    : No known bugs.                                             ****
********************************************************************************
'''
import sys

#Constants
BOARD_SIZE = 8
MAX_QUEENS = 8
HOW_MANY   = 0

class Coord:
    '''Simple Coord Class with two attributes: row and col.
    row and col start as None and can be changed
    '''
    def __init__(self, row=None, col=None):
        self.row, self.col = row, col
    def __str__(self):
        return '(%s, %s)'%(self.row, self.col)
    def __repr__(self):
        return '<%s>'%(self)
    def __iter__(self):
        return (x for x in (self.row, self.col))
    def __eq__(self, other):
        (row_1, col_1), (row_2, col_2) = self, other
        return row_1 == row_2 and col_1 == col_2
    
def displayBoardConverted(coords, queenCount):
    '''displayBoardCoverted(coords, queenCount)-> None (Dosplays Board)
    Display the board, shows the queens in their respective positions.
    Inputs:  coords     - Array of queen coordinates.
             queenCount - Number of valid coordinates in coords.
    Outputs: None
    '''
    for row in range(BOARD_SIZE):          #current row
        #This is probably overkill, but it allows for arbitrary board sizes
        sys.stdout.write("+")
        #This section prints the first line of the board.
        for col in range(BOARD_SIZE):      #current col
            sys.stdout.write("---+")
        sys.stdout.write("\n|")
        for col in range(BOARD_SIZE):      #current col
            hasQueen = False
            for i in range(queenCount):    #queen counter
                if coords[i].row == row and coords[i].col == col:
                    hasQueen = True
                    sys.stdout.write(" Q |")
                    break                  #Can't be two here
            if not hasQueen:               #If we found no queen, print a space
                sys.stdout.write("   |")
        sys.stdout.write("\n")
    #This section prints the bottom of board
    print "+",
    for col in range(BOARD_SIZE):      #current col
        sys.stdout.write("---+")
    sys.stdout.write("\n")

def boardSafeConverted(coords, queenCount):
    '''displayBoardCoverted(coords, queenCount)-> True/False
    Determines if the current board has no two queens that can take each other.
    Inputs:  coords     - Array of queen coordinates.
             queenCount - Number of valid coordinates in coords.
    Outputs: TRUE if board is safe, FALSE otherwise.
    '''
    #Loop through the array of queens comparing the current queen againt all
    #remaining queens.  If we fail any test we exit.
    for i in range(queenCount):
        for j in range(i+1, queenCount):
            if (coords[i].row == coords[j].row):#Two in same row
                return False
            if (coords[i].col == coords[j].col):#Two in same col
                return False
            #To determine the diagonal queens we can utilize the algorithm
            #that states that if the absolute value of the rows subtracted
            #is equal to the absolute value of the columns subtracted,
            #these two queens are on a diagonal to each other.
            x = coords[i].row - coords[j].row
            y = coords[i].col - coords[j].col
            if (abs(x) == abs(y)):
                return False
    return True

def placeQueenConverted(placed, startRow, startCol, queensPlaced):
    '''placeQueenCoverted(placed, startRow, startCol, queensPlaced)-> True/False
    Solves the queens problem recursively returns True in case of success False
    otherwise.
    Inputs:  placed       - Array of queen coordinates.
             startRow     - Initial row
             startCol     - Initial col
             queensPlaced - Number of queens successfully placed.
    Outputs: TRUE in case of success, FALSE otherwise.
    '''
    global HOW_MANY
    if queensPlaced == MAX_QUEENS:
        print "%d recursions\n\n" % HOW_MANY
        return True
    for row in range(startRow, BOARD_SIZE):
        for col in range(startCol, BOARD_SIZE):
            #Make sure we do not place this one on top of another one.
            alreadyPlaced = False
            for x in range(queensPlaced):
                if ((placed[x].row == row) and (placed[x].col == col)):
                    alreadyPlaced = True
            #If we made it through we are ok to place this here */
            if not alreadyPlaced:
                placed[queensPlaced].row = row
                placed[queensPlaced].col = col
                if boardSafeConverted(placed, queensPlaced+1):
                    HOW_MANY += 1
                    if placeQueenConverted(placed, 0, 0, queensPlaced+1):
                        print row,col
                        return True
            #Somebody already lives here keep going
            else:
                break
    return False

def mainConverted():
    placed = [Coord(0,0) for count in range(MAX_QUEENS)]#array of queens placed
    placeQueenConverted(placed, 0, 0, 0)
    displayBoardConverted(placed, MAX_QUEENS)

#My pythonic versions of these functions
def displayBoard(queen_coordinates):
    '''displayBoard(array of queen coordinates)-> None (Dosplays Board)
    Display the board, shows the queens in their respective positions.
    '''
    max_x, max_y = map(max,zip(*queen_coordinates))
    board = [['   ' for row in range(max_y+1)] for col in range(max_x+1)]
    for row,col in queen_coordinates:
        if   board[row][col] == '   ': board[row][col] = ' Q '
        elif board[row][col] == ' Q ': board[row][col] = ' Qs'
    d, line = '|', '\n'+'+---'*(max_y+1)+'+\n'
    sys.stdout.write(line + line.join(d+d.join(row)+d for row in board) + line)

def boardSafe(queen_coordinates):
    '''boardSafe(array of queen coordinates)-> True/False
    Determines if the current board has no two queens that can take each other.
    '''
    num_queens = len(queen_coordinates)
    return not any(any((row_1==row_2 or
                        col_1==col_2 or
                        abs(row_1-row_2)==abs(col_1-col_2))
                       for row_1,col_1 in queen_coordinates[i+1:])
                   for i,(row_2,col_2) in enumerate(queen_coordinates))

def placeQueen(queen_coordinates, num_placed):
    '''placeQueen(array_of_placed_queens, number_remaining, countCalls)-> count
    Solves the queens problem recursively returns True in case of success False
    otherwise.
    '''
    board_size = len(queen_coordinates)
    if board_size == num_placed:
        return True
    for row in range(board_size):
        for col in range(board_size):
            new_queen = Coord(row, col)
            if new_queen in queen_coordinates:
                break
            else:
                queen_coordinates[num_placed] = new_queen
                if (  boardSafe(queen_coordinates[:num_placed+1]) and 
                      placeQueen(queen_coordinates,num_placed+1)):
                    return True
    return False

def main(num_queens):
    placed = [Coord(None,None) for count in range(num_queens)]
    placeQueen(placed, 0)
    displayBoard(placed)
