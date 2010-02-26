
Messing about with python clients that play Tron in the 
2010 University of Waterloo "Google AI Challenge"

This project is hosted at http://code.google.com/p/tron-bot-jim/ .

The code and project infrastructure is a demo for the 
programming workshop course at Marlboro College in Spring 2010
at http://cs.marlboro.edu/courses/spring2010/programming/home .

Questions and comments can be sent to 
Jim Mahoney (mahoney@marlboro.edu).

-----------------------------------------------------------------

Run this from the command line in this directory like this :

  $ . conf/environment       # Define environment and aliases.
  $ tron_example             # Watch two bots battle.
  $ tourney_example          # See the results of a tournament.
  $ tron --help              # Get help.
  $ tourney --help           # Ditto.

  # Choose a room and two robots explicitly
  $ tron -v -i -B maps/empty-room.txt $pybots/randbot.py $pybots/randbot.py

Adapt the templates in the conf/ directory to suit your purposes.

-----------------------------------------------------------------

To prepare a python robot for competition submission, 
name it MyTronBot.py, put it and any needed files (e.g. tron.py)
in its own folder, and compress it all.

-----------------------------------------------------------------

History

 v0.2   Feb 18 2010 - infrastructure set up from 
        python_starter_package and python_tournament_engine

 v0.3   Feb 26 2010 - utilities.py with LogFile, BotHistory class;
        working right_hand.py bot that can do a maze.


