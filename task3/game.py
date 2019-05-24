from exceptions import InvalidMove
from board import Board
from bstree import GameTree
from constants import *


def get_position():
    '''
    Gets the position as a string and returns as a tuple of coordinates.
    :return: tuple
    '''
    while True:
        position_str = input('Enter coordinates of your next move in format i,j:\n')
        try:
            i, j = map(lambda el: el - 1, map(int, position_str.split(',')))
        except ValueError:
            print('Invalid format. Please try again')
        else:
            return i, j


class Bot:
    '''This is a class which represents a Bot'''

    def __init__(self, board):
        '''
        Initialises a Bot class.
        :param board: Board
        '''
        self.board = board
        self.game_tree = None

    def move(self, prev_i, prev_j):
        '''
        Represents a movement.
        :param prev_i: int
        :param prev_j: int
        '''
        self.game_tree = GameTree.build(self.board.state, pos=(prev_i, prev_j))
        i, j = self.game_tree.choose()
        self.board.move(i, j, player_marker=O_MARKER)


if __name__ == '__main__':
    board = Board()
    board.initialize_state()
    board.print_state()
    bot = Bot(board)
    while True:
        row, col = get_position()
        try:
            board.validate_move(row, col)
        except InvalidMove as e:
            print('Please retry again, because {}'.format(e))
            continue

        board.move(row, col)
        board.check_end_of_the_game()

        bot.move(row, col)
        board.check_end_of_the_game()
