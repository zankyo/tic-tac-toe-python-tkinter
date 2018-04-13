# Créé par Zankyo, le 06/04/2018 en Python 3.2


from tkinter import *
from random import *

# creation des variables

M = 0
player = randint(0,1)
Win = 0



# creation des fonctions

def pointeur_cercle(event):
    global player,Win
    M = 0
    x = int(event.x)
    y = int(event.y)
    print("Le clic est en : "+ str(event.x) + " ; "+ str(event.y))
    if (Win == 0):
        if(player == 0):
            while (x % 100 != 0):
                x -= 1
            while (y % 100 != 0):
                y -= 1
            if (y == 0):
                M += 0
            else:
                if (y == 100):
                    M += 3
                else:
                    if(y == 200):
                        M += 6
            if (x == 0):
                M += 0
            else:
                if (x == 100):
                    M += 1
                else:
                    M += 2
            if (Matrice[M] == 0):
                cadre.create_oval(x+10,y+10,x+80,y+80)
                Matrice[M] = 2
                player += 1
            print(Matrice)
            txt.config(text="au tour des croix ( clic droit )")
            if(Matrice[0] == 2 and Matrice[1] == 2 and Matrice[2] == 2 or Matrice[3] == 2 and Matrice[4] == 2 and Matrice[5] == 2 or Matrice[6] == 2 and Matrice[7] == 2 and Matrice[8] == 2 or Matrice[0] == 2 and Matrice[3] == 2 and Matrice[6] == 2 or Matrice[1] == 2 and Matrice[4] == 2 and Matrice[7] == 2 or Matrice[2] == 2 and Matrice[5] == 2 and Matrice[8] == 2 or Matrice[0] == 2 and Matrice[4] == 2 and Matrice[8] == 2 or Matrice[2] == 2 and Matrice[4] == 2 and Matrice[6] == 2 ):
                txt.config(text="victoire des cercle")
                Win += 1
            else:
                if(Matrice[0]!=0 and Matrice[1]!=0 and Matrice[2]!=0 and Matrice[3]!=0 and Matrice[4]!=0 and Matrice[5]!=0 and Matrice[6]!=0 and Matrice[7]!=0 and Matrice[8]!=0):
                    txt.config(text="égalité")
    else:
        txt.config(text="fin du game")



def pointeur_croix(event):
    global player,Win
    M = 0
    x = int(event.x)
    y = int(event.y)
    print("Le clic est en : "+ str(event.x) + " ; "+ str(event.y))
    if(Win == 0):
        if(player == 1):
            while (x % 100 != 0):
                x -= 1
            while (y % 100 != 0):
                y -= 1
            if (y == 0):
                M += 0
            else:
                if (y == 100):
                    M += 3
                else:
                    if(y == 200):
                        M += 6
            if (x == 0):
                M += 0
            else:
                if (x == 100):
                    M += 1
                else:
                    M += 2
            if(Matrice[M] == 0):
                cadre.create_line(x+10,y+10,x+80,y+80)
                cadre.create_line(x+80,y+10,x+10,y+80)
                Matrice[M] = 1
                player -= 1
            print(Matrice)
            txt.config(text="au tour des cercles ( clic gauche )")
            if(Matrice[0] == 1 and Matrice[1] == 1 and Matrice[2] == 1 or Matrice[3] == 1 and Matrice[4] == 1 and Matrice[5] == 1 or Matrice[6] == 1 and Matrice[7] == 1 and Matrice[8] == 1 or Matrice[0] == 1 and Matrice[3] == 1 and Matrice[6] == 1 or Matrice[1] == 1 and Matrice[4] == 1 and Matrice[7] == 1 or Matrice[2] == 1 and Matrice[5] == 1 and Matrice[8] == 1 or Matrice[0] == 1 and Matrice[4] == 1 and Matrice[8] == 1 or Matrice[2] == 1 and Matrice[4] == 1 and Matrice[6] == 1 ):
                txt.config(text="victoire des croix")
                Win += 1
            else:
                if(Matrice[0]!=0 and Matrice[1]!=0 and Matrice[2]!=0 and Matrice[3]!=0 and Matrice[4]!=0 and Matrice[5]!=0 and Matrice[6]!=0 and Matrice[7]!=0 and Matrice[8]!=0):
                    txt.config(text="égalité")
    else:
        txt.config(text="fin du game")

def reset():
    global Win,player
    carreaux = [[cadre.create_rectangle(i*100,j*100,(i+1)*100,(j+1)*100,fill="#FFFFFF")
                                        for i in range(10)] for j in range(10)]
    Matrice[:] = [0,0,0,0,0,0,0,0,0]
    Win = 0
    player = randint(0,1)
    if (player == 0):
        txt.config(text="jouer en clic gauche ( les cercles )")
    else:
        txt.config(text="jouer en clic droit ( les croix )")
    print(Matrice)

# creation du programme principal

morpion = Tk()
morpion.title('morpion nul fait par un nul pour des nuls')
morpion.geometry('300x400')

# creation des canvas

cadre = Canvas(morpion, width=300, height=300, bg='ivory')
textebouton = Canvas(morpion, width=300, height=100, bg='ivory')

# cration de la grille de jeu

carreaux = [[cadre.create_rectangle(i*100,j*100,(i+1)*100,(j+1)*100,fill="#FFFFFF")
                                        for i in range(10)] for j in range(10)]

# creation de texte

txt = Label(textebouton,text = "")
txt.grid(row=1,column=1)

if (player == 0):
    txt.config(text="jouer en clic gauche ( les cercles )")
else:
    txt.config(text="jouer en clic droit ( les croix )")

# creation du bouton reset

butreset = Button(textebouton,text="reset de la partie",command=reset)
butreset.grid(row=2,column=1)

# event

cadre.bind("<Button-1>", pointeur_cercle)
cadre.bind("<Button-3>", pointeur_croix)
cadre.pack()
textebouton.pack()

# creation des matrices

Matrice = [0,0,0,0,0,0,0,0,0]

morpion.mainloop()

