# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 02:29:46 2020

Title : Snake Game
	
Contest: Self

@author: kQueen_Etiquette
"""

import sys
import time
import pygame
import random
import winsound

pygame.init()

dis_width = 800
dis_height = 600
snake_block = 10
snake_speed = 10

frequency = 2500
duration = 100

display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Snake Game by kQueen_Etiquette')

yellow = (255,255,0)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
dpink = (255, 0, 102)
white = (255, 255, 255)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('comicsansms', 30)
score_style = pygame.font.SysFont('comicsanms', 35)

apple = pygame.image.load('D:\\apple.png')

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, yellow, [x[0], x[1], snake_block, snake_block])
        
def Your_score(score):
    Score = score_style.render("Your Score: " + str(score), True, white)
    display.blit(Score, [10, 10])

def message(msg, color):
    Msg = font_style.render(msg, True, color)
    display.blit(Msg, [dis_width /6 + 25, dis_height /3 + 75])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width /2
    y1 = dis_height /2
    
    x_change = 0
    y_change = 0
    
    snake_list = []
    snake_length = 1
    
    foodx = round(random.randrange(0, dis_width -snake_block) /10.0) *10.0
    foody = round(random.randrange(0, dis_height -snake_block) /10.0) *10.0
    
    while not game_over:
        
        while game_close == True:
            time.sleep(1)
            display.fill(black)
            message("You Lost!!! Press Q-Quit or C-Play Again", dpink)
            Your_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x_change
        y1 += y_change
        
        display.fill(black)
        display.blit(apple, (foodx, foody))
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        for p in snake_list[:-1]:
            if p == snake_head:
                game_close = True
                
        our_snake(snake_block, snake_list)
        Your_score(snake_length - 1)
        
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width -snake_block) /10.0) *10.0
            foody = round(random.randrange(0, dis_height -snake_block) /10.0) *10.0
            winsound.Beep(frequency, duration)
            snake_length += 1
        
        clock.tick(snake_speed)
        
    pygame.quit()
    sys.exit()
    
game_loop()