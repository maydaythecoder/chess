Matrix = [
    [5,4,3,2,1,3,4,5],
    [6,6,6,6,6,6,6,6],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [6,6,6,6,6,6,6,6],
    [5,4,3,2,1,3,4,5]
]

# board is represented by a matrix
#pieces are represented by numbers
#set rules to numbers to represent how the pieces move
# how do i stop pieces from capturing teammates

#PIECES
'''
pieces move
pieces capture

pawn
def move(target, IsFirst):
    if IsFirst:
        moves 2 or 1
    else
        moves forward 1

def capture(target, IsFirst, MovedTwo):
    if piece on frontDiagonal 1 square away
        able to capture
    elseif(enemy.IsFirst && MovedTwo):
        able to capture
    else unable

bishop
def move(target):
    if current position and target position unobstructed
        move allowed
    else unable

def capture(target):
    if current position and target position unobstructed
        capture allowed
    else unable

rook
def move(target):
    if current position and target position unobstructed
        move allowed
    else unable

def capture(target):
    if current position and target position unobstructed
        capture allowed
    else unable

queen
rook+bishop

king
rook+bishop capped at 1
only allow if target location isn't attacked
'''
class Pawn:
    def __init__(self, moves=None, location=None, safe=True):
        self.moves = moves if moves is not None else []
        self.location = location if location is not None else [0, 0]
        self.safe = safe

    def move(self, new_location):
        if new_location != self.location:
            self.location = new_location
            return True
        return False