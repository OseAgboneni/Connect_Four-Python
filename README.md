# Connect_Four-Python
School Project:
Python implementation of Connect Four

TO PLAY:
Run Connect_Four_4 in the shell (of course, make sure parts 1-3 are in the same directory).
In the shell, call the "connect_four(player1, player2)" function. 
      -If two human players are playing, then the two arguments should be Player('X') and Player('O'). The game won't start if any character/string other than 'X' and 'O' are used!
      -If one human wants to play against an AI, then the two arguments should be Player('X') and AIPlayer('O', <TIEBREAK>, <LOOKAHEAD>), where TIEBREAK is one of the following strings: "RIGHT", "LEFT", or "RANDOM". The TIEBREAK argument determines how the AI resolves ties in its calculation of where its next move will go. LOOKAHEAD is simply an integer that determines how many moves ahead the AI will look when figuring out its next move. The higher the number, the higher the difficulty of the AI. If the number is too high though, the game may lag. An average difficulty AI has a lookahead of 2 or 3. Of course, you can switch which player has the 'X' checker and which has the 'O' checker.
      -If you want to see two AIs play against each other, then make both of the arguments AIPlayers with the appropriate parameters set.
  
KNOWN ISSUES:
-None, really. The game will throw an error and exit if an improper parameter is passed, but once the game is started up, it'll keep going until someone wins or the board gets filled. 
-One other thing: in order to not have the AI games happen in the blink of an eye, I put a 2 second time pause after Player 1's turn. It'll have that pause even when 2 human players are playing. It never felt really annoying when I tested it with others so I just left it in.
