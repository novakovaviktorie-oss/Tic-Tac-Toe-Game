game_board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

player = 1
play_game = True
is_valid=True


def print_board():
    for row in game_board:
        print("|".join(row))

def pick_field():
    '''Asks player for a row and column and attempts to rewrite the board'''
    print("Please, choose the filed, by picking row and column (starting from 0 until 2): ")
    row_choice = int(input("Row: "))
    column_choice = int(input("Column: "))
    # chosen_field = game_board[row_choice][column_choice]
    return rewrite_field(row_choice, column_choice)

def rewrite_field(row_choice, column_choice):
    global is_valid
    if game_board[row_choice][column_choice] != '-':
        print('\nField is already filled, choose another one.')
        is_valid = False
        return False
    if player % 2 == 1:
        symbol='o'
    else:
        symbol='x'
    game_board[row_choice][column_choice]=symbol
    is_valid=True
    return True
def reset_board():
    '''Prepares for a new game'''
    global game_board
    game_board=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def play_again():
    global play_game
    global player

    restart=input('Do you want to restart the game? (Yes/No): ').lower()
    if restart=='yes':
        reset_board()
        play_game=True
        player=1
    else:
        play_game=False

def evaluate():
    global play_game
    player1='o'
    player2='x'


    winning_lines=[
        #Rows
        [game_board[0][0],game_board[0][1],game_board[0][2]],
        [game_board[1][0], game_board[1][1], game_board[1][2]],
        [game_board[2][0], game_board[2][1], game_board[2][2]],
        #Columns
        [game_board[0][0], game_board[1][0], game_board[2][0]],
        [game_board[0][1], game_board[1][1], game_board[2][1]],
        [game_board[0][2], game_board[1][2], game_board[2][2]],
        #Diagonals
        [game_board[0][0], game_board[1][1], game_board[2][2]],
        [game_board[0][2], game_board[1][1], game_board[2][0]]
    ]

    if [player1, player1, player1] in winning_lines:
        print("Player 1 wins!!")
        play_again()
        return
    if [player2,player2,player2] in winning_lines:
        print("PLayer 2 wins!!")
        play_again()
        return

    draw_check=sum(game_board,[]) #puts together a list of lists
    if '-' not in draw_check:
        print("It's a draw!")
        play_again()
        return


while play_game:
    print_board()
    if player % 2 == 1:
        print('\n\n\n--PLAYER 1----')
    else:
        print('\n\n\n--PLAYER 2----')
    is_valid=False
    while not is_valid:
        pick_field()
    evaluate()
    player+=1