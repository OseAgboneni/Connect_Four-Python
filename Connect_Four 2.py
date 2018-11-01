#
# 
#
# Connect-Four Player class 
#

from ps10pr1 import Board


class Player:
    """A class for a Connect Four Player"""

    def __init__(self, checker):
        """Constructor that initializes a player with an X or O checker
           and a num_moves variable
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """Returns a string representation of a Player Object """
        s = "Player " + self.checker
        return s
    
    def opponent_checker(self):
        """Returns a string identification of opponent's checker """
        if self.checker == 'X':
            return 'O'
        return 'X'
    def next_move(self, board):
        """Asks Player to input which column they would like their next
           checker to be placed in
        """
        while True:
            col = int(input("Which column will you place your checker? "))
            if not board.can_add_to(col):
                print("You can't place a checker there!")
            else:
                break
        self.num_moves += 1
        return col
    
