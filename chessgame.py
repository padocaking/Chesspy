from chessboard import Chessboard

start_position:str = "rkbqkbkr/pppppppp/8/8/8/8/PPPPPPPP/RKBQKBKR QKqk - 0 0"

chess = Chessboard(start_position)

fen_break:int = start_position.index(" ")
print(start_position[:fen_break].split("/"))

def print_board(fen_code:str):
    fen_break:int = fen_code.index(" ")
    board:list = fen_code[fen_break].split("/")

    rank:int = 0
    print("  ┌────┬────┬────┬────┬────┬────┬────┬────┐")

    for i in range(15):
        if i % 2 == 0:
            print(f"{rank} │ ♖  │ ♘  │ ♗  │ ♕  │ ♔  │ ♗  │ ♘  │ ♖  │")
            rank += 1
        else:
            print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")

    print("  └────┴────┴────┴────┴────┴────┴────┴────┘")
    print("     A    B    C    D    E    F    G    H")

print_board(start_position)

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