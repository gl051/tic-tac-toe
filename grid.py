"""
    Implements a grid for playing tic-tac-toe
"""

class Grid(object):
    def __init__(self):
        self.__board = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.__last_pos = 0
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
            print '  {0}  |'.format(self.__board[x][y]),
            if i in [3, 6, 9]:
                print ''
                print '-------------------'
        print ''

    def mark(self, pos, marker):
        (x, y) = self.__getCoordinates(pos)
        # check if the slot has been already marked
        if self.__board[x][y] is not '-':
            print 'Position {} already marked with {}'.format(pos, self.__board[x][y])
        else:
            self.__board[x][y] = marker
            self.__last_pos = pos
            self.empty_slots.remove(pos)

    def clear(self):
        for i in range(1, 10):
            self.mark(i, '-')
        self.__last_pos = 0
        self.empty_slots = self.empty_slots = [i for i in range(1,10)]

    def is_winner(self):
        if 0 < self.__last_pos < 10:
            return self.__is_winner(self.__last_pos)
        else:
            for i in range(1,10):
                return self.__is_winner(i)

    def __is_winner(self, pos):
        if pos == 1:
            return (self.__board[0][0] == self.__board[0][1] == self.__board[0][2] != '-' or
                self.__board[0][0] == self.__board[1][0] == self.__board[2][0] != '-'  or
                self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != '-' )
        elif pos == 2:
            return (self.__board[0][1] == self.__board[1][1] == self.__board[2][1] != '-'  or
                self.__board[0][0] == self.__board[0][1] == self.__board[0][2] != '-' )
        elif pos == 3:
            return (self.__board[0][0] == self.__board[0][1] == self.__board[0][2] != '-'  or
                self.__board[0][2] == self.__board[1][2] == self.__board[2][2] != '-'  or
                self.__board[0][2] == self.__board[1][1] == self.__board[2][0])
        elif pos == 4:
            return (self.__board[1][0] == self.__board[1][1] == self.__board[1][2] != '-'  or
                self.__board[0][0] == self.__board[1][0] == self.__board[2][0] != '-' )
        elif pos == 5:
            return (self.__board[0][1] == self.__board[1][1] == self.__board[2][1] != '-'  or
                self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != '-'  or
                self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != '-'  or
                self.__board[1][0] == self.__board[2][1] == self.__board[2][2] != '-' )
        elif pos == 6:
            return (self.__board[1][0] == self.__board[1][1] == self.__board[1][2] != '-'  or
                self.__board[0][2] == self.__board[1][2] == self.__board[2][2] != '-' )
        elif pos == 7:
            return (self.__board[2][0] == self.__board[2][1] == self.__board[2][2] != '-'  or
                self.__board[2][0] == self.__board[1][0] == self.__board[0][0] != '-'  or
                self.__board[2][0] == self.__board[1][1] == self.__board[0][2] != '-' )
        elif pos == 8:
            return (self.__board[2][1] == self.__board[1][1] == self.__board[0][1] != '-'  or
                self.__board[2][0] == self.__board[2][1] == self.__board[2][2] != '-' )
        elif pos == 9:
            return (self.__board[2][2] == self.__board[2][1] == self.__board[2][0] != '-'  or
                self.__board[2][2] == self.__board[1][2] == self.__board[0][2] != '-'  or
                self.__board[2][2] == self.__board[1][1] == self.__board[0][0] != '-' )
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
