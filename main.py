import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("space.png")
px = 370
py = 500

new_width = 80
new_height = 80
image_resized = pygame.transform.scale(playerimg, (new_width, new_height))

def player():
    screen.blit(image_resized, (px, py))

running = True

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player()
    pygame.display.update()