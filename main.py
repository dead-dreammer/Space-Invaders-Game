import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

#background
background = pygame.image.load("bg.jpg")
bg_resized = pygame.transform.scale(background, (1000, 600))

#background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("space.png")
px = 370
py = 500
pc = 0

enemyimg = [pygame.image.load("enemy.png"), pygame.image.load("enemy.png"), pygame.image.load("enemy1.png"), pygame.image.load("enemy1.png"), pygame.image.load("alien.png"), pygame.image.load("alien.png")]
ex = []
ey = []
exc = []
eyc = []
enemyResized  = []
 
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyResized.append(pygame.transform.scale(enemyimg[i], (80, 80)))
    ex.append(random.randint(0, 710))
    ey.append(random.randint(10, 100))
    exc.append(0.2)
    eyc.append(40)

# bullet
# read - you cant see the bullet on screen
# fire - the bullet is currently moving
bulletimg = pygame.image.load("missile.png")
bx = 0
by = 500
bxc = 0
byc = 1
bullet_state = "ready"




#score 
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textx = 10
texty = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255)) # typecasting changing an int into a str
    screen.blit(score, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bulletResized  = pygame.transform.scale(bulletimg, (40, 40))
    screen.blit(bulletResized, (x + 20, y + 10)) 
    # adding 16 and 10 makes the bullet come out of the centre of the spaceship

new_width = 80
new_height = 80
image_resized = pygame.transform.scale(playerimg, (new_width, new_height))


def player(x, y):
    screen.blit(image_resized, (x, y))

def enemy(x, y, i):
    screen.blit(enemyResized[i], (x, y))

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
                pc = - 0.3
                
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
                pc = 0.3

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    #only if its in ready state can a bullet be fired
                    bx = px # storing px value in bx
                    fire_bullet(bx, by)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()


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

   
    # enemy movement
    for i in range(num_of_enemies):
        ex[i] += exc[i]
        if ex[i] <= 0:
            exc[i] = 0.2
            ey[i] += eyc[i]
        elif ex[i] >= 720:
            exc[i] = -0.2
            ey[i] += eyc[i]

        #Collision
        collision = isCollision(ex[i], ey[i], bx, by)
        if collision:
            by = 500
            bullet_state = "ready"
            score_value += 1
            explosion = mixer.Sound("explosion.wav")
            explosion.play()
          
            ex[i] = random.randint(0, 710)
            ey[i] = random.randint(10, 100)

        enemy(ex[i], ey[i],i)

    #bullet movement
    if by <= 0 :
        by = 500
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bx, by) # ensures that the bullet keeps appearing on screen after its fired
        by -= byc

    

    player(px, py)
    show_score(textx, texty)
    pygame.display.update()