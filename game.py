import pygame
import sys
import player
import boss
from button import Button

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1620, 1000),pygame.SCALED, vsync=1)
clock = pygame.time.Clock() 
running = True
dt = 0

bg = pygame.image.load("big-background.png").convert()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
p = player.Player(pygame, screen)
B = boss.Boss(pygame, screen, p)

def game_start():
    global running, dt
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(bg,(0,0))
        B.setup()
        B.phase_ongoing(dt)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        dt = clock.tick(60) / 1000
game_start()
def main_menu():
    while True:
        screen.fill("black")

        mouse = pygame.mouse.get_pos()
        menu_text =  "Game name"
        #Play_button = Button()

pygame.quit()