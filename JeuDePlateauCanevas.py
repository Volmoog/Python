#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
                                *** NSI 1ère ***

    Canevas générique pour un jeu de plateau avec la bibliothèque TKINTER

"""


from tkinter import *
from tkinter.messagebox import showinfo
from random import randrange


coteCanevas = 600       # Côté du canevas en pixels
marge = 20              # Marge entre le bord du canevas et le plateau de jeu
coteCase = (coteCanevas - 2 * marge) / 3
etatJeu = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

nombreCoups = 0
humainCommence = True
humainJoue = True
partieFinie = True

def initJeu():
    """
        Initialisation du jeu. Structures de données propres au jeu
    """
    global nombreCoups
    for i in range(2):
        for j in range(2):
            etatJeu[i][j] = 0

    nombreCoups = 0
    return()


def nouvellePartie():
    global humainCommence, humainJoue, partieFinie

    print("nouvelle partie")
    partieFinie = False
    if randrange(2) == 1:
        humainCommence = True
        humainJoue = True
    else:
        humainCommence = False
        humainJoue = False

    can.delete("all")
    dessinePlateau()
    if not(humainJoue):
        machineJoue()


def about():
    """
        Affiche la fenêtre "A propos"
    """

    showinfo(
        "A propos\n\n",

        "*** Programme écrit par ***\n"
        " EXEL Tristan \n"
        "1ère NSI - Lycée Louis Armand - Mulhouse \n"
    )

    return()


def reglesJeu():
    """
        Affiche les règles du jeu dans une boîte d'information
    """

    showinfo(
        "Règles du jeu\n\n",

        "Premièrement : \n"
        "Deuxièmement : \n"
    )

    return()


def dessinePlateau():
    """
        Dessin du plateau de jeu
    """

    # Exemple avec un plateau de Tic Tac Toe

    x = 0
    y = 0

    for i in range(4): # Tracé des lignes horizontales
        can.create_line(marge, y + marge, coteCanevas - marge, y + marge, width=4, fill="black")
        y += coteCase

    x = 0
    y = 0

    for i in range(4): # Tracé des lignes verticales
        can.create_line(x + marge, marge, x + marge, coteCanevas - marge, width=4, fill="black")
        x += coteCase

def dessineCroix(i, j):
    delta = 20

    x0 = marge + j * coteCase
    y0 = marge + i * coteCase
    x1 = x0 + delta
    y1 = y0 + delta
    x2 = x0 + coteCase - delta
    y2 = y0 + coteCase - delta

    can.create_line(x1, y1, x2, y2, width=2, fill='crimson')
    can.create_line(x1, y2, x2, y1, width=2, fill='crimson')

def dessineCercle(i, j):
    delta = 20
    x0 = marge + j * coteCase
    y0 = marge + i * coteCase
    x1 = x0 + delta
    y1 = y0 + delta
    x2 = x0 + coteCase - delta
    y2 = y0 + coteCase - delta

    can.create_oval(x1, y1, x2, y2, width=2, outline = 'grey')


def machineJoue():
    global humainCommence, humainJoue, partieFinie
    i = randrange(2)
    j = randrange(2)
    if not(partieFinie) and not(humainJoue):
        if (i, j) != (-1, -1):
            if etatJeu[i][j] == 0:
                if humainCommence:
                    dessineCercle(i,j)
                    etatJeu[i][j] = -1
                    humainJoue = True
                    verifiePlateau()
                else:
                    dessineCroix(i,j)
                    etatJeu[i][j] = 1
                    humainJoue = True
                    verifiePlateau()



def verifiePlateau():
    global humainCommence, humainJoue, partieFinie, etatJeu
    if not(partieFinie):
        for i in range(2):
            for j in range(2):

                if etatJeu[0][0] == etatJeu[1][0] == etatJeu[2][0]: #ligne 1
                    partieFinie = True
                elif etatJeu[0][1] == etatJeu[1][1] == etatJeu[2][1]: # ligne 2
                    partieFinie = True
                elif etatJeu[0][2] == etatJeu[1][2] == etatJeu[2][2]: #ligne 3
                    partieFinie = True
                elif etatJeu[0][0] == etatJeu[0][1] == etatJeu[0][2]: #colonne 1
                    partieFinie = True
                elif etatJeu[1][0] == etatJeu[1][1] == etatJeu[1][2]: # colonne 2
                    partieFinie = True
                elif etatJeu[2][0] == etatJeu[2][1] == etatJeu[2][2]: #colonne 3
                    partieFinie = True
                elif etatJeu[0][0] == etatJeu[1][1] == etatJeu[2][2]: # diagonale 1
                    partieFinie = True
                elif etatJeu[0][2] == etatJeu[1][1] == etatJeu[2][0]: #diagonale 2
                    partieFinie = True
                else:
                    partieFinie = False

def convertitClick(x, y):
    if (x >= marge) and (x <= coteCanevas - marge) and (y >= marge) and (y <= coteCanevas - marge):
        i = int((y - marge) // coteCase)
        j = int((x - marge) // coteCase)
    else:
        i = -1
        j = -1
    return (i, j)

def clickSouris(event):
    """
        Fonction appelée lors d'un click du bouton gauche
        de la souris/trackpad
    """
    global nombreCoups; humainJoue
    print("Clic au point", (event.x, event.y))
    (i, j) = convertitClick(event.x, event.y)
    print(i, j)

    if not(partieFinie) and humainJoue:
        (i, j) = convertitClick(event.x, event.y)

        if (i, j) != (-1, -1):
            if etatJeu[i][j] == 0:
                if humainCommence:
                    dessineCroix(i,j)
                    etatJeu[i][j] = 1
                    verifiePlateau()
                else:
                    dessineCercle(i,j)
                    etatJeu[i][j] = -1
                    verifiePlateau()
                machineJoue()
                nombreCoups += 1




# Main

fen = Tk()

fen.title("Jeu de ...")
fen.config(bg = "bisque")                   # Couleur du fond de la fenêtre
fen.resizable(width=False, height=False)    # Interdit le redimensionnement de la fenêtre

can = Canvas(fen, width=coteCanevas, height=coteCanevas, bg = "snow2")
can.pack(side=LEFT, padx=25, pady=25)

bouton0 = Button(fen, text="A propos", command = about)
bouton0.pack(side=TOP, padx=20, pady=50)

bouton1 = Button(fen, text="Règles du jeu", command = reglesJeu)
bouton1.pack(side=TOP, padx=20, pady=50)

bouton2 = Button(fen, text="Nouvelle partie", command = nouvellePartie)
bouton2.pack(side=TOP, padx=20, pady=50)

can.bind("<Button-1>", clickSouris)         # Gestion des clicks

dessinePlateau()


# Gestionnaire d'évènements
fen.mainloop()


while not(partieFinie):
    if not(humainJoue):
        machineJoue()
