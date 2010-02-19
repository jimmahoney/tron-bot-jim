#!/usr/bin/python

""" Moves in a random direction """

import random, tron

move_number = [0]
logFile = tron.LogFile("randbot")

def which_move(board):
	move_number[0] += 1
	move = random.choice(board.moves())
	logFile.log(" move " + str(move_number[0]) + ":" + str(move))
	return move

# make a move each turn
for board in tron.Board.generate():
	tron.move(which_move(board))
