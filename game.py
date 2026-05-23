import pygame
import sys
import Entity
import player
import boss
import attack1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.SCALED, vsync=1)
clock = pygame.time.Clock() 
running = True
dt = 0

bg = pygame.image.load("background.png").convert()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
p = player.Player(pygame, screen)
B = boss.Boss(pygame, screen, p)
B.phase1()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(bg,(0,0))
    B.phase_ongoing(dt)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()