import pygame
import random
import math

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
ey = random.randint(10, 100)
exc = 0.2 
eyc = 40

# bullet
# read - you cant see the bullet on screen
# fire - the bullet is currently moving
bulletimg = pygame.image.load("missile.png")
bx = 0
by = 500
bxc = 0
byc = 0.5
bullet_state = "ready"

score = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bulletResized  = pygame.transform.scale(bulletimg, (40, 40))
    screen.blit(bulletResized, (x + 20, y + 10)) 
    # adding 16 and 10 makes the bullet come out of the centre of the spaceship

new_width = 80
new_height = 80
image_resized = pygame.transform.scale(playerimg, (new_width, new_height))
enemyResized  = pygame.transform.scale(enemyimg, (new_width, new_height))

def player(x, y):
    screen.blit(image_resized, (x, y))

def enemy(x, y):
    screen.blit(enemyResized, (x, y))

def isCollision(ex, ey, bx, by):
    distance = math.sqrt(math.pow((ex - bx),2) + math.pow((ey - by),2))
    if distance < 27:
        return True
    else:
        return False

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

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    #only if its in ready state can a bullet be fired
                    bx = px # storing px value in bx
                    fire_bullet(bx, by)


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

    #bullet movement
    if by <= 0 :
        by = 500
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bx, by) # ensures that the bullet keeps appearing on screen after its fired
        by -= byc

    #Collision
    collision = isCollision(ex, ey, bx, by)
    if collision:
        by = 500
        bullet_state = "ready"
        score += 1
        print(score)
        ex = random.randint(0, 710)
        ey = random.randint(10, 100)

    player(px, py)
    enemy(ex, ey)
    pygame.display.update()