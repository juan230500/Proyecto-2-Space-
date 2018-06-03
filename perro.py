import pygame
from pygame.locals import *
from random import *
from time import *
import time
#from threading import Thread

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

#           _____________________________
#__________/Generar y reescalar imagenes
'''def car(x,y): #Generar jugador
	root.blit(Jug,(x,y))

def aro(x,y): #Generar aro
	root.blit(Aro,(x,y))

def mira(x,y): #Generar aro
	root.blit(Mira,(x,y))'''

def gen_img(img,x,y): #Generar cualquier imagen
	root.blit(img,(x,y))


def exp(surf,x,y,xi,yi): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
	global in1
	time.sleep(0.001)
	if x>500: #Si sobre pasa la medida 500x500 traspasa al jugaodr
		in1=0
	surf=pygame.transform.scale(surf, (x, y))
	root.blit(surf,(xi,yi))

def ev_choque(PosJug,l1,PosAro,l2):
	if PosAro[0]<=PosJug[0]<=PosAro[0]+l2 and PosAro[1]<=PosJug[1]<=PosAro[1]+l2:
		print("SI")
	else:
		print("NO")
	return


#           _____________________________
#__________/Posiciones

xi_a,yi_a=300,300 #posicon inicial del aro
x_a=100
y_a=100

i=1 #indicador de parada del while principal
a=6 #incremento de aro inicial



#           _____________________________
#__________/movimiento
while i:
	root.fill(black)
	root.blit(fondo,(0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			i=0

	teclas = pygame.key.get_pressed()

	if teclas[pygame.K_LEFT] or teclas[97]:
		if posX_jug>=10:
			posX_jug-=10
			Jug=pygame.transform.scale(Jug_a, (300, 150))
	elif teclas[pygame.K_RIGHT] or teclas[100]:
		if posX_jug<=499:
			posX_jug+=10
			Jug=pygame.transform.scale(Jug_d, (300, 150))
	elif teclas[pygame.K_UP] or teclas[119]:
		if posY_jug>=60:
			posY_jug-=10
			Jug=pygame.transform.scale(Jug_w, (300, 150))
	elif teclas[pygame.K_DOWN] or teclas[115]:
		if posY_jug<=445:
			posY_jug+=10
			Jug=pygame.transform.scale(Jug_s, (300, 150))

		


	if x_a>600: #Si el aro mide más de 600x600 se resetean sus condiciones de inicio
		x_a,y_a=50,50
		in1=1
		xi_a,yi_a=randint(100,500),randint(200,500) #Se varía un poco el eje
		if a<14: 
			a+=1 #Se limita la velocidad de incremento

	x_a+=int(a) #aumenta el incremento de "exp"
	y_a+=int(a)
	xi_a-=a//2 #desplaza el eje de imagen para dar efecto de crecer sobre sí misma
	yi_a-=a//2

	if x_a>500 and in1==1:
		ev_choque((posX_jug,posY_jug),150,(xi_a,yi_a),500)
	

	if in1: #si debe traspasarlo, entonces se genera primero el aro
		exp(Aro,x_a,y_a,xi_a,yi_a)
		gen_img(Jug,posX_jug,posY_jug)
	else: #si no debe traspasarlo, entonces se genera primero el jugador
		gen_img(Jug,posX_jug,posY_jug)
		exp(Aro,x_a,y_a,xi_a,yi_a)

	gen_img(Mira,posX_jug+121,posY_jug-50)

	Jug=pygame.transform.scale(Jug_c, (300, 150)) #El jugador siempre debe medir 300x150
	
	pygame.display.update()

	c.tick(60)
