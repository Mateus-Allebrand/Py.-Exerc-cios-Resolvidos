#Programa deveria tocar uma música em mp3 usando pygame, porém não esta funcionando o código.Mas eu consegui executar esse programa usando outro módulo.




#Programa principal.
import pygame
pygame.init()
pygame.mixer.music.load('world01.py\ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
