from tkinter import *
from src.card import *


class cardShow:

    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.frame_a = Frame()
        self.window.resizable(False, False)

        self.l = []
        self.createWindow()

    # What this class should do:
    # Show the cards and not allow player to click on them
    # Allow player to click on them when showCards() is activated --> they have to show a card if they have it

    # Pop up asking you to show card to someone
    # Bold margin around which ones you can show
    # Choose which one you want to show and click 'show'

    def createWindow(self):
        self.window.title('Cluedo')
        self.window.geometry("600x600+10+10")

        # Explanation text
        introText = 'These are your cards. ' \
                    '\n Here you can see which cards you have, and can select which card you want ' \
                    '\n to show to another player.' \
                    '\n \n The cards you can show will have a bold margin.' \
                    '\n Select the card and press the show button.' \
                    '\n \n To close the window when viewing press the x in the top left corner.' \
                    '\n If you close without having suggested, the window will pop up again.  '
        introLabel = Label(self.window, text=introText)
        introLabel.place(x=50, y=40)

        # 4 canvases for card images

        card1 = Canvas(self.window, height=200, width=130, bg='red')
        card1.place(x=15, y=230)

        card2 = Canvas(self.window, height=200, width=130, bg='red')
        card2.place(x=160, y=230)

        card3 = Canvas(self.window, height=200, width=130, bg='red')
        card3.place(x=305, y=230)

        card4 = Canvas(self.window, height=200, width=130, bg='red')
        card4.place(x=450, y=230)

        # Show button

        btn_show = Button(self.window, text='Show', height=2, width=15, command=lambda: self.show())
        btn_show.place(x=230, y=520)
        btn_show["state"] = DISABLED
        # Can do if state == NORMAL OR ENABLE

        value = StringVar(self.window)
        value.set("Select card")
        optionMenu = OptionMenu(self.window, value, *Weapon.weapons, command=self.addValue)
        optionMenu.config(width=12, height=2)
        optionMenu.place(x=300, y=480, anchor=CENTER)

    # Show button - prints what card player has chosen (needs changing)
    def show(self):
        for i, p in enumerate(self.l):
            print("Player", i, "has selected: " + p)
        self.window.destroy()

    def addValue(self, value):
        self.l.append(value)

    def showTheCards(self):
        play = self.Player()
        playCards = play.cards
