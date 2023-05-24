import pygame, math, sys, threading, random
from pygame.locals import *
import pygame_textinput
from pygame_textinput import *
import pygame_gui
pygame.init()
screen_size = screen_width, screen_height = 1280, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Chromatic Codebreaker")
clock = pygame.time.Clock()

color_dictionary = {
        0 : 'blue',
        1 : 'black',
        2 : 'green',
        3 : 'red',
        4 : 'orange',
        5 : 'purple',
        6 : 'yellow',
        7 : 'gray',
        8 : 'pink'                   
}

black = (15, 15, 15)
red = (255, 0, 0)
white = (255, 255, 255)
gray = (145, 145, 145)
light_green = (144, 238, 144)
light_blue = (173, 216, 230)
coral = (255, 127, 80)

music_paused = False

play_music_button = pygame.image.load('play_button.png').convert_alpha()
play_music_button = pygame.transform.scale(play_music_button, (100, 100))

pause_music_button = pygame.image.load('pause_button.png').convert_alpha()
pause_music_button = pygame.transform.scale(pause_music_button, (100, 100))

up_arrow = pygame.image.load('arrow.png').convert_alpha()
up_arrow = pygame.transform.scale(up_arrow, (100, 58.8))
down_arrow = pygame.transform.rotate(up_arrow.copy(), 180)

shrinked_up_arrow = pygame.transform.scale(up_arrow.copy(), (90, 52.9))
shrinked_down_arrow = pygame.transform.rotate(shrinked_up_arrow.copy(), 180)

images = []

blue_circle = pygame.image.load('blue_circle.png').convert_alpha()
blue_circle = pygame.transform.scale(blue_circle, (150, 300))
images.append(blue_circle)

black_circle = pygame.image.load('black_circle.png').convert_alpha()
black_circle = pygame.transform.scale(black_circle, (150, 300))
images.append(black_circle)

green_circle = pygame.image.load('green_circle.png').convert_alpha()
green_circle = pygame.transform.scale(green_circle, (150, 300))
images.append(green_circle)

red_circle = pygame.image.load('red_circle.png').convert_alpha()
red_circle = pygame.transform.scale(red_circle, (150, 300))
images.append(red_circle)

orange_circle = pygame.image.load('orange_circle.png').convert_alpha()
orange_circle = pygame.transform.scale(orange_circle, (150, 300))
images.append(orange_circle)

purple_circle = pygame.image.load('purple_circle.png').convert_alpha()
purple_circle = pygame.transform.scale(purple_circle, (150, 300))
images.append(purple_circle)

yellow_circle = pygame.image.load('yellow_circle.png').convert_alpha()
yellow_circle = pygame.transform.scale(yellow_circle, (150, 300))
images.append(yellow_circle)

gray_circle = pygame.image.load('gray_circle.png').convert_alpha()
gray_circle = pygame.transform.scale(gray_circle, (150, 300))
images.append(gray_circle)

pink_circle = pygame.image.load('pink_circle.png').convert_alpha()
pink_circle = pygame.transform.scale(pink_circle, (150, 300))
images.append(pink_circle)

pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)

