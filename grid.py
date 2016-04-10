"""
    Implements a grid for playing tic-tac-toe
"""

class Grid(object):
    def __init__(self):
        self._board = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self._last_pos = 0
        self.empty_slots = [i for i in range(1,10)]

    def is_full(self):
        if len(self.empty_slots) < 1:
            return True
        else:
            return False

    def show(self):
        print ''
        for i in range(1, 10):
            (x, y) = self.__getCoordinates(i)
            print '  {0}  |'.format(self._board[x][y]),
            if i in [3, 6, 9]:
                print ''
                print '-------------------'
        print ''

    def mark(self, pos, marker):
        (x, y) = self.__getCoordinates(pos)
        # check if the slot has been already marked
        if self._board[x][y] is not '-':
            print 'Position {} already marked with {}'.format(pos, self._board[x][y])
        else:
            self._board[x][y] = marker
            self._last_pos = pos
            self.empty_slots.remove(pos)

    def clear(self):
        for i in range(1, 10):
            self.mark(i, '-')
        self._last_pos = 0
        self.empty_slots = self.empty_slots = [i for i in range(1,10)]

    def is_winner(self):
        if 0 < self._last_pos < 10:
            return self.__is_winner(self._last_pos)
        else:
            for i in range(1,10):
                return self.__is_winner(i)

    def __is_winner(self, pos):
        if pos == 1:
            return (self._board[0][0] == self._board[0][1] == self._board[0][2] != '-' or
                self._board[0][0] == self._board[1][0] == self._board[2][0] != '-'  or
                self._board[0][0] == self._board[1][1] == self._board[2][2] != '-' )
        elif pos == 2:
            return (self._board[0][1] == self._board[1][1] == self._board[2][1] != '-'  or
                self._board[0][0] == self._board[0][1] == self._board[0][2] != '-' )
        elif pos == 3:
            return (self._board[0][0] == self._board[0][1] == self._board[0][2] != '-'  or
                self._board[0][2] == self._board[1][2] == self._board[2][2] != '-'  or
                self._board[0][2] == self._board[1][1] == self._board[2][0])
        elif pos == 4:
            return (self._board[1][0] == self._board[1][1] == self._board[1][2] != '-'  or
                self._board[0][0] == self._board[1][0] == self._board[2][0] != '-' )
        elif pos == 5:
            return (self._board[0][1] == self._board[1][1] == self._board[2][1] != '-'  or
                self._board[0][0] == self._board[1][1] == self._board[2][2] != '-'  or
                self._board[0][2] == self._board[1][1] == self._board[2][0] != '-'  or
                self._board[1][0] == self._board[1][1] == self._board[1][2] != '-' )
        elif pos == 6:
            return (self._board[1][0] == self._board[1][1] == self._board[1][2] != '-'  or
                self._board[0][2] == self._board[1][2] == self._board[2][2] != '-' )
        elif pos == 7:
            return (self._board[2][0] == self._board[2][1] == self._board[2][2] != '-'  or
                self._board[2][0] == self._board[1][0] == self._board[0][0] != '-'  or
                self._board[2][0] == self._board[1][1] == self._board[0][2] != '-' )
        elif pos == 8:
            return (self._board[2][1] == self._board[1][1] == self._board[0][1] != '-'  or
                self._board[2][0] == self._board[2][1] == self._board[2][2] != '-' )
        elif pos == 9:
            return (self._board[2][2] == self._board[2][1] == self._board[2][0] != '-'  or
                self._board[2][2] == self._board[1][2] == self._board[0][2] != '-'  or
                self._board[2][2] == self._board[1][1] == self._board[0][0] != '-' )
        else:
            raise ValueError('Position in the grid must be between 1 and 9')

    def __getCoordinates(self, pos):
        """
            Givena  position in the grid returns the coordinates to point the
            matric. It returns the tuple (x, y)
        """
        if 0 < pos < 10:
            if pos == 1:
                return (0, 0)
            elif pos == 2:
                return (0, 1)
            elif pos == 3:
                return (0, 2)
            elif pos == 4:
                return (1, 0)
            elif pos == 5:
                return (1, 1)
            elif pos == 6:
                return (1, 2)
            elif pos == 7:
                return (2, 0)
            elif pos == 8:
                return (2, 1)
            elif pos == 9:
                return (2, 2)
        else:
            raise ValueError('Position in the grid must be between 1 and 9')
