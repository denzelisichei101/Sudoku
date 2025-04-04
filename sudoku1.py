'''This file is for Project 1, written by Denzel Isichei'''
def horizontal_rule_violated(row, col, value):
    """This function has three input arguments: row (integer), col 
(integer), and value(‘A’, ‘B’, ‘C’, or ‘D’). When value is entered in the 
board[row-1][col-1], if the horizontal rule is violated, this function
will return True. Otherwise, it will return False. """
    colored_value = "\x1b[0;32m" + value + "\x1b[0m"
    if value in board_input[row] or colored_value in board_input[row]:
        horizontal_rule_violated = True
    else:
        horizontal_rule_violated = False
    return horizontal_rule_violated


def vertical_rule_violated(row, col, value):
    """This function has three input arguments: row (integer), col
    (integer), and value("A", "B", "C", or D). when the letter value is
    entered in the board[row-1][col-1], if the vertical rule is violated, it
    will return True. Otherwise,it will return False."""
    colored_value = "\x1b[0;32m" + value + "\x1b[0m"
    for i in range(len(board_input)):
        if (
            value == board_input[i][col]
            or colored_value == board_input[i][col]
        ):
            vertical_rule_violated = True
            break
        else:
            vertical_rule_violated = False
    return vertical_rule_violated


def square_rule_violated(row, col, value):
    """This function has three input arguments: row (integer), col
    (integer), and value("A", "B", "C", or "D"). When the letter value is
    entered in the board[row-1][col-1], if the square rule is violated, it
    will return True. Otherwise,it will return False."""
    colored_value = "\x1b[0;32m" + value + "\x1b[0m"  # Value with color
    if row <= 1:  # If row is less than or eaual to 1
        mod1 = 0  # Let mod1 be equal to 0
        times1 = 2  # Let times1 be equal to 2
    elif row > 1:  # Else if row is greater than 1
        mod1 = 2  # Let mod1 be equal to 2
        times1 = 4  # Let times1 be equal to 4

    if col <= 1:  # If column is less than or eaual to 1
        mod2 = 0  # Let mod2 be equal to 0
        times2 = 2  # Let times2 be equal to 2
    elif col > 1:  # Else if column is greater than 1
        mod2 = 2  # Let mod2 be equal to 2
        times2 = 4  # Let times2 be equal to 4

    for i in range(mod1, times1):  # Iterate the loop of mod1 and times1
        for j in range(mod2, times2):  # Iterate the loop of mod2 and times2
            if (
                value == board_input[i][j]
                or colored_value == board_input[i][j]
            ):  # If value or colored_value is equal  to current value
                square_rule_violated = True  # Square rule violated is True
                break  # Break out of nested loop
            else:  # If value is not equal to current value
                square_rule_violated = False  # Square rule violated is True
        if square_rule_violated == True:  # If  square rule violated is True
            break  # Break out of parent loop
    return square_rule_violated  # Return square rule is violated


def all_cells_filled(board):
    """If all cells are filled in, return True. Otherwise, return False."""
    for i in range(len(board)):  # Iterate through the  length of board
        for j in range(len(board[i])):  # Iterate through length of current item in board
            if board[i][j] == " ":  # If current item is empty
                finished = False  # Board is not complete
                break  # Break out of nested loop
            else:  # If current item is not empty
                finished = True  # Board is complete
        if finished == False:  # If board is not complete
            break  # Break out of parent loop
    return finished  # Return board is complete or not

'''board = [[' ', ' ', ' ', 'B' ], [' ', 'B', ' ', ' ' ], [' ','C',' ','D' ], [' ', 'A', 'B', ' ' ]]
           [['C', ' ', ' ', 'A' ], ['A', ' ', ' ', ' ' ], [' ','A','B','C' ], [' ', ' ', ' ', ' ' ]]
           [[' ', ' ', 'A', 'B' ], ['B', ' ', ' ', ' ' ], [' ',' ',' ','D' ], ['D', 'C', ' ', ' ' ]]
           [[' ', ' ', 'C', ' ' ], ['B', 'C', ' ', ' ' ], ['A',' ',' ',' ' ], ['C', ' ', ' ', 'D' ]]
'''
def display_board(board):
    '''This function displays the 4x4 grid which is a 2-d list.'''
    r=1
    print('   1 2 3 4')

    row = 0
    for i in range(2):
        print('  +','+','+','+','+', sep='-')
        for j in range(2):
            print('{} |{} {}|{} {}|'.format(r, board[row][0], board[row][1], board[row][2], board[row][3], end=' '))
            r=r+1
            row=row+1
    print('  +','+','+','+','+', sep='-')

def board_filler(input):
    mod_user_input = (user_input.split())  # Split user's input into a list and assign to mod_user_input
    global row
    global column
    global value
    for i in range(len(mod_user_input) - 1):  # Loop through first two items in user input list
        mod_user_input[i] = (eval(mod_user_input[i]) - 1)  # Change item to integer and subtract one

    row = mod_user_input[0]  # Assign variable row to first user input
    column = mod_user_input[1]  # Assign variable column to second user input
    value = mod_user_input[2].upper()  # Assign variable value to last user input  and change to uppercase


board_input = eval(input("Enter your 2-d board (4x4): "))  # Collect 2-d list from user

display_board(board_input)  # Display user inputted 2-d board as sudoku board


while (all_cells_filled(board_input) == False):  # Run a forever loop till all the cells are filled up
    user_input = input("Type a row number, a column number, and a letter (e.g., 1 2 A):")
      # Recieve input from user; row number, column number and letter
    board_filler(user_input)    
    if (horizontal_rule_violated(row, column, value) == True):  # If horizontal rule is violated
        print(
            """
============================
Horizontal rule violated.
Do it again!
==============================================
        """ )  # Print horizontal rule violated error message
    elif (vertical_rule_violated(row, column, value) == True):  # Else if vertical rule is violated
        print(
            """
============================
Vertical rule violated.
Do it again!
==============================================
        """)  # Print vertical rule violated error message
    elif (square_rule_violated(row, column, value) == True):  # Else if square rule is violated
        print(
            """
============================
Square rule violated.
Do it again!
==============================================
        """ )  # Print square rule violated error message
    else:  # If horizontal, vertical and square rule are not violated
        Green = "\033[0;32m"  # Color Green
        original_color = "\033[0m"  # Original color to prevent other elements in terminal from turning green
        board_input[row][column] = (Green + value + original_color)  # Change user inputted value with the color green
    display_board(board_input)  # Display sudoku board using user inputted 2-d board
    # print(board_input)

print(
    """
==============================================
You solved this Sudoku! Congratulations!!!!
==============================================
    """)  # When while loop is done and all cells are filled print congratulations message.
