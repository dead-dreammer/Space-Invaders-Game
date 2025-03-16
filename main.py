import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

#background
background = pygame.image.load("bg.jpg")
bg_resized = pygame.transform.scale(background, (1000, 600))

icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("space.png")
px = 370
py = 500
pc = 0

enemyimg = pygame.image.load("enemy.png")
ex = random.randint(0, 710)
ey = random.randint(50, 150)
exc = 0.2 
eyc = 40

new_width = 80
new_height = 80
image_resized = pygame.transform.scale(playerimg, (new_width, new_height))
enemyResized  = pygame.transform.scale(enemyimg, (new_width, new_height))

def player(x, y):
    screen.blit(image_resized, (x, y))

def enemy(x, y):
    screen.blit(enemyResized, (x, y))

running = True

while running:
    screen.fill((0, 0, 0))

    #background image
    screen.blit(bg_resized, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check if its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow is pressed")
                pc = - 0.2
                
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
                pc = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pc = 0 # stop the ship once the key is released
                print("Keystroke has been released")

    px += pc
    # adding boundary to space ship
    if px <= 0:
        px = 0
    elif px >= 720:
        px = 720

    ex += exc
    # enemy movement
    if ex <= 0:
        exc = 0.2
        ey += eyc
    elif ex >= 720:
        exc = -0.2
        ey += eyc

    player(px, py)
    enemy(ex, ey)
    pygame.display.update()