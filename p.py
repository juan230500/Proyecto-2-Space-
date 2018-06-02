import pygame
from pygame.locals import *
from random import *
from time import *
from threading import Thread

global in1 #indicador para que el aro se sobre ponga a la nave
in1=1

pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

a=800
b=600 #medidas de la pantalla

root=pygame.display.set_mode((a,b))
pygame.display.set_caption("###")
c=pygame.time.Clock()

Jug=pygame.image.load("1.jpg") #Jugador
Aro=pygame.image.load("2.png") #Aro
fondo=pygame.image.load("fo.jpg") #Fondo

def car(x,y): #Generar jugador
	root.blit(Jug,(x,y))

def aro(x,y): #Generar aro
	root.blit(Aro,(x,y))

def exp(surf,x,y,xi,yi): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
	if x>500: #Si sobre pasa la medida 500x500 trapasa al jugaodr
		global in1
		in1=0
	surf=pygame.transform.scale(surf, (x, y))
	root.blit(surf,(xi,yi))
	

x_j=a*.45 #posicion del jugador
y_j=b*.5

xi_a,yi_a=300,300 #posicon inicial del aro


x_a=100
y_a=100
i=1 #indicar de parada del whhile principal
a=2 #incremetno de aro inicial


while i:
	root.fill(black)
	root.blit(fondo,(0,0))

	for e in pygame.event.get(): #Lee teclado y evento de cierre
		if e.type==pygame.QUIT:
			i=0
		if e.type==pygame.KEYDOWN:
			if e.key==pygame.K_LEFT:
				x_j-=30
			elif e.key==pygame.K_RIGHT:
				x_j+=30
		if e.type==pygame.KEYUP:
			if e.key==pygame.K_UP:
				y_j-=30
			elif e.key==pygame.K_DOWN:
				y_j+=30



	x_a+=a #aumenta el incremento de "exp"
	y_a+=a
	xi_a-=a/2 #desplaza el eje de imagen para dar efecto de crecer sobre sí misma
	yi_a-=a/2

	if x_a>600: #Si el aro mide más de 600x600 se resetean sus condiciones de inicio
		x_a,y_a=50,50
		in1=1
		xi_a,yi_a=randint(300,400),randint(300,400) #Se varía un poco el eje
		if a<12: a+=2 #Se limita la velocidad de incremento

	if in1: #si debe traspasarlo, entonces se genera primero el aro
		exp(Aro,x_a,y_a,xi_a,yi_a)
		car(x_j,y_j)
	else: #si no debe traspasarlo, entonces se genera primero el jugador
		car(x_j,y_j)
		exp(Aro,x_a,y_a,xi_a,yi_a)

	Jug=pygame.transform.scale(Jug, (100, 100)) #El jugador siempre debe medir 100x100
	
	pygame.display.update()
	c.tick(60)