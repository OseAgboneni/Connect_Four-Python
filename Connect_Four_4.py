#
# 
#
# AI Player for use in Connect Four
#

import random  
from Connect_Four_3 import *

#Helper Function

class AIPlayer(Player):
    """Class for an intelligent Connect 4 Player."""

    def __init__(self, checker, tiebreak, lookahead):
        """Tiebreak is a string containing AI's tiebreak strategy 
           and lookahead is the number of steps specifying how many
           moves the player looks ahead in order to evaluate possible
           moves.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """Same repr as Player, but also indicates AI player's tiebreak
           strategy and lookahead
        """
        s = super().__repr__()
        s +=  ' (' + self.tiebreak +  ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """Takes a list scores containing a score for each column of
           the board and returns the index of the column with the
           maximum score
        """
        champ = max(scores)
        matches = []
        for elem in range(len(scores)):
            if scores[elem] == champ:
                matches += [elem]
        if self.tiebreak == "LEFT":
            return matches[0]
        elif self.tiebreak == "RIGHT":
            return matches[-1]
        else:
            return random.choice(matches)
    
    def scores_for(self, board):
        scores = [1]*board.width
        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opp.scores_for(board)
                x = max(opp_scores)
                scores[col] = 100 - x
                board.remove_checker(col)
        return scores
    def next_move(self, board):
        """Returns the AI's judgement of it best possible move"""
        scores = self.scores_for(board)
        best = self.max_score_column(scores)
        self.num_moves += 1
        return best
        
