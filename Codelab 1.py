def create_board(width, height):
    board = [[' ' for _ in range(width)] for _ in range(height)]

    pattern = ['X', 'O']

    for i in range(height):
        for j in range(width):
            board[i][j] = pattern[(i + j) % 2]

    return board

rauls = create_board(3,3)
print(rauls)