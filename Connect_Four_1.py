#Ose Agboneni


class Board:
    """ Class for a board representing one used in the game Connect Four """


    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(height)]


    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Hyphens at the bottom of the board and the numbers underneath it.

        for x in range(self.width):
            s += '--'

        s += '-\n'

        for y in range(self.width):
            s += ' ' + str(y)
            
        return s
    def add_checker(self, checker, col):
        """ Adds a 'X' or 'O' checker in the indicated column
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        for r in range(self.height):
            if r == self.height-1:
                self.slots[r][col] = checker
                break
            elif self.slots[r+1][col] != ' ':
                self.slots[r][col] = checker
                break
    def reset(self):
        """ resets all slots to a blank space """
        self.slots = [[' '] * self.width for row in range(self.height)]
        #Is this the simpler way mentioned? Simply making a new reference to an empty 2-D list?

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

                
    def can_add_to(self, col):
        """Returns True if it is valid to place a checker in the column col
           col on the calling Board object. Returns False otherwise.
        """
        return 0 <= col < self.width and self.slots[0][col] == ' '


    def is_full(self):
        """ Returns True if the called Board object is completely full """
        for c in range(self.width):
            if self.can_add_to(c):
                return False
        return True

    def remove_checker(self, col):
        """Removes the top checker from indicated column """
        if self.slots[self.height-1][col] == ' ':
            return
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                break
    ##~~~~~~~~~~~~~~~Helper Functions for is_win_for~~~~~~~~~~~~~


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a downwards diagonal win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for an upwards diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False

    ##~~~~~is_win_for Function~~~~~##
    def is_win_for(self, checker):
        """Returns True if there are four consecutive slots containing the
           checker parameter on the board. """
        assert(checker == 'X' or checker == 'O')
        
        #Storing calls in variables to make return statement easier to read
        h = self.is_horizontal_win(checker)
        v = self.is_vertical_win(checker)
        dd = self.is_down_diagonal_win(checker)
        du = self.is_up_diagonal_win(checker)

        return h or v or dd or du
