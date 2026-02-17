whiteKing   = '♔'
whiteQueen  = '♕'
whiteRook   = '♖'
whiteBishop = '♗'
whiteKnight = '♘'
whitePawn   = '♙'

blackKing   = '♚'
blackQueen  = '♛'
blackRook   = '♜'
blackBishop = '♝'
blackKnight = '♞'
blackPawn   = '♟'

board = [
    [blackRook, blackKnight, blackBishop, blackQueen, blackKing, blackBishop, blackKnight, blackRook],
    [blackPawn]*8,
    [' ']*8,
    [' ']*8,
    [' ']*8,
    [' ']*8,
    [whitePawn]*8,
    [whiteRook, whiteKnight, whiteBishop, whiteQueen, whiteKing, whiteBishop, whiteKnight, whiteRook]
]

def print_board():
    print("\n  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print(8 - i)
    print("  a b c d e f g h\n")


def parse_move(move):
    try:
        start, end = move.lower().split()

        if len(start) != 2 or len(end) != 2:
            return None

        col1 = ord(start[0]) - ord('a')
        row1 = 8 - int(start[1])
        col2 = ord(end[0]) - ord('a')
        row2 = 8 - int(end[1])

        if not (0 <= row1 < 8 and 0 <= col1 < 8 and
                0 <= row2 < 8 and 0 <= col2 < 8):
            return None

        return row1, col1, row2, col2
    except:
        return None


def is_white(piece):
    return piece in [whiteKing, whiteQueen, whiteRook, whiteBishop, whiteKnight, whitePawn]


def is_black(piece):
    return piece in [blackKing, blackQueen, blackRook, blackBishop, blackKnight, blackPawn]


def valid_move(r1, c1, r2, c2, turn):
    piece = board[r1][c1]
    target = board[r2][c2]

    if piece == ' ':
        return False

    if turn == "white" and not is_white(piece):
        return False
    if turn == "black" and not is_black(piece):
        return False

    if (is_white(piece) and is_white(target)) or \
       (is_black(piece) and is_black(target)):
        return False

    dr = r2 - r1
    dc = c2 - c1

    # ---------------- Pawn ----------------
    if piece == whitePawn:
        # Single move
        if dc == 0 and dr == -1 and target == ' ':
            return True
        # Double move from start
        if r1 == 6 and dc == 0 and dr == -2 and \
           board[r1-1][c1] == ' ' and target == ' ':
            return True
        # Capture
        if abs(dc) == 1 and dr == -1 and is_black(target):
            return True

    if piece == blackPawn:
        if dc == 0 and dr == 1 and target == ' ':
            return True
        if r1 == 1 and dc == 0 and dr == 2 and \
           board[r1+1][c1] == ' ' and target == ' ':
            return True
        if abs(dc) == 1 and dr == 1 and is_white(target):
            return True

    # ---------------- Rook ----------------
    if piece in [whiteRook, blackRook]:
        if r1 == r2 or c1 == c2:
            return clear_path(r1, c1, r2, c2)

    # ---------------- Bishop ----------------
    if piece in [whiteBishop, blackBishop]:
        if abs(dr) == abs(dc):
            return clear_path(r1, c1, r2, c2)

    # ---------------- Queen ----------------
    if piece in [whiteQueen, blackQueen]:
        if r1 == r2 or c1 == c2 or abs(dr) == abs(dc):
            return clear_path(r1, c1, r2, c2)

    # ---------------- Knight ----------------
    if piece in [whiteKnight, blackKnight]:
        if (abs(dr), abs(dc)) in [(2,1),(1,2)]:
            return True

    # ---------------- King ----------------
    if piece in [whiteKing, blackKing]:
        if max(abs(dr), abs(dc)) == 1:
            return True

    return False


def clear_path(r1, c1, r2, c2):
    dr = (r2 - r1)
    dc = (c2 - c1)

    step_r = (dr > 0) - (dr < 0)
    step_c = (dc > 0) - (dc < 0)

    r, c = r1 + step_r, c1 + step_c
    while (r, c) != (r2, c2):
        if board[r][c] != ' ':
            return False
        r += step_r
        c += step_c

    return True


turn = "white"

while True:
    print_board()
    move = input(f"{turn.capitalize()} move (e2 e4) or 'quit': ")

    if move == "quit":
        break

    parsed = parse_move(move)
    if not parsed:
        print("Invalid format.")
        continue

    r1, c1, r2, c2 = parsed

    if valid_move(r1, c1, r2, c2, turn):
        board[r2][c2] = board[r1][c1]
        board[r1][c1] = ' '
        turn = "black" if turn == "white" else "white"
    else:
        print("Invalid move.")
