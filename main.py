import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("space.png")
px = 370
py = 500
pc = 0

new_width = 80
new_height = 80
image_resized = pygame.transform.scale(playerimg, (new_width, new_height))

def player(x, y):
    screen.blit(image_resized, (x, y))

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check if its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow is pressed")
                pc = 0.2
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
                pc = -0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pc = 0 # stop the ship once the key is released
                print("Keystroke has been released")

    px += pc
    player(px, py)
    pygame.display.update()