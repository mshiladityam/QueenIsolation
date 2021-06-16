import pygame
from constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WIDTH, HEIGHT, BLUE, WHITE, PINK, GREEN
import subprocess
from sys import platform, setprofile

class Board:
    def __init__(self):
        pass
    def draw_squares(self, win, matrix):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                if (matrix[row][col]==1):
                    pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif (matrix[row][col]==2):
                    pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif (matrix[row][col]==4 and (row+col)%2==0):
                    pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif (matrix[row][col]==4 and (row+col)%2==1):
                    pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    def move(self, win, matrix, x, y): #move player 1's piece to (x, y)
        old_x=0;
        old_y=0;
        for i in range(ROWS):
            for j in range(COLS):
                if (matrix[i][j]==1):
                    old_x=i;
                    old_y=j;

        q=False
        bad=False
        if (old_x==x):
            for i in range(min(y, old_y)+1, max(y, old_y)):
                if (matrix[x][i]!=4):
                    bad=True;
            q=True;
        
        elif (old_y==y):
            for i in range(min(x, old_x)+1, max(x, old_x)):
                if (matrix[i][y]!=4):
                    bad=True;
            q=True;   
        
        elif ((old_x-old_y==x-y) or (old_x+old_y==x+y)): q=True;

        if ((q==False) or (bad==True) or matrix[x][y]!=4): return
        matrix[old_x][old_y]=3;
        matrix[x][y]=1;
        inp=""
        for i in range (ROWS):
            for j in range(COLS):
                inp+=str(matrix[i][j]);
                inp+=' ';
            inp+='\n'
        stri = subprocess.run(["GameEngine.exe"], text=True, input=inp,
                                 stdout=subprocess.PIPE).stdout
        stri = stri.splitlines()
        for i in range(ROWS):
            matrix[i]=list(map(int, stri[i].strip().split()))