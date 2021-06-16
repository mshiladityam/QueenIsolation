'''
maintain a board matrix of states of each cell
after each move, 
'''
import pygame
import sys
import time
from board import Board
from constants import SQUARE_SIZE, WHITE, BLACK, RED
FPS=5
HEIGHT, WIDTH=500, 500
pygame.init()
pygame.font.init()
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Queen Isolation")

font=pygame.font.SysFont(None, 50)

def message_to_screen(msg, color):
    screen_text=font.render(msg, True, color)
    WIN.blit(screen_text, [WIDTH//4, HEIGHT//2])

def getPoints(event):
    x = (event.pos[0])//SQUARE_SIZE
    y = (event.pos[1])//SQUARE_SIZE
    return x, y

matrix=[[4,4,4,1,4,4,4], [4,4,4,4,4,4,4], [4,4,4,4,4,4,4], [4,4,4,4,4,4,4] , [4,4,4,4,4,4,4], [4,4,4,4,4,4,4],[4,4,4,2,4,4,4]]

def main():
    run=False
    clock=pygame.time.Clock()
    
    while True:
        board=Board()
        board.draw_squares(WIN, matrix)
        clock.tick(FPS)
        if (matrix[0][0]==5):
            message_to_screen("Woaaahhhh you beat the machine!!!", RED)
            pygame.display.update();
            time.sleep(2)
            sys.exit(0)
        elif (matrix[0][0]==6):
            message_to_screen("You lost!!!", RED)
            pygame.display.update();
            time.sleep(2)
            sys.exit(0)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y=getPoints(event)
                x=int(x)
                y=int(y)
                board.move(WIN, matrix, x, y)
                board.draw_squares(WIN, matrix)
        pygame.display.update()
    pygame.quit()
main()