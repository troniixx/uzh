#!/usr/bin/python3

## program to play "Vier Gewinnt" (English: "Connect Four")
## based on a two-dimensional list (= a list of lists)
## by Martin Volk
## reworked by Mert Erol

size = 7

## alternative to initialize the board
my_board = []
# initialize the board
for row in range(0, size):
    for col in range (0, size):
        my_board.append = 'O'

## list of the current board position per column
my_board_position = []

# initialize the board positions
for col in range (0, size):
    my_board_position.append(0)

#################################################################
def display_the_board():
    ## display the board
    for row in reversed(range(0, size)):
        for col in range (0, size):
            print(my_board[row][col], end="|")
        print()
    print('-------------')
    print('0|1|2|3|4|5|6|')
#################################################################

def score_the_board():
    ##### find winner with 4 in row #####
    for row in range(0, size):
#       print('Test: row is', row)

        ## check for 4 times in a given row
        for col in range(0, size-3):
            
            if (my_board[row][col:col+4] == ['Y', 'Y', 'Y', 'Y']):
                print('Game over in row', row, ': Y is the winner. Congrats!')
                return 'off'
                
            elif (my_board[row][col:col+4] == ['R', 'R', 'R', 'R']):
                print('Game over in row', row, ': R is the winner. Congrats!')
                return 'off'
                
    ##### find winner with 4 in column  #####               
    for row in range(0, size-4):
        for col in range(0, size):
            if (my_board[row][col] == my_board[row+1][col] == my_board[row+2][col] == my_board[row+3][col] != 'O'):
                print('Game over in column', col, ':', my_board[row][col], 'is the winner. Congratulations!')
                return 'off'
                
    ##### find winner with 4 in diagonal: left down - right up #####
    for row in range(0, size-4):
        for col in range(0, size-4):
            if (my_board[row][col] == my_board[row+1][col+1] == my_board[row+2][col+2] == my_board[row+3][col+3] != 'O'):
                print('Game over in diagonal from', row, col, 'to', row+3, col+3, ':', my_board[row][col], 'is the winner. Well done!')
                return 'off'
                    
    ##### find winner with 4 in diagonal: left up - right down #####
    for row in range(3, size):
        for col in range(0, size-4):            
            if (my_board[row][col] == my_board[row-1][col+1] == my_board[row-2][col+2] == my_board[row-3][col+3] != 'O'):
                print('Game over in diagonal from', row, col, 'to', row-3, col+3, ':', my_board[row][col], 'is the winner. Good job!')
                return 'off'
    
    ## else: we did not find a winner
    return 'on'
    
#################################################################
## start the game


def game(mode):
    while mode == 'on':
        print('YELLOW: Please select a column (0-6)')
        response = input()

        if (response == 'stop'):
            mode = 'off'
        else:
            ## convert the input string into a number
            col = int(response)
            row = my_board_position[col]
            my_board[row][col] = 'Y'
            display_the_board()
            my_board_position[col] += 1

        mode = score_the_board()
        if mode == 'off':
            break

        print('RED: Please select a column (0-6)')
        response = input()

        if response == 'stop':
            mode = 'off'
        else:
            ## convert the input string into a number
            col = int(response)
            row = my_board_position[col]
            my_board[row][col] = 'R'
            display_the_board()
            my_board_position[col] += 1

        mode = score_the_board()

if __name__ == '__main__':
    display_the_board()
    mode = 'on'
    game(mode)
    