import sys
from constants import *
from exceptions import *



class Board:
    '''
    This is a class for Board representation.
    '''

    def __init__(self, state=None):
        '''Initialises a state of board.'''
        self.state = state

    def print_state(self):
        '''Prints the state of board.'''
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=' ')
            print('\n')
        print('\n')

    def initialize_state(self):
        '''Initialises the state of board.'''
        self.state = [[NULL_MARKER for _ in range(LENGTH_DIMENSION)] for _ in range(LENGTH_DIMENSION)]

    def validate_move(self, i, j):
        '''Raises errors in the cases when the cell is out of field or is already busy.'''
        if i > LENGTH_DIMENSION - 1 or j > LENGTH_DIMENSION - 1:
            raise InvalidMove('exceeded length of dimension')
        if self.state[i][j] != NULL_MARKER:
            raise InvalidMove('this position is already marked')

    def move(self, i, j, player_marker=X_MARKER):
        '''Fills the array with positions and prints the state each time.'''
        self.state[i][j] = player_marker
        self.print_state()

    @property
    def is_full(self):
        '''
        Defines whether the state is full.
        :return:bool
        '''
        for row in self.state:
            if NULL_MARKER in row:
                return False
        return True

    def check_state(self):
        '''
        Check whether x or o wins.
        :return: int
        '''
        win_positions = []
        for state_row in self.state:
            win_positions.append(set(state_row))

        for i in range(LENGTH_DIMENSION):
            win_positions.append(set([self.state[j][i] for j in range(LENGTH_DIMENSION)]))

        win_positions.append(set([self.state[i][i] for i in range(LENGTH_DIMENSION)]))
        win_positions.append(set([self.state[i][LENGTH_DIMENSION - 1 - i] for i in range(LENGTH_DIMENSION)]))
        for win_position in win_positions:
            if not len(win_position) == 1:
                continue

            marker = win_position.pop()
            if marker == X_MARKER:
                return X_WIN
            elif marker == O_MARKER:
                return O_WIN

        return NO_WINNER

    def check_end_of_the_game(self):
        '''
        Check whether somebody wins or the board is full.
        '''
        result = self.check_state()
        if result in (X_WIN, O_WIN):
            print(' sssPlayer {} win! Congratulations!'.format(result))
            sys.exit(0)
        elif self.is_full:
            print('Draw! Try next time!')
            sys.exit(0)
