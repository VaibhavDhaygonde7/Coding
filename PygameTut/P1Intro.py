import pygame

x = pygame.init()      #this will initialize all the modules of the pygame module

# print(x)     #this will print (6,0) 
# 6 is the number of modules initalized and 0 is the number of module which are not initialized

gameWindow = pygame.display.set_mode((1200, 500)) 
# the function typed above takes input of a tuple and 1200 is the width of the display and 500 is the height
# of the display