from tkinter import *
from PIL import ImageTk, Image
from src import Game
#from player import Player

#click button rollDice in game screen
#this shows what you rolled
#2 images corresponding to the numbers

class dice:

    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.frame_a = Frame()
        self.window.resizable(False, False)
        self.createWindow()

    def createWindow(self):
        self.window.geometry("500x500+10+10")
        self.window.title('Cluedo')

        # Left die
        self.lDie = Canvas(self.window, height=230, width=230, highlightbackground="black")
        self.lDie.place(x=10, y=50)

        # Right die
        self.rDie = Canvas(self.window, height=230, width=230, highlightbackground="black")
        self.rDie.place(x=255, y=50)

        self.button = Button(self.window, text="Roll Dice", command=lambda: self.roll(), width=15, height=2)
        self.button.place(x=180, y=400)

        # Close button


    def closeWindow(self):
        self.window.destroy()

    def roll(self):
        l, r = self.game.curPlayer.rollDice()
        self.lDie.create_text(115,115,text=str(l), font="Arial 40 bold")
        self.rDie.create_text(115,115,text=str(r), font="Arial 40 bold")
        self.button.place_forget()
        button = Button(self.window, text="Close", command=self.closeWindow, width=15, height=2)
        button.place(x=180, y=400)



# def diceroll(self):
# bard = Image.open()
# bard = img.resize((50, 50), Image.ANTIALIAS)
# bardejoy = ImageTk.PhotoImage("Dice.jpeg")

#  leftplace = Label(self.window, height= 15, width=25, image=bardejoy)
#  rightplace = Label(self.window, height=15, width=25, image=bardejoy)

#   leftplace.place(x=10, y=80)
#   rightplace.place(x=260, y=80)

# bardejoy = ImageTk.PhotoImage("Dice.jpeg")

# leftplace = Label(self.window, height=15, width=25, image=bardejoy)
# rightplace = Label(self.window, height=15, width=25, image=bardejoy)

# leftplace.place(x=10, y=80)
# rightplace.place(x=260, y=80)


