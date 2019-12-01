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
SHIP_WIDTH = 32
SHIP_HEIGHT = 32
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False
clock = pygame.time.Clock()

x = (SCREEN_WIDTH - SHIP_WIDTH) / 2
y = (SCREEN_HEIGHT - SHIP_HEIGHT)
speed = 5

#MUSIC FUNCTION
#pygame.mixer.music.load('music/basic_song_01.mp3')
#pygame.mixer.music.play(0)

#TEXT FUNCTION
#font = pygame.font.SysFont("Arial", 72)
#text = font.render("Title Screen of Doom!", True, (0, 128, 128))

def move_ship(position, speed, direction):
    if direction == "up" and position != 0:
        position = position - speed
        if position < 0:
            position = 0
    if direction == "down" and position != SCREEN_HEIGHT - SHIP_HEIGHT:
        position = position + speed
        if position > SCREEN_HEIGHT - SHIP_HEIGHT:
            position = SCREEN_HEIGHT - SHIP_HEIGHT
    if direction == "left" and position != 0:
        position = position - speed
        if position < 0:
            position = 0
    if direction == "right" and position != SCREEN_WIDTH - SHIP_WIDTH:
        position = position + speed
        if position > SCREEN_WIDTH - SHIP_WIDTH:
            position = SCREEN_WIDTH - SHIP_WIDTH
    return position

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     play_sound("sound_effects/laser_shot_01.wav")

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y = move_ship(y, speed, "up") 
    if pressed[pygame.K_DOWN]:
        y = move_ship(y, speed, "down")
    if pressed[pygame.K_LEFT]:
        x = move_ship(x, speed, "left")
    if pressed[pygame.K_RIGHT]:
        x = move_ship(x, speed, "right")

    screen.fill((255, 255, 255))
    screen.blit(get_image('images\ship_shape.png'), (x, y))
    #screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)
