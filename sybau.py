

import pygame

pygame.init()
screenwidth = pygame.display.Info().current_w
screenheight = pygame.display.Info().current_h
pygame.display.set_mode((screenwidth, screenheight))


RED     = (255, 0,   0)
ORANGE  = (255, 127, 0)
YELLOW  = (255, 255, 0) 
GREEN   = (0,   255, 0)  
CYAN    = (0,   255, 255) 
BLUE    = (0,   0,   255)
MAGENTA = (255, 0,   255) 
PINK    = (255, 192, 203)
WHITE   = (255, 255, 255)
GRAY    = (128, 128, 128)


running = True
drawatmouse = False
clearing = False
radius = 5
pygame.display.set_caption("Sybau")
currentcolor = RED
probeposx = 0
probeposy = 0
brushspeed = 5

while running:
    if UseMouse:
        usepos = mousepos
    if UseProbe:
        usepos = probepos
    probepos = (probeposx, probeposy)
    mousepos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed() 

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
            
            if keys[pygame.K_w]:
                probeposy -= brushspeed
            if keys[pygame.K_s]:
                probeposy += brushspeed
            if keys[pygame.K_a]:
                probeposx -= brushspeed
            if keys[pygame.K_d]:
                probeposx += brushspeed   

            if event.key == pygame.K_1:
                currentcolor = RED
            if event.key == pygame.K_2:
                currentcolor = ORANGE
            if event.key == pygame.K_3:
                currentcolor = YELLOW
            if event.key == pygame.K_4:
                currentcolor = GREEN
            if event.key == pygame.K_5:
                currentcolor = CYAN
            if event.key == pygame.K_6:
                currentcolor = BLUE
            if event.key == pygame.K_7:
                currentcolor = MAGENTA
            if event.key == pygame.K_8:
                currentcolor = PINK
            if event.key == pygame.K_9:
                currentcolor = GRAY
            if event.key == pygame.K_0:
                currentcolor = WHITE

            if event.key == pygame.K_UP:
                radius += 1
            if event.key == pygame.K_DOWN:
                radius -= 1
                if radius < 1:
                    radius = 1
            if event.key == pygame.K_SPACE:
                clearing = False
                if drawatmouse:
                    drawatmouse = False
                else:
                    drawatmouse = True
            if event.key == pygame.K_c:
                if clearing:
                    clearing = False
                else:
                    clearing = True
                drawatmouse = False
                pygame.draw.circle(pygame.display.get_surface(), (0, 0, 0), mousepos, radius)
            if event.key == pygame.K_m:
                if UseMouse:
                    UseMouse = False
                    UseProbe = True
                else:
                    UseMouse = True
                    UseProbe = False
    pygame.display.update()


