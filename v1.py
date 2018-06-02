import pygame
from pygame.locals import *
from random import *
from time import *
from threading import Thread

#           _____________________________
#__________/Variables globales
global in1, posX_jug, posY_jug
in1=1	#indicador para que el aro se sobre ponga a la nave
posX_jug=300
posY_jug=300

pygame.init()

#           _____________________________
#__________/Crear pantalla
a=800 #ancho pantalla
b=600 #largo pantalla
black=(0,0,0)

root=pygame.display.set_mode((a,b))
pygame.display.set_caption("###")
c=pygame.time.Clock()

#           _____________________________
#__________/Cargar imagenes
Jug=pygame.image.load("1.jpg") #Jugador
Aro=pygame.image.load("2.png") #Aro
fondo=pygame.image.load("fondo.jpg") #Fondo

#           _____________________________
#__________/Generar y reescalar imagenes
def car(x,y): #Generar jugador
	root.blit(Jug,(x,y))

def aro(x,y): #Generar aro
	root.blit(Aro,(x,y))

def exp(surf,x,y,xi,yi): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
	if x>500: #Si sobre pasa la medida 500x500 traspasa al jugaodr
		global in1
		in1=0
	surf=pygame.transform.scale(surf, (x, y))
	root.blit(surf,(xi,yi))


#           _____________________________
#__________/Posiciones
x_j=a*.45 #posicion del jugador
y_j=b*.5

xi_a,yi_a=300,300 #posicon inicial del aro
x_a=100
y_a=100

i=1 #indicar de parada del whhile principal
a=2 #incremetno de aro inicial


#           _____________________________
#__________/movimiento
while i:
	root.fill(black)
	root.blit(fondo,(0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			i=0

	teclas = pygame.key.get_pressed()

	if teclas[pygame.K_LEFT]:
		if posX_jug>=10:
			posX_jug-=10
			x_j-=10
		else:
			posX_jug-=0
	if teclas[pygame.K_RIGHT]:
		if posX_jug<=590:
			posX_jug+=10
			x_j+=10
		else:
			posX_jug+=0
	if teclas[pygame.K_UP]:
		if posY_jug>=10:
			posY_jug-=10
			y_j-=10
		else:
			posX_jug-=0
	if teclas[pygame.K_DOWN]:
		if posY_jug<=490:
			posY_jug+=10
			y_j+=10
		else:
			posY_jug+=0



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
		car(posX_jug,posY_jug)
	else: #si no debe traspasarlo, entonces se genera primero el jugador
		car(posX_jug,posY_jug)
		exp(Aro,x_a,y_a,xi_a,yi_a)

	Jug=pygame.transform.scale(Jug, (100, 100)) #El jugador siempre debe medir 100x100
	
	pygame.display.update()
	c.tick(60)
