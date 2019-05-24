from main import Board
from constants import *

state1 = [
    ['X', 'X', 'X'],
    ['-', 'O', 'X'],
    ['-', '-', '-']
]



state1 = [
    ['X', 'X', 'X'],
    ['-', 'O', 'X'],
    ['-', '-', '-']
]



state2 = [
    ['X', 'O', 'X'],
    ['-', 'O', 'X'],
    ['-', 'O', '-']
]


state3 = [
    ['X', 'X', 'O'],
    ['X', 'O', 'X'],
    ['X', '-', '-']
]


state4 = [
    ['X', 'X', 'O'],
    ['-', 'O', 'X'],
    ['O', '-', '-']
]


state5 = [
    ['X', 'O', 'X'],
    ['-', 'O', 'X'],
    ['-', '-', 'X']
]

state6 = [
    ['-', 'O', 'X'],
    ['-', 'O', '-'],
    ['-', '-', 'X']
]

state7 = [
    ['O', 'O', 'X'],
    ['-', 'O', '-'],
    ['-', '-', 'O']
]

state8 = [
    ['O', 'O', 'X'],
    ['-', 'X', '-'],
    ['X', '-', 'O']
]

state9 = [
    ['O', 'O', 'X'],
    ['X', 'X', 'X'],
    ['X', '-', 'O']
]

state10 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', '-', '-']
]

assert Board(state1).check_state() == X_WIN
assert Board(state2).check_state() == O_WIN
assert Board(state3).check_state() == X_WIN
assert Board(state4).check_state() == O_WIN
assert Board(state5).check_state() == X_WIN
assert Board(state6).check_state() == NO_WINNER
assert Board(state8).check_state() == X_WIN
assert Board(state9).check_state() == X_WIN
assert Board(state10).check_state() == O_WIN







