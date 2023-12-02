#!/usr/bin/python3

## program to play "Connect Four"
## based on a two-dimensional list (= a list of lists)

my_board_position = [0, 0, 0, 0, 0, 0, 0]

def init_board(size):
    board = []
    for _ in range(size):
        board.append(['O'] * size)
    return board

def display_the_board(board):
    ## display the board
    size = len(board)
    for row in reversed(range(size)):
        for col in range(size):
            print(board[row][col], end="|")
        print()
    print('-------------')
    print('0|1|2|3|4|5|6|')

def score_the_board(my_board):
    size = len(my_board)
    # Check for winner in rows
    for row in range(size):
        for col in range(size - 3):
            if my_board[row][col:col + 4] == ['Y', 'Y', 'Y', 'Y']:
                print('Game over: Y is the winner. Congrats!')
                return False
            elif my_board[row][col:col + 4] == ['R', 'R', 'R', 'R']:
                print('Game over: R is the winner. Congrats!')
                return False

    # Check for winner in columns
    for col in range(size):
        for row in range(size - 3):
            if all(my_board[row + i][col] == 'Y' for i in range(4)):
                print('Game over: Y is the winner. Congrats!')
                return False
            elif all(my_board[row + i][col] == 'R' for i in range(4)):
                print('Game over: R is the winner. Congrats!')
                return False

    # Check for winner in diagonals (left down to right up)
    for col in range(size - 3):
        for row in range(size - 3):
            if all(my_board[row + i][col + i] == 'Y' for i in range(4)):
                print('Game over: Y is the winner. Congrats!')
                return False
            elif all(my_board[row + i][col + i] == 'R' for i in range(4)):
                print('Game over: R is the winner. Congrats!')
                return False

    # Check for winner in diagonals (left up to right down)
    for col in range(size - 3):
        for row in range(3, size):
            if all(my_board[row - i][col + i] == 'Y' for i in range(4)):
                print('Game over: Y is the winner. Congrats!')
                return False
            elif all(my_board[row - i][col + i] == 'R' for i in range(4)):
                print('Game over: R is the winner. Congrats!')
                return False

    return True

def game():
    size = 7
    my_board = init_board(size)
    mode = True
    while mode:
        # Yellow's turn
        col = get_player_input('YELLOW')
        if col is None: break
        row = my_board_position[col]
        my_board[row][col] = 'Y'
        display_the_board(my_board)
        my_board_position[col] += 1
        mode = score_the_board(my_board)
        if not mode: break

        # Red's turn
        col = get_player_input('RED')
        if col is None: break
        row = my_board_position[col]
        my_board[row][col] = 'R'
        display_the_board(my_board)
        my_board_position[col] += 1
        mode = score_the_board(my_board)

def get_player_input(color):
    while True:
        print(f'{color}: Please select a column (0-6) or type "stop" to quit:')
        response = input().strip()
        if response.lower() == 'stop':
            return None
        if response.isdigit():
            col = int(response)
            if 0 <= col < 7 and my_board_position[col] < 7:
                return col
            else:
                print("Invalid column or column is full. Please choose another one.")
        else:
            print("Invalid input. Please enter a number between 0 and 6.")

if __name__ == '__main__':
    game()
