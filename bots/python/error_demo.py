#!/usr/bin/python
"""
 error_demo.py 

 A both that just moves south.
 And after a couple of moves, a 1/0 error kills it.
 
 The point here is to demonstrate the use of 
 the LogFile utility, which serves two purposes :
  (1) you send the logfile explicit messages, and 
  (2) runtime errors are output to the logfile.

 $ cd tron-bot-jim     # from root directory
 $ . conf/environment  # set up environment
 $ tron -v -i -B maps/empty-room.txt $pybots/error_demo.py $pybots/randbot.py

 Jim Mahoney | Feb 2010 | GPL
"""

import random, tron, utilities

debug = utilities.LogFile("logs/error_demo.txt")
data = {'move#':0}

def which_move(board):
  move = tron.SOUTH
  direction = utilities.direction2string[move]
  data['move#'] += 1
  debug.log("move %i : %s " % (data['move#'], direction))
  #
  # A few moves already?  Let's throw an error ...
  if data['move#'] > 3: error = 1/0
  #
  return move

# --- main -------------------
for board in tron.Board.generate():
  tron.move(which_move(board))
