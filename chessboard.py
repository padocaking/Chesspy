class Chessboard:
    def __init__(self, fen):

        def fen_to_board(position):
            board:list[str] = []
            for piece in position:
                if piece.isnumeric():
                    for _ in range(int(piece)):
                        board.append("")
                else:
                    board.append(piece)
            return board
        
        fen_arr = fen.split(" ")
        
        self.pos:str = fen_arr[0].replace("/", "")
        self.castle:str = fen_arr[1]
        self.enpassant:str = fen_arr[2]
        self.no_capture:int = int(fen_arr[3])
        self.full_move:int = int(fen_arr[4])
        self.board:list[str] = fen_to_board(self.pos)

    def get_board(self):
        return self.board


#print("♙♘♗♖♕♔♚♛♜♝♞♟")
#print("")
#print("  ┌────┬────┬────┬────┬────┬────┬────┬────┐")
#print("8 │ ♖  │ ♘  │ ♗  │ ♕  │ ♔  │ ♗  │ ♘  │ ♖  │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("7 │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("6 │    │    │    │    │    │    │    │    │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("5 │    │    │    │    │    │    │    │    │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("4 │    │    │    │    │    │    │    │    │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("3 │    │    │    │    │    │    │    │    │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("2 │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │")
#print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")
#print("1 │ ♜  │ ♞  │ ♝  │ ♛  │ ♚  │ ♝  │ ♞  │ ♜  │")
#print("  └────┴────┴────┴────┴────┴────┴────┴────┘")
#print("     A    B    C    D    E    F    G    H")