from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                    # 
import winsound                     # Playsound
import os                           # ruta = os.path.join('')                       # time.sleep(x)
from tkinter import messagebox # AskYesNo ()
from random import *                # randint()
import pygame
from pygame.locals import *
from time import *

#______________/Sección de funciones a usar a lo largo del programa
def cargarImg(nombre): # carga una imagen de la carpeta adyacente al archivo img a una variable
    ruta=os.path.join('img',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

def inn(el,li): # devuelve True si "el" se haya en "li", similar a la keyword "in"
    if li==[]:
        return False
    if el==li[0]:
        return True
    return inn(el,li[1:])

def innli(li1,li2): #aplica el "inn" a todos los elementos de ambas listas
	if li1==[]:
		return False
	if inn(li1[0],li2):
		return True
	else:
		return innli(li1[1:],li2)
	    
def lenn(li):
    if li==[] or li=="":
        return 0
    return 1+lenn(li[1:])

def pasar():
    return

def invdic(dic):
    lk=list(dic.keys())
    lv=list(dic.values())
    def invdic2(dic,lk,lv,dic2={}):
        if lk==[]:
            return dic2
        dic2[lv[0]]=lk[0]
        return invdic2(dic,lk[1:],lv[1:],dic2)
    return invdic2(dic,lk,lv,{})

def suli(li,j):
    if li==[]:
	    return []
    else:
	    return [li[0][j]]+suli(li[1:],j)

def high():
    file=open("pts0.txt","r")
    a=file.readline()
    file.close()
    try:
        a=a.split(",")
        a=a[1][1:]
        return int(a)
    except:
        return 0

def splitt(st,deli):
    def delim(st,deli,res="",ind=0):
        if st=="" or st[0]==deli:
            return res,ind
        else:
            return delim(st[1:],deli,res+st[0],ind+1)
    def splitt_aux(st,deli,res=[]):
        if st=="":
            return res
        elif st[0]==deli:
            return splitt_aux(st[1:],deli,res)
        else:
            b=delim(st,deli)
            res+=[b[0]]
            return splitt_aux(st[b[1]+1:],deli,res)
    return splitt_aux(st,deli,[])



#______________/Sección de manejo de archivos\______________

#_________________/Generar lista aleatoria de jugadores
def escribir_1(arch):
    from random import randint
    file=open(arch,"w")

    def gen(lon,res):
        v="aaeeuio"
        c="qwrrtypssdfghjklzxcvbnm"
        punt_max=20
        if lon==0 or lon==1:
            i=randint(0,punt_max)
            return res.capitalize()+","+str(i)
        else:
            i=randint(0,len(c)-1)
            j=randint(0,len(v)-1)
            return gen(lon-2,res+c[i]+v[j])

    def gen_mult(cant,res):
        if cant==0:
            return res
        else:
            i=randint(2,8)
            return gen_mult(cant-1,res+gen(i,"")+"\n")

    nom=gen_mult(19,"")
    file.write(nom)
    file.close()

#_________________/Leer lista de jugadores

def leer(arch):
    file=open(arch,"r")

    def agrupar(file):
        c=0
        l=[]
        while(c!=""):
            c=file.readline()
            c=c[:-1]
            l+=[c]
        l.pop(-1)
        return l

    def trad(st):
        t=["",0]
        for i in range(len(st)):
            if st[i]==",":
                t[1]=int(st[i+1:])
                break
            else:
                t[0]+=st[i]
        return tuple(t)

    l=[]
    for i in agrupar(file):
        l+=[trad(i)]

    file.close()
    return l



#_________________/Ordenar lista de jugadores
def ordenar(li):
    def quicksort(L, first, last):
        # definimos los índices y calculamos el pivote
        i = first
        j = last    
        pivote = (L[i][1] + L[j][1]) / 2

        # iteramos hasta que i no sea menor que j
        while i < j:
            # iteramos mientras que el valor de L[i] sea menor que pivote
            while L[i][1] < pivote:
                # Incrementamos el índice
                i+=1
            # iteramos mientras que el valor de L[j] sea mayor que pivote
            while L[j][1] > pivote:
                # decrementamos el índice
                j-=1
            # si i es menor o igual que j significa que los índices se han cruzado
            if i <= j:
                # creamos una variable temporal para guardar el valor de L[j]
                x = L[j]
                # intercambiamos los valores de L[j] y L[i]
                L[j] = L[i]
                L[i] = x
                # incrementamos y decrementamos i y j respectivamente
                i+=1
                j-=1

        # si first es menor que j mantenemos la recursividad
        if first < j:
            L = quicksort(L, first, j)
        # si last es mayor que i mantenemos la recursividad
        if last > i:
            L = quicksort(L, i, last)

        # devolvemos la lista ordenada
        return L

    return quicksort(li,0,len(li)-1)

def ordenar2():
    a=leer("Jug.txt")
    a=ordenar(a)
    b=""
    for i in range(1,6):
    	b+=(a[-i][0]+","+str(a[-i][1])+"\n")
    file=open("t.txt","w")
    file.write(b)





#______________/Sección de funciones de música y sonidos
def off():
    winsound.PlaySound(None, winsound.SND_ASYNC)

    
def play1():
    off()
    def Song1():
        winsound.PlaySound('song1.wav', winsound.SND_ASYNC)
    ''''imagen = cargarImg("img1.gif")
    imagenc.config(image=imagen)'''
    p1=Thread(target=Song1,args=())
    p1.start()
    root.mainloop()

def play2():
    off()
    def Song2():
        winsound.PlaySound('song2.wav', winsound.SND_ASYNC)
    '''imagen2 = cargarImg("img2.gif")
    imagenc.config(image=imagen2)'''
    p2=Thread(target=Song2,args=())
    p2.start()
    root.mainloop()


def playdis():
    def Songdis():
        winsound.PlaySound('songdis.wav', winsound.SND_ASYNC)
    p=Thread(target=Songdis,args=())
    p.start()

#______________/Sección de variables predefinidas con uso en todo el programa

global li_img
li_img=['1_ar.gif','1_de.gif','1_ab.gif','1_iz.gif']

global sel_esc
sel_esc=0

global dft
dft="1" #1: asteroides 0:aros

sel_esc=0

#______________/Sección de idomas

global dic_trad,dic_trad_es,dic_trad_en

dic_trad_es=["Ventana principal","Introduzca el nombre \n (máx 10 caracteres)","Puntuaciones",'Atrás',"Juego",
             "Balas restantes: ","Enemigos restantes: ","arriba: w \nabajo: s \nizquierda: a \nderecha: d \n disparo: espaciadora",
             "Nombre debe ser menor de 10 caracteres","Introduzca nombre","Jugador: ","Opciones","Puntaje máximo: ",
             "Nivel ","Mapa ","Aleatorio", "Reiniciar puntuaciones","Clave","Clave érronea","Reiniciar puntajes (requiere clave)","Dificultad",
             "\tNombre\t\tPts\tDificultad\tFecha\n", "Juego de Tanques", "Puntuación alcanzada= ","Canción ","Parar","""******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Introducción a la programación
País de Producción: Costa Rica
Profesor: Milton Villegas Lemus
Como implementar: Se invoca con F5 desde el Idle del código
Programa: I Proyecto
Autor: Juan Pablo Alvarado Villalobos
Carné: 2018135360
Lenguaje: Python 3.6
Versión: 7.1
Ult.Fecha de mod: 22//18
******************************************************************""","Hacer clic en la pantalla para usar el teclado"]

dic_trad_en=["Main window","Enter the name \n (max 10 characters)","Scores",'Back',"Game",
             "Remaining bullets: ", "Remaining enemies: ", " up: w \n down: s \n left: a \n right: d \n shot: space",
             "Name must be less than 10 characters", "Enter name", "Player: ", "Settings","Highscore: ",
             "Level ","Map ","Random","Restart scores","Key","Wrong key","Restart scores (requires password)","Difficulty",
             "\tName\t\tPts\tDifficulty\t\tDate\n", "Game of Tanks", "Score reached= ","Song ","Stop", """******************************************************************
Institute: Tecnológico de Costa Rica
Career :Ing. Computadores 
Course: Introducción a la programación
Country of Production: Costa Rica
Teacher: Milton Villegas Lemus
How to implement: It is invoked with F5 from the Idle of the code
Program: I Proyecto
Author: Juan Pablo Alvarado Villalobos
Cardé: 2018135360
Language: Python 3.6
Version: 7.1
Last modified date: 22//18
******************************************************************""","Click on the screen to use the keyboard"]


dic_trad=dic_trad_en #lista con todas las palabras en dos idiomas



def inter(): #función para intercambiar los idiomas
    """
******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Intro a la programación
Como implementar: se invoca con inter()
Módulo : intercambio de idiomas
Autores : Juan Pablo Alvarado
Lenguaje: Python 3.6
Version : 1.0
Ult.Fecha de mod: 1/5/18
Entradas : ninguna
Restricciones: ninguna
Salidas: ninguna
******************************************************************"""

    winsound.Beep(100,2)
    global dic_trad,dic_trad_en
    if dic_trad[0]=="Ventana principal":
        dic=dic_trad_en
        Btn4.config(text="Español")
        img_auxes=cargarImg("us.gif")
        Btn4.image=(img_auxes)
        Btn4.config(image=img_auxes)
    else:
        dic=dic_trad_es
        Btn4.config(text="English")
        img_auxen=cargarImg("mex.gif")
        Btn4.image=(img_auxen)
        Btn4.config(image=img_auxen)
        
    dic_trad=dic
    
    L_vr.config(text=dic[1])
    L_vr1.config(text=dic[22])
    root.title(dic[0])
    Btn1.config(text=dic[2])
    Btn3.config(text=dic[4])
    Btn6.config(text=dic[11])
    Btn_song1.config(text=dic[24]+'1')
    Btn_song2.config(text=dic[24]+'2')
    Btn_song0.config(text=dic_trad[25])

print(len(dic_trad))




ordenar2() #se ajustan las puntuaciones desde el inico

#______________/Sección de ventana principal
#Se define la ventana principal=>
root=Tk()
root.title(dic_trad[0])
root.geometry("800x600+100+50")
root.minsize(800,600)
root.resizable(NO,NO)
root.title()


C_root=Canvas(root,width=800,height=600,bg="grey")
C_root.place(x=0,y=0)
CE0=cargarImg("fon.gif")
C_root.create_image(400,300,image=CE0)

#______________/Subsección de imágenes
CE1=cargarImg("fonp.gif")
CE2=cargarImg("foni.gif")
CE3=cargarImg("fons.gif")


L_vr1=Label(C_root,text=dic_trad[22],bg="grey",fg="black",font=('Eras Bold ITC',32))
L_vr1.place(x=50,y=10)

CE=cargarImg("A.gif")
imagen_cancion=Label(C_root,bg='white')
imagen_cancion.place(x=80,y=100)
imagen_cancion.config(image=CE)


L_vr=Label(C_root,text=dic_trad[1],bg="grey",fg="black",font=('Eras Bold ITC',14))
L_vr.place(x=500,y=350)


E_nombre=Entry(C_root,width=20,font=('Eras Bold ITC',16))
E_nombre.place(x=500,y=400)

Btn_song1 = Button(C_root,text=dic_trad[24]+'1',command=play1,bg='green',fg='white',font=('Eras Bold ITC',12))
Btn_song1.place(x=100,y=550)


Btn_song2=Button(C_root,text=dic_trad[24]+'2',command=play2,bg='green',fg='white',font=('Eras Bold ITC',12))
Btn_song2.place(x=200,y=550)

Btn_song0=Button(C_root,text=dic_trad[25],command=off,bg='green',fg='white',font=('Eras Bold ITC',12))
Btn_song0.place(x=300,y=550)




#______________/Sección de ventana de puntuaciones
def Ventana1():
    datos=""
    for i in leer("t.txt"):
    	print(50-len(i[0]))
    	datos+=(i[0]+str(i[1]).rjust(50-len(i[0])+len(i[1])," ")+"\n")
    texal="Top 5".center(50,"=")
    texad=dic_trad[21]
    datos=texad+datos
    
    root.withdraw()
    v1=Toplevel(root)
    v1.title(dic_trad[2])
    v1.geometry("800x600+100+50")
    v1.minsize(800,600)
    v1.resizable(NO,NO)

    C_v1=Canvas(v1,width=800,height=600,bg="black")
    C_v1.place(x=0,y=0)
    C_v1.create_image(400,300,image=CE1)

    fondoImg=cargarImg('top.gif')
    F_v1=Label(C_v1, image=fondoImg,bg='black')
    F_v1.photo=fondoImg
    F_v1.place(x=200,y=20)

    L_v1=Label(v1,text=datos,bg="black",fg="white",font=('Eras Bold ITC',14),justify=LEFT)
    L_v1.place(x=50,y=200)

    def reiniciar():
        """
******************************************************************
Instituto: Tecnológico de Costa Rica
Carrera :Ing. Computadores 
Curso: Intro a la programación
Como implementar: se invoca con reiniciar()
Módulo : reiniciar puntuaciones
Autores : Juan Pablo Alvarado
Lenguaje: Python 3.6
Version : 1.0
Ult.Fecha de mod: 1/5/18
Entradas : ninguna
Restricciones: ninguna
Salidas: ninguna
******************************************************************"""
        clave=str(E_clave.get())
        if clave!="luca":
            messagebox.showinfo(":(",dic_trad[18])
            return
        file=open("pts0.txt","w") #archivo de puntuaciones
        file.write("")
        file.close()
        ordenar2()
        
        file=open("pts02.txt","r+") #archivo de puntuaciones
        datos=file.read()
        texal="Top 5".center(50,"=")
        texad=dic_trad[21]
        datos=texad+datos
        file.close()
        
        L_v1.configure(text=datos)
        
    L_v1r=Label(v1,text=dic_trad[19],bg="grey",fg="black",font=('Eras Bold ITC',12),justify=LEFT)
    L_v1r.place(x=100,y=500)
    E_clave=Entry(C_v1,width=20,font=('Eras Bold ITC',12))
    E_clave.place(x=100,y=530)
    Btn_res = Button(C_v1,text=dic_trad[16],command=reiniciar,bg='grey',fg='black',font=('Eras Bold ITC',12))
    Btn_res.place(x=100,y=560)
    
    def back():
        v1.destroy()
        root.deiconify()

    home=cargarImg("home.gif")
    Btn_back1 = Button(C_v1, image=home ,command=back, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=650,y=500)

#______________/Sección de ventana de about
def Ventana2():
    root.withdraw()
    v2=Toplevel(root)
    v2.title("About")
    v2.geometry("800x600+100+50")
    v2.minsize(800,600)
    v2.resizable(NO,NO)
    
    C_v2=Canvas(v2,width=800,height=600,bg="light green")
    C_v2.place(x=0,y=0)
    C_v2.create_image(400,300,image=CE2)
    
    tex=dic_trad[26]

    L_v2=Label(v2,text=tex,bg="white",fg="#000000",font=('Eras Bold ITC',12),justify=CENTER)
    L_v2.place(x=130,y=20)

    fondoImg=cargarImg('tec.gif')
    F_v2=Label(C_v2, image=fondoImg,bg='#000000')
    F_v2.photo=fondoImg
    F_v2.place(x=400,y=300)

    fondoImg1=cargarImg('per.gif')
    F_v21=Label(C_v2, image=fondoImg1,bg='#000000')
    F_v21.photo=fondoImg1
    F_v21.place(x=150,y=300)
    
    def back():
        v2.destroy()
        root.deiconify()

    home=cargarImg("home.gif")
    Btn_back1 = Button(C_v2, image=home ,command=back, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=700,y=500)

#______________/Sección de ventana de puntuaciones
def Ventana3():
    root.withdraw()
    v3=Toplevel(root)
    v3.title(dic_trad[11])
    v3.geometry("800x600+100+50")
    v3.minsize(800,600)
    v3.resizable(NO,NO)

    C_v3=Canvas(v3,width=800,height=600,bg="black")
    C_v3.place(x=0,y=0)
    C_v3.create_image(400,300,image=CE3)
    

    
    #______________/Subsección de casillas
    C_v31=Canvas(v3,bg="grey", width=200,height=200)
    C_v31.place(x=50,y=50)

    C_v32=Canvas(v3,bg="grey", width=300,height=250)
    C_v32.place(x=400,y=50)

    C_v33=Canvas(v3,bg="grey", width=200,height=200)
    C_v33.place(x=50,y=300)
    
    #______________/Subsección de mapas
    if sel_esc==0:
        fondoImg=cargarImg('m1.gif')
    if sel_esc==1:
        fondoImg=cargarImg('m2.gif')
    if sel_esc==2:
        fondoImg=cargarImg('m3.gif')
    if sel_esc==3:
        fondoImg=cargarImg('m4.gif')
    if sel_esc==4:
        fondoImg=cargarImg('in.gif')
    F_v3m=Label(C_v31, image=fondoImg,bg="grey")
    F_v3m.photo=fondoImg
    F_v3m.place(x=95,y=50)

    
    def m1():
        global sel_esc
        sel_esc=0
        fondoImg=cargarImg('m1.gif')
        F_v3m.photo=fondoImg
        F_v3m.config(image=fondoImg)

    def m2():
        global sel_esc
        sel_esc=1
        fondoImg=cargarImg('m2.gif')
        F_v3m.photo=fondoImg
        F_v3m.config(image=fondoImg)
        
    def m3():
        global sel_esc
        sel_esc=2
        fondoImg=cargarImg('m3.gif')
        F_v3m.photo=fondoImg
        F_v3m.config(image=fondoImg)

    def m4():
        global sel_esc
        sel_esc=3
        fondoImg=cargarImg('m4.gif')
        F_v3m.photo=fondoImg
        F_v3m.config(image=fondoImg)

    def ma():
        global sel_esc
        sel_esc=4
        fondoImg=cargarImg('in.gif')
        F_v3m.photo=fondoImg
        F_v3m.config(image=fondoImg)

    L_v3m=Label(C_v31,text=dic_trad[14],bg="grey",fg="black",font=('Eras Bold ITC',20),justify=LEFT)
    L_v3m.place(x=65,y=2)

    m=30
    Btn_m1 = Button(C_v31,text=dic_trad[14]+"1",command=m1,bg='white',fg='green')
    Btn_m1.place(x=2,y=40)
    Btn_m2 = Button(C_v31,text=dic_trad[14]+"2",command=m2,bg='white',fg='green')
    Btn_m2.place(x=2,y=40+m*1)
    Btn_m3 = Button(C_v31,text=dic_trad[14]+"3",command=m3,bg='white',fg='green')
    Btn_m3.place(x=2,y=40+m*2)
    Btn_m4 = Button(C_v31,text=dic_trad[14]+"4",command=m4,bg='white',fg='green')
    Btn_m4.place(x=2,y=40+m*3)
    Btn_ma = Button(C_v31,text=dic_trad[14]+dic_trad[15],command=ma,bg='white',fg='green')
    Btn_ma.place(x=2,y=40+m*4)
    


    #______________/Subsección de dificultades
    if dft=="1":
        fondoImg=cargarImg('A1.gif')
    if dft=="2":
        fondoImg=cargarImg('B1.gif')
    if dft=="3":
        fondoImg=cargarImg('C1.gif')

    F_v3=Label(C_v32, image=fondoImg,bg='grey')
    F_v3.photo=fondoImg
    F_v3.place(x=30,y=45)

    def dft1():
        global dft
        dft="1"
        fondoImg=cargarImg('A1.gif')
        F_v3.photo=fondoImg
        F_v3.config(image=fondoImg)
        Btn_dft1.configure(fg="blue")
        Btn_dft2.configure(fg="green")
        Btn_dft3.configure(fg="green")
        

    def dft2():
        global dft
        dft="2"
        fondoImg=cargarImg('B1.gif')
        F_v3.photo=fondoImg
        F_v3.config(image=fondoImg)
        Btn_dft1.configure(fg="green")
        Btn_dft2.configure(fg="blue")
        Btn_dft3.configure(fg="green")

    def dft3():
        global dft
        dft="3"
        fondoImg=cargarImg('C1.gif')
        F_v3.photo=fondoImg
        F_v3.config(image=fondoImg)
        Btn_dft1.configure(fg="green")
        Btn_dft2.configure(fg="green")
        Btn_dft3.configure(fg="blue")
        
    L_v3=Label(C_v32,text=dic_trad[20],bg="grey",fg="black",font=('Eras Bold ITC',20),justify=LEFT)
    L_v3.place(x=80,y=2)
    
    Btn_dft1 = Button(C_v32,text=dic_trad[13]+"1",command=dft1,bg='white',fg='green')
    Btn_dft1.place(x=30,y=200)
    Btn_dft2 = Button(C_v32,text=dic_trad[13]+"2",command=dft2,bg='white',fg='green')
    Btn_dft2.place(x=130,y=200)
    Btn_dft3 = Button(C_v32,text=dic_trad[13]+"3",command=dft3,bg='white',fg='green')
    Btn_dft3.place(x=230,y=200)

    
    #______________/Subsección de avatares
    
    def c_avatar1():
        global li_img
        li_img=['1_ar.gif','1_de.gif','1_ab.gif','1_iz.gif']
        Btn_a1.configure(bg="blue")
        Btn_a2.configure(bg="green")
        Btn_a3.configure(bg="green")
        Btn_a4.configure(bg="green")
    def c_avatar2():
        global li_img
        li_img=['2_ar.gif','2_de.gif','2_ab.gif','2_iz.gif']
        Btn_a1.configure(bg="green")
        Btn_a2.configure(bg="blue")
        Btn_a3.configure(bg="green")
        Btn_a4.configure(bg="green")
    def c_avatar3():
        global li_img
        li_img=['3_ar.gif','3_de.gif','3_ab.gif','3_iz.gif']
        Btn_a1.configure(bg="green")
        Btn_a2.configure(bg="green")
        Btn_a3.configure(bg="blue")
        Btn_a4.configure(bg="green")
    def c_avatar4():
        global li_img
        li_img=['4_ar.gif','4_de.gif','4_ab.gif','4_iz.gif']
        Btn_a1.configure(bg="green")
        Btn_a2.configure(bg="green")
        Btn_a3.configure(bg="green")
        Btn_a4.configure(bg="blue")


    L_v3=Label(C_v33,text="Avatar",bg="grey",fg="black",font=('Eras Bold ITC',20),justify=LEFT)
    L_v3.place(x=50,y=2)
        
    imb_b=cargarImg('1_ar.gif')
    Btn_a1 = Button(C_v33,text="avatar 1",command=c_avatar1,bg='green',fg='green',image=imb_b)
    Btn_a1.image=imb_b
    Btn_a1.place(x=20,y=40)
    
    imb_b=cargarImg('2_ar.gif')
    Btn_a2 = Button(C_v33,text="avatar 2",command=c_avatar2,bg='green',fg='green',image=imb_b)
    Btn_a2.image=imb_b
    Btn_a2.place(x=20+100,y=40)
    
    
    imb_b=cargarImg('3_ar.gif')
    Btn_a3 = Button(C_v33,text="avatar 3",command=c_avatar3,bg='green',fg='green',image=imb_b)
    Btn_a3.image=imb_b
    Btn_a3.place(x=20,y=40+100)
    
    imb_b=cargarImg('4_ar.gif')
    Btn_a4 = Button(C_v33,text="avatar 4",command=c_avatar4,bg='green',fg='green',image=imb_b)
    Btn_a4.image=imb_b
    Btn_a4.place(x=20+100,y=40+100)

    def back():
        v3.destroy()
        root.deiconify()

    Silueta=cargarImg("SH.png")
    Sh_cv=Label(C_v3, image=Silueta, bg='white')
    Sh_cv.photo=Silueta
    Sh_cv.place(x=500,y=310)

    flchi=cargarImg("flechaizquierda.gif")
    Btn_fi = Button(C_v3, image=flchi , command=back,fg="#000000")
    Btn_fi.image=flchi
    Btn_fi.place(x=400,y=450)

    flchd=cargarImg("flechaderecha.gif")
    Btn_fd = Button(C_v3, image=flchd , command=back,fg="#000000")
    Btn_fd.image=flchd
    Btn_fd.place(x=600,y=450)
        
    home=cargarImg("home.gif")
    Btn_back1 = Button(C_v3, image=home ,command=back, fg = "#000000")
    Btn_back1.image = home
    Btn_back1.place(x=650,y=500)


        
    
    
#______________/Sección de ventana de de juego
def VentanaJuego(nombre):
	va=Toplevel()
	va.geometry("800x600+100+50")
	va.minsize(800,600)
	va.resizable(NO,NO)

	C_va=Canvas(va,width=800,height=600,bg="light green")
	C_va.place(x=0,y=0)
	C_va.create_image(400,300,image=CE2)

	tex=dic_trad[26]

	L_va=Label(va,text=tex,bg="white",fg="#000000",font=('Eras Bold ITC',12),justify=CENTER)
	L_va.place(x=130,y=20)



	

	def Juego(dft):
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

		root_jueg=pygame.display.set_mode((a,b))
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
		#__________/Efectos de sonido
		colision_sonido= pygame.mixer.Sound('crash.wav')

		#           _____________________________
		#__________/Generar y reescalar imagenes
		'''def car(x,y): #Generar jugador
			root_jueg.blit(Jug,(x,y))

		def aro(x,y): #Generar aro
			root_jueg.blit(Aro,(x,y))

		def mira(x,y): #Generar aro
			root_jueg.blit(Mira,(x,y))'''

		def gen_img(img,x,y): #Generar cualquier imagen
			root_jueg.blit(img,(x,y))


		def exp(surf,x,y,xi,yi): #Exapandir superficie (surf), se expande a x,y y se colaca siempre en xi,yi
			global in1
			sleep(0.001)
			if x>500: #Si sobre pasa la medida 500x500 traspasa al jugaodr
				in1=0
			surf=pygame.transform.scale(surf, (x, y))
			root_jueg.blit(surf,(xi,yi))

		def ev_aro(PosJug,PosAro):
		   print (PosJug)
		   print (PosAro)
		   if PosJug[0]<(PosAro[0]+500) and (PosJug[0]+300)>=PosAro[0] and PosJug[1]+150>=PosAro[1] and (PosJug[1]+150)<=(PosAro[1]+500):
		      if PosJug[0]>(PosAro[0]+10) and (PosJug[0]+300)<(PosAro[0]+490) and PosJug[1]>(PosAro[1]+10) and (PosJug[1]+150)<(PosAro[1]+480):
		         print ('Pasa')
		      else:
		         print ('Choca')
		         colision_sonido.play()
		         sleep(2)
		         return True
		   else:
		      print ('No suma')
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
			root_jueg.fill(black)
			root_jueg.blit(fondo,(0,0))

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
					a+=0.5 #Se limita la velocidad de incremento

			x_a+=int(a) #aumenta el incremento de "exp"
			y_a+=int(a)
			xi_a-=a//2 #desplaza el eje de imagen para dar efecto de crecer sobre sí misma
			yi_a-=a//2

			if x_a>500 and in1==1:
				salir=ev_aro((posX_jug,posY_jug),(xi_a,yi_a))
				if salir:
					break
			

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
		root.deiconify()
		pygame.quit()

	def aro():
		root.withdraw()
		va.destroy()
		Juego(1) #aro
	def enemigos():
		root.withdraw()
		va.destroy()
		Juego(0) #enemigo


	home=cargarImg("aro.gif")
	Btn_back1 = Button(C_va, image=home ,command=aro, fg = "#000000")
	Btn_back1.image = home
	Btn_back1.place(x=500,y=300)

	home1=cargarImg("aste.gif")
	Btn_back2 = Button(C_va, image=home1 ,command=enemigos, fg = "#000000")
	Btn_back2.image = home1
	Btn_back2.place(x=250,y=300)
	
    
#______________/Sección de preventana del juego
def Jugar(): #función que carga la ventana del juego
    nombre = str(E_nombre.get()).capitalize()
    if lenn(nombre)>10: #verifica largo del nombre
        messagebox.showinfo(":(",dic_trad[8])
        return
    if nombre=="": #verifica que no sea vacío
        messagebox.showinfo(":(",dic_trad[9])
        return
    else:
        VentanaJuego(nombre) #devuelve la ventana junto con el nombre introducido



#______________/Sección de botonesde la ventana principal
x1=400
mul=80
y1=500

def back ():
    root.destroy()

img_aux=cargarImg("top2.gif")
Btn1=Button(root,command=Ventana1,text=dic_trad[2],fg="black",bg="black",image=img_aux)
Btn1.place(x=x1+mul*2,y=y1)

img_aux1=cargarImg("inf.gif")
Btn2=Button(root,command=Ventana2,text="Info",fg="black",bg="black",image=img_aux1)
Btn2.place(x=x1+mul*3,y=y1)

img_aux2=cargarImg("play.gif")
Btn3=Button(root,command=Jugar,text=dic_trad[4],fg="black",bg="black",image=img_aux2)
Btn3.place(x=x1,y=y1)


img_aux3=cargarImg("set.gif")
Btn6=Button(root,command=Ventana3,text=dic_trad[11],fg="black",bg="black",image=img_aux3)
Btn6.place(x=x1+mul,y=y1)

img_aux4=cargarImg("cerr.gif")
Btn7=Button(root,command=back,text=dic_trad[11],fg="black",bg="black",image=img_aux4)
Btn7.place(x=x1+mul*4,y=y1)

img_aux5=cargarImg("us.gif")
Btn4=Button(root,command=inter,text="Español",fg="black",bg="grey",font=('Eras Bold ITC',12),image=img_aux5)
Btn4.place(x=650,y=10)



root.mainloop()
