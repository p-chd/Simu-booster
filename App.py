from tkinter import *
import customtkinter as ctk

import scrapCard
from Card import Card
from main import printList, main2, sortById


deck = list()


#creer une fenetre
window = ctk.CTk()

background_image = PhotoImage(file="resources\eyeofjudgement3.png")
label1 = Label(window, image = background_image)
label1.place(x=0, y=0, relheight=1, relwidth=1)

def button_create_deck_function():
    global deck
    deck = main2()
    deck = sortById(deck)
    printList(deck)

button_create_deck_function()


def create_main_window():
    #On cree la fenetre de base
    global window, frame_droite, frame_gauche
    window.title("EoJ Deck Maker")
    window.geometry("480x360")
    window.iconbitmap("resources\logo.ico")
    window.config(background="#71382c")
    #on sépare la fenetre en 2
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.grid_rowconfigure(0, weight=1)

    #on cree la partie gauche
    frame_gauche = ctk.CTkFrame(master=window, fg_color="transparent")
    frame_gauche.grid(column=0, sticky="nsew")

    frame_gauche.grid_rowconfigure(0, weight=1)
    frame_gauche.grid_columnconfigure(0, weight=1)

    #on cree la partie droite
    frame_droite = ctk.CTkFrame(master=window, fg_color="gray")
    frame_droite.grid(column=1, sticky="nsew")

    frame_droite.grid_rowconfigure(0, weight=1)
    frame_droite.grid_columnconfigure(0, weight=1)


    label_gauche = ctk.CTkLabel(frame_gauche, text="Contenu à gauche", fg_color="transparent")
    label_gauche.grid(row=0, column=0, sticky='nsew')


create_main_window()


#Creation d'une frame scrollable
scrollable_frame = ctk.CTkScrollableFrame(frame_droite, fg_color="white")
scrollable_frame.pack(fill="both", expand=True, padx=100, pady=100)

for x in deck:
    ctk.CTkButton(scrollable_frame, text=x.__str__(), fg_color="white", text_color="black", hover_color="#222222").pack(pady=10)

#Creation d'un bouton
button_create_deck = Button(frame_gauche, text = "Générer un deck", command = button_create_deck_function)

#Placement du bouton
#button_create_deck.pack()


#Affiche la fenetre
window.mainloop()