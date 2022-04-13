
import random

# Function to display array as board

def display_board(game_list):
    # Clear the terminal by adding 100 "\n"
    print('\n' * 100)
    print('Here is a game board.')
    print('  |  ' + ' |  ')
    print(game_list[0] + ' | ' + game_list[1] + ' | ' + game_list[2])
    print('  |  ' + ' |  ')
    print('----------')
    print('  |  ' + ' |  ')
    print(game_list[3] + ' | ' + game_list[4] + ' | ' + game_list[5])
    print('  |  ' + ' |  ')
    print('----------')
    print('  |  ' + ' |  ')
    print(game_list[6] + ' | ' + game_list[7] + ' | ' + game_list[8])
    print('  |  ' + ' |  ')

def player_input():
    
    available_characters = ['X', 'O']
    choice = 'Wrong'
    while choice not in available_characters:
        
        choice = input('Player 1: Do you want to be "X" or "O": ')
        
        if choice not in available_characters:
            print('Such a character does not exists, you dummy :D.')
     
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def space_check(board, position):

    return board[position-1] == ' '

def full_board_check(board):

    for i in range(0, 9):
        if space_check(board, i):
            return False
    
    # Return true if board is full.
    return True

def position_choice(board):
    choice = -5
    numpad_range = range(0,10)

    while int(choice) not in numpad_range or not space_check(board, choice):
        choice = int(input('Please, make a move. Choose a number (1-9): '))

        if int(choice) not in numpad_range:
            print('Your number is not in (1, 9).')
        

    
    return int(choice)

def changed_board(board, position, player):
    board[position-1] = player

    return board 

def winner_finder(board, player):
    
    does_player_win = False

    if (board[0] == board[1] == board[2] == 'X') or (board[0] == board[1] == board[2] == 'O'):
        does_player_win = True
    elif (board[3] == board[4] == board[5] == 'X') or (board[3] == board[4] == board[5] == 'O'):
        does_player_win = True
    elif (board[6] == board[7] == board[8] == 'X') or (board[6] == board[7] == board[8] == 'O'):
        does_player_win = True
    elif (board[0] == board[4] == board[8] == 'X') or (board[0] == board[4] == board[8] == 'O'):
        does_player_win = True
    elif (board[3] == board[1] == board[6] == 'X') or (board[3] == board[1] == board[6] == 'O'):
        does_player_win = True
    elif (board[0] == board[3] == board[6] == 'X') or (board[0] == board[3] == board[6] == 'O'):
        does_player_win = True
    elif (board[1] == board[4] == board[7] == 'X') or (board[1] == board[4] == board[7] == 'O'):
        does_player_win = True
    elif (board[2] == board[5] == board[8] == 'X') or (board[2] == board[5] == board[8] == 'O'):
        does_player_win = True

    if does_player_win:
        print(f'Congratulations! {player} has won.')
        return True
    else:
        return False

def keep_playing():
    answers = ['Y', 'N']
    choice = input('Play again? Enter Yes or No.')

    return choice == 'Yes'

def random_player():

    val = random.randint(0,1)

    if val == 0:
        return 'Player_1'
    else:
        return 'Player_2'


print('Welcome to "Tic Tac Toe" game.')

while True:
    board = [' ']*10
    player_1, player_2 = player_input()

    turn = random_player()
    print(turn + ' ' + 'goes first.')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        gameon = True
    else:
        gameon = False



    while gameon:
        if turn == 'Player_1':

            display_board(board)

            position = position_choice(board)
            
            changed_board(board, position, player_1)

            if winner_finder(board, player_1):
                display_board(board)
                print('Player 1 has won!!!')
                gameon = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!')
                    gameon = False
                else:
                    turn = 'Player_2'
        else:

            display_board(board)

            position = position_choice(board)

            changed_board(board, position, player_2)

            if winner_finder(board, player_2):
                display_board(board)
                print('Player 2 has won!!!')
                gameon = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('TIE GAME!')
                    gameon = False
                else:
                    turn = 'Player_1'


    if not keep_playing():
        break





