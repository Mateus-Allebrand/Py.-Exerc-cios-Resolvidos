#tentativa de fazer a musica tocar com pygame, não funcionou
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


