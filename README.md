# QueenIsolation

This is an abstract strategy board game, like Checkers or Chess. The description of the game is really simple and is as follows:

1) There is an 7x7 checker board.
2) There are two players: player 1 is the user, player 2 is the computer
3) Each player has one piece, which they can move around like a queen in chess
4) There are three conditions under which the pieces can be moved —
      a) They cannot place their piece on an already visited square.
      b) They cannot cross over already visited squares (squeezing through them diagonally is OK).
      c) They cannot cross over each other’s piece.
5) The player, who cannot move in his turn, loses.

This game is not solved in the game-theoretic sense, which means that given an arbitrary position, it is not computationally practical 
to determine the state of the game. However, we can come up with a heuristic function which can come up with an "evaluation" for the 
position. In this evaluation, +inf is winning for Player 1 and -inf is winning for Player 2. 

The heuristic function I have used is really simple but quite effective: f(GAME_STATE)=No of moves available for (Player 1-Player2)
Then, using this as an evaluating function, I applied Minimax Algorithm with alpha-beta pruning.

We can easily adjust the difficulty of the game by changing the DEPTH of minimax algorithm. Computationally, a depth of 5 is pretty strong and very fast too.

I made the GameEngine in C++, because here, the time taken for the computer to think should be as small as possible and hence, due
to performance considerations, C++ is the best choice.

For the game interface I used PyGame, a module in Python.

![Gameplay](/GameplayGIF1.gif)
