import os
import random

def display_board(board):
    """
        Display the Tic Tac Toe Board on screen 

    """
    os.system("cls")
    print("\t\t**Tic Tac Toe Board**\n")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[7],board[8],board[9]))
    print("   |   |   ")
    print("--------------------")
    print("   |   |   ")
    print(" {} | {} | {}  ".format(board[4],board[5],board[6]))
    print("   |   |   ")
    print("--------------------")
    print("   |   |   ")
    print(" {} | {} | {}  ".format(board[1],board[2],board[3]))
    print("   |   |   ")
    print("\n")


def player_input():
    """
    OUTPUT : (player 1 marker, player 2 marker)
    """

    marker =""
    while not( marker =='X' or marker =='O'):
        marker = input("Player 1 choose 'X' or 'O' : ").upper()

    if marker == 'O':
        return ('O','X')
    else:
        return ('X','O')


def place_marker(board,marker,position):
    '''
    Place your marker on the board at the given position
    '''
    board[position] = marker


def win_check(board , mark):
    """
    WIN TIC TAC TOE ?

    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
    """
    Randomly choose the player who goes first
    """

    flip = random.randint(0,1)

    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    """
    Check for empty space
    """

    return board[position] == " "


def full_board_check(board):
    """
    Check for the board is full or not
    """

    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and not space_check(board,position):
        position = int(input("Choose position : (1-9) "))

    return position


def replay():
    choice = input("Do You want to play Again? Yes or No : ")
    return choice == 'Yes'
    


if __name__ == "__main__":
    print("\t\tWelcome to Tic Tac Toe Game\n")
    while True:
        the_board =[" "]*10
        player1_marker, player2_marker =player_input()

        turn =choose_first()
        print(turn, " will go first \n")
        play_game = input("Ready to play? y or n :")
        if play_game =='y':
            game_on = True
        else:
            game_on = False
        
        while game_on:
            if turn =='Player 1':
                
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player1_marker,position)
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print("PLAYER 1 WON..!!\n")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("TIE GAME")
                        game_on =False
                    else:
                        turn = 'Player 2'
            else:

                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player2_marker,position)
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("PLAYER 2  WON..!!\n")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("TIE GAME")
                        game_on =False
                    else:
                        turn = 'Player 1'
    
        if not replay():
            break
        