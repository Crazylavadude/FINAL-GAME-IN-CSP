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
death_screen_bg = pygame.image.load("death.png").convert()

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
        if(B.player_health <= 0):
            going = True
            while (going and running):
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        going = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if(mouse[0] < 1300 and mouse[0] > 300 and mouse[1] <680 and mouse[1] >480):
                            going = False
                            B.phase1()
                screen.blit(death_screen_bg, (0, 0))
                pygame.display.flip()



        # limits FPS to 60
        dt = clock.tick(60) / 1000


main_screen_bg = pygame.image.load("start-screen.png").convert()
def main_menu():
    global running
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(mouse[0] < 1095 and mouse[0] > 525 and mouse[1] <645 and mouse[1] >455):
                    game_start()
        screen.blit(main_screen_bg,(0,0))

        
        pygame.display.flip()
        #Play_button = Button()
    
main_menu()
pygame.quit()