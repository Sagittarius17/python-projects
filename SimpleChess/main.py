class ChessBoard:
    def __init__(self):
        # initializing an 8x8 board
        self.board = [["--" for _ in range(8)] for _ in range(8)]

        # placing pawns
        for i in range(8):
            self.board[1][i] = "BP"  # Black Pawn
            self.board[6][i] = "WP"  # White Pawn

        # placing other pieces for both players
        self.board[0] = ["BR", "BK", "BB", "BQ", "BK", "BB", "BK", "BR"]
        self.board[7] = ["WR", "WK", "WB", "WQ", "WK", "WB", "WK", "WR"]

    def display(self):
        for row in self.board:
            print(" ".join(row))

    def move_piece(self, start, end):
        # This is a naive move without any validation
        # 'start' and 'end' are tuples (row, col)
        piece = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = "--"

# Game Loop:
board = ChessBoard()

while True:
    board.display()
    move = input("Enter your move (e.g., e2 e4): ")
    try:
        start_str, end_str = move.split()
    except ValueError:
        print("Invalid input. Please enter a valid move.")
        continue

    # converting algebraic notation to row,col
    start = (8 - int(start_str[1]), ord(start_str[0]) - ord('a'))
    end = (8 - int(end_str[1]), ord(end_str[0]) - ord('a'))
    
    board.move_piece(start, end)
