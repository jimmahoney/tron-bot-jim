#!/usr/bin/python
"""
 Keep your right hand on the wall.
"""

import random
from tron import NORTH, SOUTH, EAST, WEST, DIRECTIONS, \
                 FLOOR, WALL, ME, THEM, Board, move

rightwards = {NORTH:EAST, EAST:SOUTH, SOUTH:WEST, WEST:NORTH}
leftwards = {NORTH:WEST, WEST:SOUTH, SOUTH:EAST, EAST:NORTH}

me, them = None, None


class BotHistory(object):
  """ A bot's previous position, direction of motion, etc. """
  def __init__(self, board, bot, direction=None):
    self.bot = bot
    self.position = [board.find(bot)]
    self.direction = [direction or random.choose(DIRECTIONS)]


def init(board):
  if me:
    me.update(board)
    them.update(board)
  else:
    me = BotHistory(board, ME)
    them = BotHistory(board, THEM)


def which_move(board):
  movingDirection = lastDirection or random.choose(DIRECTIONS)
  return random.choice(board.moves())


# --- main -------------------
for board in Board.generate():
  move(which_move(board))
