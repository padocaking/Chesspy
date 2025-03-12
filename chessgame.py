from chessboard import Chessboard

start_position:str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR QKqk - 0 0"

print_piece:dict = {
    "p": "♙",
    "P": "♟",
    "n": "♘",
    "N": "♞",
    "b": "♗",
    "B": "♝",
    "r": "♖",
    "R": "♜",
    "q": "♕",
    "Q": "♛",
    "k": "♔",
    "K": "♚",
    "": " "
}

def print_board(pos:list[str]):
    rank:int = 0
    print("  ┌────┬────┬────┬────┬────┬────┬────┬────┐")

    for i in range(15):
        if i % 2 == 0:
            full_rank:str = f"{8 - rank} | "
            for column in range(8):
                full_rank += f"{print_piece[pos[rank * 8 + column]]}  │ "
            print(full_rank)
            rank += 1
        else:
            print("  ├────┼────┼────┼────┼────┼────┼────┼────┤")

    print("  └────┴────┴────┴────┴────┴────┴────┴────┘")
    print("     A    B    C    D    E    F    G    H")

chess = Chessboard(start_position)

checkmate:bool = False


print_board(chess.get_board())
print("")

while not checkmate:
    move:str = input("Make your move: ")
    print("")
    print_board(chess.get_board())
    print("")



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