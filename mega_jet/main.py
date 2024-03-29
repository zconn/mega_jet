import pygame
import os

IMAGE_LIBRARY = {}
def get_image(path):
    global IMAGE_LIBRARY
    image = IMAGE_LIBRARY.get(path)
    if image == None:
        print(path)
        extended_path = os.path.normpath(path)
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
pygame.mixer.music.load('music/basic_song_01.mp3')
pygame.mixer.music.play(0)

#TEXT FUNCTION
#font = pygame.font.SysFont("Arial", 72)
#text = font.render("Title Screen of Doom!", True, (0, 128, 128))

#rendering stuff should go here
bullets = []
missiles = []

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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            play_sound("sound_effects/laser_shot_01.wav")
            bullets.append([x + SHIP_WIDTH/2, y])

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
            #TODO GET MISSILE SOUND
            # play_sound("sound_effects/laser_shot_01.wav")
            missiles.append([x + SHIP_WIDTH/2, y])

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y = move_ship(y, speed, "up") 
    if pressed[pygame.K_DOWN]:
        y = move_ship(y, speed, "down")
    if pressed[pygame.K_LEFT]:
        x = move_ship(x, speed, "left")
    if pressed[pygame.K_RIGHT]:
        x = move_ship(x, speed, "right")

    #bullet handler, movement and removal at the end of the screen
    for b in range(len(bullets)):
        bullets[b][1] -= 10

    for b in range(len(missiles)):
        missiles[b][1] -= 8

    for bullet in bullets[:]:
        if bullet[1] < -10:
            bullets.remove(bullet)

    for missile in missiles[:]:
        if missile[1] < -10:
            missiles.remove(missile)

    screen.fill((200, 200, 120))
    screen.blit(get_image('images/ship_shape.png'), (x, y))
    for bullet in bullets:
        screen.blit(get_image('images/bullet-basic.png'), pygame.Rect(bullet[0], bullet[1], 0, 0))
    for missile in missiles:
        screen.blit(get_image('images/missile-basic.png'), pygame.Rect(missile[0], missile[1], 0, 0))
    #screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()
    clock.tick(60)


