"""
 Utility functions and classes for tron bots.
"""

from tron import NORTH, EAST, SOUTH, WEST
import sys, time

rightwards = {NORTH:EAST, EAST:SOUTH, SOUTH:WEST, WEST:NORTH}
leftwards = {NORTH:WEST, WEST:SOUTH, SOUTH:EAST, EAST:NORTH}
vector2direction = {(1,0):NORTH, (0,1):EAST, (-1,0):SOUTH, (0,-1):WEST}
direction2string = {NORTH:'north', EAST:'east', SOUTH:'south', WEST:'west'}

class LogFile():
	""" A log file for storing bot messages. 
            Usage:
              debug = LogFile("botlog.txt")
              debug.log("put your message here.")
        """
	def __init__(self, name):
		self.name = name
		self.file = open(name, 'a')
		self.file.write("--- '%s' at %s --- \n" % \
                                  (name, time.asctime()))
                sys.stderr = self.file    # send errors to the log
	def log(self, message):
		self.file.write(message + "\n")

class BotHistory(object):
  """ Keep a record of a bot's history. 
      Usage: 
        h = BotHistory()
        h.update(board)   # Do this for each new board.
        print direction2string(h.lastDirection())
  """
  def __init__(self):
    self.positions = []
    self.directions = []
  def update(self, board):
    self.positions.append(board.me())
  def lastDirection(self):
    if length(self.directions) < 2:
      return NORTH
    else:
      vector = (self.direction[-2][0] - self.direction[-1][0], 
                self.direction[-2][1] - self.direction[-1][0])
      return vector2direction(vector)

