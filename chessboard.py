class Chessboard:
    def __init__(this, fen:str):

        # Converts FEN notation to 64 length array
        def fen_to_board(position:str) -> list[str]:
            board:list[str] = []
            for piece in position:
                if piece.isnumeric():
                    for _ in range(int(piece)):
                        board.append("")
                else:
                    board.append(piece)
            return board
        
        def notation_to_index(notation:str) -> int:
            if len(notation) > 1:
                column:int = ord(notation[0].lower()) - 96
                row:int = int(notation[1])
                return 63 - row * 8 + column
            else:
                return None
        
        fen_arr = fen.split(" ")
        this.pos:str = fen_arr[0].replace("/", "")
        this.castle:str = fen_arr[1]
        this.enpassant = notation_to_index(fen_arr[2])
        this.no_capture:int = int(fen_arr[3])
        this.full_move:int = int(fen_arr[4])
        this.board:list[str] = fen_to_board(this.pos)

    def in_range(this, x:int) -> bool:
        return 0 < x < 64

    def pawn_move(this, x:int) -> list[int]:
        moves:list[int] = []
        is_white = this.board[x].isupper()

        # One square move for pawn advance
        oneSqr:int = x - 8 if is_white else x + 8
        if this.in_range(oneSqr):
            if not this.board[oneSqr]:
                moves.append(oneSqr)

                # Two square move for pawn advance
                twoSqr:int = x - 16 if is_white else x + 16
                range:list[int] = [48, 55] if is_white else [8, 15]
                if this.in_range(twoSqr):
                    if not this.board[twoSqr] and range[0] <= x <= range[1]:
                        moves.append(twoSqr)

        # Diagonals delta for pawn capturing
        diagonals:list[int] = [-7, -9]
        if not is_white: [i * -1 for i in diagonals]
        for diagonal in diagonals:
            sqr:int = x + diagonal
            if this.in_range(sqr):
                if bool(this.board[sqr]) and is_white != this.board[sqr].isupper():
                    moves.append(sqr)

        return moves

    def get_board(this):
        return this.board
    


chess = Chessboard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR QKqk - 0 0")

print(chess.pawn_move(49))

VERTICAL = 8
HORIZONTAL = 1
DIAGONAL_LR = 9
DIAGONAL_RL = 7


#┌────┬────┬────┬────┬────┬────┬────┬────┐"
#│  0 │  1 │  2 │  3 │  4 │  5 │  6 │  7 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│  8 │  9 │ 10 │ 11 │ 12 │ 13 │ 14 │ 15 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│ 16 │ 17 │ 18 │ 19 │ 20 │ 21 │ 22 │ 23 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│ 24 │ 25 │ 26 │ 27 │ 28 │ 29 │ 30 │ 31 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│ 32 │ 33 │ 34 │ 35 │ 36 │ 37 │ 38 │ 39 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│ 40 │ 41 │ 42 │ 43 │ 44 │ 45 │ 46 │ 47 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│ 48 │ 49 │ 50 │ 51 │ 52 │ 53 │ 54 │ 55 │"
#├────┼────┼────┼────┼────┼────┼────┼────┤"
#│ 56 │ 57 │ 58 │ 59 │ 60 │ 61 │ 62 │ 63 │"
#└────┴────┴────┴────┴────┴────┴────┴────┘"
