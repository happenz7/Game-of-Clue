from tkinter import *
# from src import Game
from src.card import *
from tkinter import messagebox

class suggestionScreen:

    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.frame_a = Frame()
        self.window.resizable(False, False)
        self.createWindow()
        self.window.mainloop()

    # Create the window and add the widgets
    def createWindow(self):
        self.window.geometry("500x500+10+10")
        self.window.title('Suggestion')

        # Murderer text and drop down menu
        murderer = Label(self.window, text='The murderer is ', width=16)
        murderer.place(x=175, y=100)

        self.selCharacter = StringVar(self.window)
        self.selCharacter.set("Select")
        optionMenu = OptionMenu(self.window, self.selCharacter, *Character.characters)
        optionMenu.place(x=250, y=150, anchor=CENTER)

        # Weapon text and drop down menu
        weapon = Label(self.window, text='The weapon used is ', width=16)
        weapon.place(x=175, y=200)

        self.selWeapon = StringVar(self.window)
        self.selWeapon.set("Select")
        optionMenu2 = OptionMenu(self.window, self.selWeapon, *Weapon.weapons)
        optionMenu2.place(x=250, y=250, anchor=CENTER)

        # Add a label that says which room the player is in and therefore suggesting

        self.location = Room.kitchen.name
        locationLabel = Label(self.window, text='Room is ' + self.location, borderwidth=2, relief='solid', width=18)
        locationLabel.place(x=250, y=320, anchor=CENTER)

        #Confirm button does not close the window and does not print location

        confirmButton = Button(self.window, width=14, height=2, text="Suggest", command=lambda: self.suggest())
        confirmButton.place(x=250, y=400, anchor=CENTER)
        # Button is disabled when it's not a player's turn
        #confirmButton['state']==DISABLED


    def suggest(self):
        shownCard = self.game.curPlayer.suggestion(
            Room.rooms[self.location],
            Weapon.weapons[self.selWeapon.get()],
            Character.characters[self.selCharacter.get()],
            self.game.players
        )
        #popup with shownCard.name in text here. When user clicks ok, suggest window will close
        if shownCard is not None:
            msg = f"Shown card: {shownCard.name}"
        else:
            msg = "No card shown"
        messagebox.showinfo(title="Result", message=msg)
        self.window.destroy()

    # def suggestionAction(self):
        # self.game.playerSuggests()


