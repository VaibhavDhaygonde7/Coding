import pygame
import random

pygame.init() 

# Colors with rgb values
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 700
screen_height = 400


#Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Snakes - First Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
# by selecting None we will get the default font and 55 is the font size\
with open("hiscore.txt", "r") as f:
    hiscore = f.read()
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)    # always give True as teh second argument
    gameWindow.blit(screen_text, [int(x),int(y)])   # this will update the screen

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 220, 229))
        text_screen("Welcome to Snakes", black, 200, 150)
        text_screen("Press Space Bar To Play", black, 175, 180)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(30)


# Creating Game Loop
def gameloop():
    # Game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0 
    init_velocity = 5
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    snake_size = 20 
    fps = 30
    snk_list = []
    snk_length = 1
    score = 0
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter to continue", red, 100, screen_height/2-50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True   #this will help us to exit the game

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: 
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True   #this will help us to exit the game
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score = score + 10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 20:
                #abs will print approximate values
                score = score + 10
                # remember that the first argument should be a string
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                if score>int(hiscore):
                    hiscore = score


            gameWindow.fill(white)   #this will fill white color \
            text_screen("Score: " + str(score) + "  High Score: " + str(hiscore), red, 5, 5)   
            # Drawing food for the snake
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]     #this will cut the head of the snake
            # Drawing snake 
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])]
            if head in snk_list[:-1]:
                game_over = True
                # our last element of the snk_list is the head so we are excluding the last element of the
                # snk_list 
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
            # this function takes argument which is as follows
            # gameWindow, color, [x position, y position, length, height]
        pygame.display.update()   #we have to run this function whenever we make any changes in the display
        clock.tick(fps)

    pygame.quit()    #this will exit the pygame 
    exit()     #this will exit the python

welcome()