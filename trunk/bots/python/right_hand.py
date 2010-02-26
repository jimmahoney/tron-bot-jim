#!/usr/bin/python
"""
 right_hand.py 
 A tron bot whose rule is: keep your right hand on the wall.
 Jim Mahoney | Feb 2010 | GPL
"""

# Remember that coordinates are (y,x) with (0,0) at the top left.

import random, tron, utilities

# history = utilities.BotHistory()
debug = utilities.LogFile("logs/right_hand.txt")

a = [0]

def which_move(board):
  debug.log(" a move ... ")
  a[0] += 1
  if a[0] > 3: a[0] = 1/0
  return tron.SOUTH

###
  # history.update(board)
  # direction = randomDirection()
  # debug.log("last, this directions = " + \
  #             direction2string(direction) + \
  #             ", " + direction2string(history.lastDirection()))
  # return direction

# --- main -------------------
for board in tron.Board.generate():
  tron.move(which_move(board))
