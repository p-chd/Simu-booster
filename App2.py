import customtkinter as ctk
from tkinter import Menu, Label, PhotoImage, BooleanVar
from Card import Card
from main import main2, sortById, printList, importCardListFromJSON, retrieveByRarity, createDeck
from pygame import mixer 
from scrapCard import cardListToCSV, saveCSV


mixer.init()
mixer.music.load("resources\MusicTheme.mp3")

def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def stop():
    mixer.music.stop()


def export_fun():
    global deck
    CSV = cardListToCSV(deck)
    saveCSV("deck", CSV)

cardListSetOne = list()
cardListSetTwo = list()
cardListSetThree = list()
deck = list()
deck_size = 0

# Exemple de fonction (appelée par le menu)
def fun1():
    global deck, setOneBool, setTwoBool, setThreeBool
    deck.clear()
    cardListAllSet = list()
    if setOneBool.get():
        cardListSetOne = importCardListFromJSON(".\data\dataSetOne")
        cardListAllSet += cardListSetOne
    if setTwoBool.get():
        cardListSetTwo = importCardListFromJSON(".\data\dataSetTwo")
        cardListAllSet += cardListSetTwo
    if setThreeBool.get():
        cardListSetThree = importCardListFromJSON(".\data\dataSetThree")
        cardListAllSet += cardListSetThree
    commonCardList = (retrieveByRarity(cardListAllSet, "common"))
    uncommonCardList = (retrieveByRarity(cardListAllSet, "uncommon"))
    rareCardList = (retrieveByRarity(cardListAllSet, "rare"))
    veryrareCardList = (retrieveByRarity(cardListAllSet, "ultra_rare"))

    try:
        deck_size = int(entry_number.get())
        deck = createDeck(commonCardList, uncommonCardList, rareCardList, veryrareCardList, deck_size)
        deck = sortById(deck)
        actualiser()
    except ValueError:
        pass
    printList(deck)

# Créer la fenêtre principale
window = ctk.CTk()
window.geometry("1920x1080")
window.title("EoJ Deck Maker")
window.iconbitmap("resources\logo.ico")

mixer.music.set_volume(0.01)
play()


# Importe l'image de fond
bg = PhotoImage(file="resources\eyeofjudgement3.png")

# Creer les boolean de set
setOneBool=BooleanVar(value=False)
setTwoBool=BooleanVar(value=False)
setThreeBool=BooleanVar(value=False)

# --- MENU ---
menu_bar = Menu(window)
deck_menu = Menu(menu_bar, tearoff=0)
deck_menu.add_command(label="Créer un nouveau deck", command=fun1)
menu_bar.add_cascade(label="Deck", menu=deck_menu)

sets_menu = Menu(menu_bar, tearoff=0)
sets_menu.add_checkbutton(label="Set 1", variable=setOneBool)
sets_menu.add_checkbutton(label="Set 2", variable=setTwoBool)
sets_menu.add_checkbutton(label="Set 3", variable=setThreeBool)
menu_bar.add_cascade(label="Sets", menu=sets_menu)

export_menu = Menu(menu_bar, tearoff=0)
export_menu.add_command(label="Exporter le deck actuel en CSV", command=export_fun)
menu_bar.add_cascade(label="Export", menu=export_menu)

window.configure(menu=menu_bar)

# --- FOND D'ÉCRAN AVEC IMAGE ---
background_label = Label(window, image=bg)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Sous-frame gauche : saisie + volume
left_frame = ctk.CTkFrame(window, fg_color="white")
left_frame.place(relx=0.02, rely=0.5, anchor="sw", relwidth=0.3, relheight=0.35)  # 30% largeur, petit espace à gauche

# Champ de saisie d’un nombre
entry_number = ctk.CTkEntry(left_frame, placeholder_text="Entrer un nombre", justify="center")
entry_number.pack(pady=(10, 20), padx=10, fill="x")

# Label volume (optionnel)
volume_label = ctk.CTkLabel(left_frame, text="Volume")
volume_label.pack(pady=(0, 5))

# Slider de volume
def changer_volume(valeur):
    mixer.music.set_volume(float(valeur*0.2))

volume_slider = ctk.CTkSlider(left_frame, from_=0, to=1, number_of_steps=100, command=changer_volume)
volume_slider.set(0.1)
volume_slider.pack(pady=(0, 10), padx=10, fill="x")

# --- ZONE DROITE : LISTE SCROLLABLE DE BOUTONS ---
right_frame = ctk.CTkFrame(window, fg_color="white")
right_frame.place(relx=0.34, rely=0.5, anchor="w", relwidth=0.64, relheight=0.7)  # 66% de largeur, collé à gauche de la zone droite


# Scrollable frame à l’intérieur
scrollable = ctk.CTkScrollableFrame(right_frame, fg_color="transparent")
scrollable.pack(fill="both", expand=True)

# Ajouter quelques boutons (tu remplaces "texte" plus tard)
def actualiser():
    for widget in scrollable.winfo_children():
        widget.destroy()
    for i in deck:
        btn = ctk.CTkButton(scrollable, text=i.__str__(), fg_color="#DDDDDD", text_color="black")
        btn.pack(pady=5, padx=10, fill="x")

# Lancer l’interface
window.mainloop()