#!/usr/bin/env python
"""Tetris game using pygame."""

from copy import deepcopy
import sys
import pygame
import random

W, H = 10, 20
TILE = 25
GAME_RES = W * TILE, H * TILE
FPS = 60

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
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

## Змінюємоо координати фігур для того щоб вони зявились на нашій сітцій
## Рухаємо все на середину Зміщуємо головну точку фігури на 1 вниз, щоб вона влазила
#figures = [[pygame.Rect( x + Shyryna // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
## Rect(left, top, width, height)
figures = [[pygame.Rect( x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
## Устанавлюєм первоначальну точку 


def empty_lines(height):
    return [[None for c in range(W)] for r in range(height)]


field = empty_lines(H)


# Look through the field and get rid of full rows
def check_complete(field):
    # The sorted list of row numbers to remove
    to_destroy = []

    # Collect full lines
    for y in range(H-1, -1, -1):
        if None not in field[y]:
            to_destroy.append(y)

    if not to_destroy:
        return field

    # Delete the full lines
    for y in to_destroy:
        del(field[y])

    # Append the necessary count of empty lines at the top
    return empty_lines(H - len(field)) + field


figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
figure = deepcopy(random.choice(figures))

animation_speed = 1
animation_limit = 60
animation_count = 0


def hit_borders(x, y):
    if x < 0 or x > W - 1:
        return True
    if y > H - 1:
        return True
    if field[y][x]:
        return True
    return False

###################################### NEW #####################################
################################################################################
while True:

    dx = 0
    rotation = False

    game_sc.fill(pygame.Color('orange'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_DOWN:
                animation_limit = 1
            if event.key == pygame.K_UP:
                rotation = True

    figure_old = deepcopy(figure)
    if dx:
        for i in range(len(figure)):
            figure[i].x += dx
            if hit_borders(figure[i].x, figure[i].y):
                figure = figure_old
                break

    #falling down
    animation_count += animation_speed
    if animation_count > animation_limit:
        animation_count = 0
        figure_old = deepcopy(figure)
        for i in range(len(figure)):
            figure[i].y += 1
            if hit_borders(figure[i].x, figure[i].y):
                for j in range(len(figure_old)):
                    field[figure_old[j].y][figure_old[j].x] = pygame.Color('grey')
                field = check_complete(field)
                figure = deepcopy(random.choice(figures))
                animation_limit = 60
                break

    if rotation:
        figure_old = deepcopy(figure)
        center = figure[0]
        for i in range(1, len(figure)):
            x = figure[i].x - center.x
            y = figure[i].y - center.y
            figure[i].x = center.x + y
            figure[i].y = center.y - x
            if hit_borders(figure[i].x, figure[i].y):
                figure = figure_old
                break

    #draw_grid
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    #draw_figure
    for i in range(len(figure)):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, pygame.Color('blue'), figure_rect)

    # Draw field
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figure_rect.x = x * TILE
                figure_rect.y = y * TILE
                pygame.draw.rect(game_sc, col, figure_rect)

    ## Виклакаємо функцію малювання , ( задаємо розмір екрану, Встановлюємл колір фігур , Передаємо координати для малювання фігури )
    pygame.display.flip()
    clock.tick(FPS)
