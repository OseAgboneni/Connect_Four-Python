#
# 
#
# Playing the Game  
#

from Connect_Four_1 import Board
from Connect_Four_2 import Player
import random
import time

def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board
        #Added a sleep time to make games between RandomAI go less quickly
        
        time.sleep(2) #Stops the script for two seconds
        
        if process_move(player2, board):
            return board

        #time.sleep(2)
def process_move(player, board):
    """Processes player's move """
    s = player.__repr__()
    s += "'s turn"
    print(s)

    move = player.next_move(board)
    board.add_checker(player.checker, move)
    print()
    print(board)

    if board.is_win_for(player.checker):
        x = player.num_moves
        s = "Player " + player.checker + " wins in " + str(x) + " moves.\nCongratulations!"
        print(s)
        return True
    elif board.is_full():
        print("It's a tie! Good game!")
        return True
    else:
        return False

        
class RandomPlayer(Player):
    """Class for an unintelligent AI player"""

    def next_move(self, board):
        available = [col for col in range(board.width) if board.can_add_to(col)]
        x = random.choice(available)
        self.num_moves += 1
        return x
        
        
        
