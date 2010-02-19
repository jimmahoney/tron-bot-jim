#!/usr/bin/python

# This is a random comment.

import tron, random

def which_move(board):
    return random.choice(board.moves())

for board in tron.Board.generate():
    tron.move(which_move(board))
