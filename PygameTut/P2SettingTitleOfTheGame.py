import pygame

pygame.init()

#Creating window
gameWindow = pygame.display.set_mode((1200, 500)) 
pygame.display.set_caption("My First Game")     #this function will set the title of the game

# Game specific variable
exit_game = False
game_over = False