import pygame
import os

IMAGE_LIBRARY = {}
def get_image(path):
    global IMAGE_LIBRARY
    image = IMAGE_LIBRARY.get(path)
    if image == None:
        print(path)
        extended_path = path
        image = pygame.image.load(extended_path)
        IMAGE_LIBRARY[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((640, 480))

done = False
clock = pygame.time.Clock()

x = 20
y = 20
speed = 3

pygame.mixer.music.load('music/basic_song_01.mp3')
pygame.mixer.music.play(0)

font = pygame.font.SysFont("Arial", 72)

text = font.render("Title Screen of Doom!", True, (0, 128, 128))

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= speed
        if pressed[pygame.K_DOWN]:
            y += speed
        if pressed[pygame.K_LEFT]:
            x -= speed
        if pressed[pygame.K_RIGHT]:
            x += speed

    screen.fill((255, 255, 255))
    screen.blit(get_image('ball.png'), (x, y))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
