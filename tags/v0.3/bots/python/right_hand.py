#!/usr/bin/python
"""
 right_hand.py 
 A tron bot whose rule is: keep your right hand on the wall.
 Jim Mahoney | Feb 2010 | GPL
"""

import random, tron, utilities

history = utilities.BotHistory()
debug = utilities.LogFile("logs/right_hand.txt")

def lookForWall(board):
  """ Return a move along a right hand wall, or a random move. """
  for direction in tron.DIRECTIONS:
    directionString = utilities.direction2string[direction]
    debug.log("  looking %s for open with wall right " % directionString)
    right = utilities.rightwards[direction]
    if board.passable(board.rel(direction)) \
          and not board.passable(board.rel(right)):
      debug.log("  yup, let's do that.")
      return direction
  debug.log("  no motion along a wall found; picking randomly.")
  return random.choice(board.moves())

def which_move(board):
  history.update(board)
  debug.log("move %i" % history.length())
  if history.length() == 1:
    debug.log("  1st move")
    direction = lookForWall(board)
  else:
    oldDirection = history.lastDirection()
    debug.log("  was moving %s" % utilities.direction2string[oldDirection])
    direction = utilities.rightwards[oldDirection]
  finalTry = utilities.rightwards[direction]
  while True:
    directionString = utilities.direction2string[direction]
    debug.log("  looking at %s ..." % directionString)
    if board.passable(board.rel(direction)):
      debug.log("  yup, am moving %s" % directionString)
      return direction
    elif direction == finalTry:
      debug.log("  no where to go - moving north to die")
      return tron.NORTH
    else:
      debug.log("  turning left ...")
      direction = utilities.leftwards[direction]

# --- main -------------------
for board in tron.Board.generate():
  tron.move(which_move(board))
