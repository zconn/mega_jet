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

SOUND_LIBRARY = {}
def play_sound (path):
    global SOUND_LIBRARY
    sound = SOUND_LIBRARY.get(path)
    if sound == None:
        extended_path = path
        print(extended_path)
        sound = pygame.mixer.Sound(extended_path)
        SOUND_LIBRARY[path] = sound
    sound.play()
    return None

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False
clock = pygame.time.Clock()

x = (SCREEN_WIDTH - 40) / 2
y = (SCREEN_HEIGHT - 40)
speed = 5

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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            play_sound("sound_effects/laser_shot_01.wav")

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
