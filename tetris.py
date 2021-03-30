#!/usr/bin/env python

import pygame
from copy import deepcopy

W, H = 14, 28
TILE = 25
GAME_RES = W * TILE, H * TILE
FPS = 1

figure_number = 1 

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()
grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range (H)]
################################################################################
###################################### NEW ######################################
### Создаем Координати фигур 
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)],
               [(0, 0), (-1, 0), (1, 0), (0, 1), (-1, -1)]]

## Змінюємоо координати фігур для того щоб вони зявились на нашій сітцій 
## Рухаємо все на середину Зміщуємо головну точку фігури на 1 вниз, щоб вона влазила 
#figures = [[pygame.Rect( x + Shyryna // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
## Rect(left, top, width, height)
figures = [[pygame.Rect( x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
## Устанавлюєм первоначальну точку 
# Rect(left, top, width, height)
# Rect( Віступ вліво, Вершина фігури (точка), Товщина, Висота)
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
### Викликаємо Фігури які в нас є ( 7 штук )
figure = deepcopy(figures[figure_number])

###################################### NEW #####################################
################################################################################
while True:

    dx = 0

    game_sc.fill(pygame.Color('orange'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1

    print(f'dx = {dx}')

    figure_old = deepcopy(figure)
    for i in range(len(figure)):
        figure[i].x += dx
        if figure[i].x < 1 or figure[i].x >= TILE - 1:
            figure = figure_old
            break
    
    #draw_grid
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]
    ################################################################################
    ###################################### NEW #####################################
    #draw_figure
    # Для кожного із кубіків фігури робимо наступні дії
    for i in range(len(figure)):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, pygame.Color('blue'), figure_rect)
    ## Виклакаємо функцію малювання , ( задаємо розмір екрану, Встановлюємл колір фігур , Передаємо координати для малювання фігури )
    ###################################### NEW #####################################
    ################################################################################
    pygame.display.flip()
    clock.tick(FPS)
