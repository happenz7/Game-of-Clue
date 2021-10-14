from tkinter import *
from src.card import *
from src.lossscreen import Loss
from src.winscreen import Win


class accusationScreen:

    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.frame_a = Frame()
        self.window.resizable(False, False)
        self.createWindow()
        self.window.mainloop()

    # Creates the window and adds the widgets
    def createWindow(self):
        self.window.geometry("500x500+10+10")
        self.window.title('Accusation')

        # Character text and drop down menu
        murderer = Label(self.window, text='The murderer is ', width=16)
        murderer.place(x=175, y=100)

        self.selCharacter = StringVar(self.window)
        self.selCharacter.set("Select")
        optionMenu = OptionMenu(self.window, self.selCharacter, *Character.characters)
        optionMenu.config(width=12, height=2)
        optionMenu.place(x=250, y=150, anchor=CENTER)

        # Weapon text and drop down menu
        weapon = Label(self.window, text='The weapon used is ', width=16)
        weapon.place(x=175, y=200)

        self.selWeapon = StringVar(self.window)
        self.selWeapon.set("Select")
        optionMenu2 = OptionMenu(self.window, self.selWeapon, *Weapon.weapons)
        optionMenu2.config(width=12, height=2)
        optionMenu2.place(x=250, y=250, anchor=CENTER)

        # Room text and drop down menu
        room = Label(self.window, text='The room where the murder happened is ')
        room.place(x=250, y=300, anchor=CENTER)

        self.selRoom = StringVar(self.window)
        self.selRoom.set("Select")
        optionMenu3 = OptionMenu(self.window, self.selRoom, *Room.rooms)
        optionMenu3.config(width=12, height=2)
        optionMenu3.place(x=250, y=340, anchor=CENTER)

        confirmButton = Button(self.window, width=14, height=2, text="Accuse", command=lambda: self.accuse())
        confirmButton.place(x=250, y=420, anchor=CENTER)

    def accuse(self):
        result = self.game.curPlayer.accusation(
            Room.rooms[self.selRoom.get()],
            Weapon.weapons[self.selWeapon.get()],
            Character.characters[self.selCharacter.get()],
            self.game.murderCards
        )

        if result:
            Win(self.game)
        else:
            Loss(self.game)
        self.window.quit()
