from constants import *
from copy import deepcopy
from board import Board

PLAYED_INDEX = 0
POSITION_INDEX = 1


class GameTree:
    '''This class represents a GameTree.'''

    def __init__(self, state, last_pos, depth):
        '''
        Initialises a GameTree.
        :param state:list
        :param last_pos: tuple
        :param depth: int
        '''
        self.board = Board(state)
        self.nodes = []
        self.scores = None
        self.depth = depth
        self.last_move = last_pos  # Will store info about last move in format: (X_PLAYER, (3, 2))

    def calculate_scores(self):
        '''
        Calculates a score.
        :return: int
        '''
        if not self.nodes:
            result = self.board.check_state()
            if result == X_WIN:
                self.scores = -1
            elif result == O_WIN:
                self.scores = 1
            else:
                self.scores = 0
        else:
            for node in self.nodes:
                if node:
                    node.calculate_scores()
        return self.scores

    @staticmethod
    def get_order(marker):
        '''
        Gets the coeficient for function choose_node
        :param marker: str
        :return: int
        '''
        if marker == O_MARKER:
            return 1
        return -1

    def choose_node(self, turn=O_MARKER):
        '''
        Chooses the best option to win.
        :param turn: str
        :return: GameTree
        '''
        self.calculate_scores()
        if not self.nodes:
            return self
        prev_chosen_nodes = [node.choose_node(turn=self.get_next_marker(turn)) for node in self.nodes]
        prev_chosen_nodes.sort(key=lambda el: (self.get_order(turn) * el.scores, el.depth))
        return prev_chosen_nodes[0]

    def choose(self):
        '''
        Returns the position of most convenient position to go to.
        :return: tuple
        '''
        best_node = self.choose_node()
        return best_node.last_move

    @classmethod
    def get_next_marker(cls, current):
        '''
        Gets the marker for next move.
        :param current: str
        :return:str
        '''
        return X_MARKER if current == O_MARKER else O_MARKER

    @classmethod
    def build(cls, state, pos, marker=O_MARKER, depth=0):
        '''
        Builds the tree with given parameters.
        :param state: list
        :param pos: tuple
        :param marker: str
        :param depth: int
        :return:GameTree
        '''
        root = cls(state, last_pos=pos, depth=depth)
        if root.board.is_full or root.board.check_state() in (X_WIN, O_WIN):
            return root
        x = 0
        for row in range(LENGTH_DIMENSION):
            for col in range(LENGTH_DIMENSION):
                if state[row][col] == NULL_MARKER:
                    new_state = deepcopy(state)
                    new_state[row][col] = marker
                    new_tree = cls.build(new_state, pos=(row, col), marker=cls.get_next_marker(marker), depth=depth + 1)
                    root.nodes.append(new_tree)
                    x += 1
                    if x == 2:
                        return root
        return root

    def print(self):
        '''
        Prints the state of the board.
        '''
        self.board.print_state()
        for node in self.nodes:
            node.print()
