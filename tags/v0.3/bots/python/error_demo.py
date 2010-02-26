#!/usr/bin/python
"""
 error_demo.py 

 A tron bot that just moves south.
 And after a couple of moves, a 1/0 error kills it.
 
 The point here is to demonstrate the use of 
 the LogFile utility, which serves two purposes :
   (1) it can save (to a file) debug messages, and 
   (2) it also saves runtime errors.

 Running it looks like this :

   $ cd tron-bot-jim     # from root directory
   $ . conf/environment  # set up environment
   $ tron -v -B maps/empty-room.txt $pybots/error_demo.py $pybots/randbot.py
   # ... which prints an unhelpful error from the engine, something like
   player.PlayerFailedException: bots/python/error_demo.py ...
   # ... but actual error is stored in the log file :
   $ cat logs/error_demo.txt
   --- 'logs/error_demo.txt' at Thu Feb 25 22:30:30 2010 --- 
   move 1 : south 
   move 2 : south 
   move 3 : south 
   move 4 : south 
   Traceback (most recent call last):
     File "bots/python/error_demo.py", line 44, in <module>
       tron.move(which_move(board))
     File "bots/python/error_demo.py", line 38, in which_move
       if data['move#'] > 3: error = 1/0
   ZeroDivisionError: integer division or modulo by zero

 So there you are.

 Jim Mahoney | Feb 2010 | GPL
"""

import tron, utilities

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
