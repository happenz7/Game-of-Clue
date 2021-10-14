from tkinter import *
from src.GameScreen import GameScreen
from src.card import *

#Class CharacterSelect -allows players to select characters
class CharacterSelect:

    #Constructor
    def __init__(self, window, game):
        self.game = game
        self.window = window
        self.frame_a = Frame()
        self.label_a = Label(master=self.frame_a)
        self.window.resizable(False, False)
        self.players = ['Colonel Mustard', 'Professor Plum', 'Reverand Green', 'Mrs. Peacock', 'Miss Scarlett',
                        'Mrs. White']
        self.ys = [i for i in range(150, 450, 50)]
        # self.v
        self.l = []
        self.createWindow2()

    #next screen function - ensure that the screen is destroyed when moving to the next screen
    def next_screen(self):
        for wid in self.window.winfo_children():
            wid.destroy()
        self.frame_a.destroy()
        self.game.sortCards()
        self.game.start()
        GameScreen(self.window, self.game)

    #creating window - size and tile specified
    #includes specifications for the various drowdown menus
    def createWindow2(self):
        self.window.geometry("700x700+10+10")
        self.window.title('Cluedo')
        players = list(Character.characters.keys())
        #loop allowing each menu to contain each playable character
        for p, y in zip(players, self.ys):
            value = StringVar(self.window)
            value.set("Select character")
            optionMenu = OptionMenu(self.window, value, *players, command=self.addValue)
            optionMenu.config(width=12, height=2)
            optionMenu.place(x=350, y=y, anchor=CENTER)

        button = Button(self.window, text="Ready", command=lambda: [self.ok(), self.next_screen()], width=12, height=2)
        button.place(x=295, y=500)

    # confirmation of character selection
    def ok(self):
        for i, p in enumerate(self.l):
            # prints out which player has selected which character
            print("Player {0} has selected: {1}".format(i + 1, p))
            self.game.addPlayer(Character.characters[p])

    #specifies which character is currently selected by player
    def addValue(self, value):
        self.l.append(value)


