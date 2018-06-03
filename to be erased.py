import pygame
from pygame.locals import *
from random import *
from time import *
import time
#from threading import Thread

#           _____________________________
#__________/Crear pantalla
a=800 #ancho pantalla
b=600 #largo pantalla

black=(0,0,0)

root=pygame.display.set_mode((a,b))
pygame.display.set_caption("Juego")
c=pygame.time.Clock()

#           _____________________________
#__________/Cargar imagenes
Jug_w=pygame.image.load("Jug_w.png") #Jugador hacia arriba
Jug_a=pygame.image.load("Jug_a.png") #Jugador hacia la izquierda
Jug_s=pygame.image.load("Jug_s.png") #Jugador hacia abajo
Jug_d=pygame.image.load("Jug_d.png") #Jugador hacia la derecha
Jug_c=pygame.image.load("Jug_c.png") #Jugador centro
Jug=pygame.image.load("Jug_c.png") #Jugador
Aro=pygame.image.load("Aro.png") #Aro
fondo=pygame.image.load("fondo.jpg") #Fondo
Mira=pygame.image.load("mira.png") 

def gen_img(img,x,y): #Generar cualquier imagen
	root.blit(img,(x,y))
	pygame.display.update()
