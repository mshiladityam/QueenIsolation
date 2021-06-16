# QueenIsolation

This is an abstract strategy board game.

The rules of the game are:
1) There is an 7x7 checker board.
2) There are two players: player 1 is the user, player 2 is the computer
3) Each player has one piece, which they can move around like a queen in chess
4) There are three conditions under which the pieces can be moved —
      a) They cannot place their piece on an already visited square.
      b) They cannot cross over already visited squares (squeezing through them diagonally is OK).
      c) They cannot cross over each other’s piece.
5) The player, who cannot move in his turn, loses.

In this project, I used Minimax Algorithm with Alpha-Beta Pruning to make the GameEngine in C++ 

I made the game interface using PyGame.

![Gameplay](/gameplay.png)
