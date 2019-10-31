WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    row = str(WHITE + BLACK) * int(size / 2)
    board = [row if count % 2 == 0 else row[::-1] for count in range(size)]
    print(*board, sep='\n')
