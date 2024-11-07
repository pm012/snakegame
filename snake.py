import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 600
display_height = 400

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

def draw_snake(snake_block, snake_list):
    for elements in snake_list:
        pygame.draw.rect(dis, black, [elements[0], elements[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_block = 10
    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, display_width-snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height-snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_over = True
        
        for coord in snake_list[:-1]:
            if coord[0] == x1 and coord[1] == y1:
                game_over = True

        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        draw_snake(snake_block, snake_list)
        #pygame.draw.rect(dis, black, [x1, y1, 10, 10]) 
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width-snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height-snake_block) / 10.0) * 10.0
            length_of_snake +=1


        time.sleep(0.1)
    pygame.quit()
    quit()

game_loop()
