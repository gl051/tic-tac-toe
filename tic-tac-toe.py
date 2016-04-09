#!/usr/bin/python

"""
    Exercise: Implement a Tic-Tac-Toe game
"""
import grid
import random

class TicTacToe(object):
    def __init__(self):
        self.grid = grid.Grid()
        self.game_over = False
        self.players = {0: 'User', 1:'AI'}

    def user_pick(self):
        self.grid.show()
        pos_str = raw_input("Your turn, pick a slot available (1 to 9): ")
        pos = int(pos_str)
        self.grid.mark(pos, 'x')

    def computer_pick(self):
        #pos = random.sample(self.grid.empty_slots,1)[0]
        pos = random.choice(self.grid.empty_slots)
        self.grid.mark(pos, 'o')
        print 'AI,marked on position {}'.format(pos)

    def play(self):
        # randomly start with one of the two players
        pick = random.randint(0, 1)
        print "Let's play, {} goeas first".format(self.players[pick])
        self.game_over = False;

        while not self.game_over:
            self.callPlayer(pick)
            # toggle next player
            pick = (pick + 1) % 2


    def callPlayer(self, pick):
        # Check there are still slots available
        if self.grid.is_full():
            print '*** Tie Game ***'
            self.game_over = True
            return
        print '{} play now'.format(self.players[pick])
        if pick == 0:
            self.user_pick()
        elif pick == 1:
            self.computer_pick()
        # check if the player won
        if self.grid.is_winner():
            self.grid.show()
            if pick == 0:
                print '*** Congratulation, you won! ***'
            elif pick == 1:
                print '*** I am sorry, AI won! ***'
            self.game_over = True

# Gather our code in a main() function
def main():
  game = TicTacToe();
  game.play()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
