import pygame

pygame.init()

#Creating window
gameWindow = pygame.display.set_mode((1200, 500)) 
pygame.display.set_caption("My First Game")     #this function will set the title of the game

# Game specific variable
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        # print(event)  
        #pygame.event.get() is the movements we do with our mouse or the keys we press or anything
        if event.type == pygame.QUIT:
            exit_game = True   #this will help us to exit the game

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed the rigth arrow key")

pygame.quit()    #this will exit the pygame 
exit()     #this will exit the python