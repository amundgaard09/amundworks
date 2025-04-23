import pygame
import random

pygame.init()
screenwidth = pygame.display.Info().current_w
screenheight = pygame.display.Info().current_h
pygame.display.set_mode((screenwidth, screenheight))

colors = [
    (255, 0, 0), # RED
    (255, 127, 0), # ORANGE
    (255, 255, 0), # YELLOW
    (0, 255, 0),  # GREEN
    (0, 255, 255), # CYAN
    (0, 0, 255), # BLUE
    (255, 0, 255), # MAGENTA
    (255, 192, 203), # PINK
    (255, 255, 255), # WHITE
    (128, 128, 128), # GRAY
]

running = True
drawatmouse = False
clearing = False
radius = 5
pygame.display.set_caption("Sybau")
currentcolor = random.choice(colors)

while running:
    mousepos = pygame.mouse.get_pos()
    if drawatmouse: # pensel
        pygame.draw.circle(pygame.display.get_surface(), currentcolor, mousepos, radius) 
    if clearing: # viskelær
        pygame.draw.circle(pygame.display.get_surface(), (0, 0, 0), mousepos, radius) 

    for event in pygame.event.get(): # main
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_c:
                currentcolor = random.choice(colors)

            if event.key == pygame.K_SPACE:
                clearing = False
                if drawatmouse:
                    drawatmouse = False
                else:
                    drawatmouse = True

            if event.key == pygame.K_UP:
                radius += 1

            if event.key == pygame.K_DOWN:
                radius -= 1
                if radius < 1:
                    radius = 1

            if event.key == pygame.K_q:
                if clearing:
                    clearing = False
                else:
                    clearing = True
                drawatmouse = False
                pygame.draw.circle(pygame.display.get_surface(), (0, 0, 0), mousepos, radius)  

                
    pygame.display.update()


