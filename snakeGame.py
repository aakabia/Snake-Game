# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
pygame.display.set_caption("Aziz Snake Game")

dis_width = 500
dis_height  = 500
screen = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

# Above creates a width and height for our game board 
# pygame.time.Clock() object allows you to control the speed of your game by setting a target frame rate


font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# Above sets a font_style object and score_font object 


def our_snake(snake_block, snake_list):
    for snakePart in snake_list:
        pygame.draw.rect(screen, "green", [snakePart[0], snakePart[1], snake_block, snake_block])
 

# our_snake takes in a snake_block size and a snake_list list 
# for each entry in the list we creat a rec with its xand y positions as snakePart[0], snakePart[1] and its height and width as snake_block


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [30, 250])


# message function takes a message and a color 
# renders a message using our font_style object 
# adds the message to the screen using screen.blit





def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, "Yellow")
    screen.blit(value, [0, 0])


# Your_score function takes score
# renders a message using our score_font object 
# adds the message to the screen using screen.blit



def gameLoop():

    running = True
    game_close = False

    # Above  creates or variables for the game running and closing 

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0       
    y1_change = 0

    # Above is our snakes inital position and inital rate of change 

    snakeSpeed = 12
    snake_block = 12

    # Above is our snake speed and size 


    snake_List = []
    Length_of_snake = 1


    # Above, we initalize an empty list for snake_List and  Length_of_snake variable at 1



    foodx = round(random.randrange(0, 500 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, 500 - snake_block) / 10.0) * 10.0

    # Above are our random x and y value for our food
    # These values compliment our screen size 

 

    while running:

        # Above Initalizes outter while loop when running is true 

        while game_close == True:
             # Above Initalizes inner while loop when game_close is true also.

            screen.fill("blue")
            message("You Lost! Press Q For Quit or C for Play Again", "red")
            Your_score(Length_of_snake - 1)
            pygame.display.flip()

            # Above fills our background color, displays a message , displays a score and updates the frame.
           
            for event in pygame.event.get():

                # Above manages our events in pygame.event.get() for our inner while loop

                if event.type == pygame.QUIT:
                    running = False
                    game_close = False

                # Above handles closing the game tab 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

                    # Above manages if the q or c keys are pressed
        

        for event in pygame.event.get():
            # Above manages our events in pygame.event.get() for our outter while loop

            if event.type == pygame.QUIT:
                running = False

            # Above handles closing the game tab 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
            # Above manages if our arrow keys are pressed 
            # We increment or decrement the respected x or y value 
            
        
        

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        # Above chacks if our x and y value stretch past our screen length.
        # If it does we end the game 

        
        
        x1 += x1_change
        y1 += y1_change

        # Above updates our x and y value at each change

        
        screen.fill("blue")


        
        pygame.draw.rect(screen, "red", [foodx, foody, snake_block, snake_block])

        # Above creates our random food item with our x and y values 

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Above createsa new snake head and addis it to our snake_List

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Above makes sure we control the length of our snake_List to not grow bigger than Length_of_snake

        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Above makes sure the snake_Head cant touch any part of its body 
        # If it does the game is over 


        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        # Above updates our_snake list and renders our snakes 
        # Also displays our current score 




       
        pygame.display.flip()
        # flip() the display to put your work on screen


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        # Above sets a new food x and y if our current x1 and y1 match foodx foody
        

        clock.tick(snakeSpeed)

        # Above sets the speed of our frames
    

    pygame.quit()
    quit()

    # Above ends the function and game becuase running is now false




if __name__ == "__main__":
    gameLoop()



