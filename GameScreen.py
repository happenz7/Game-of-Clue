from tkinter import *
from tkinter import messagebox as mb
from src.Suggestion import suggestionScreen
from src.Accusation import accusationScreen
from src.rollDice import dice
from src.cardShow import cardShow
from PIL import ImageTk, Image

class GameScreen:
    def __init__(self, window, game):
        self.game = game
        self.window = window
        self.frame_a = Frame()
        self.window.resizable(False, False)
        self.addWidgets()
        self.addMenu()
        self.buttonsBelow()
        self.createWindow()

    def addWidgets(self):
        # Player name top left
        self.playerName = StringVar(self.window)

        namelabel = Label(self.window, textvariable=self.playerName, borderwidth=2, relief='solid', width=18)
        self.playerName.set(self.game.curPlayer.name)
        namelabel.place(x=50, y=40)

        # Notebook button and pop-up
        btn_note = Button(self.window, text='Notebook', height=2, width=15)
        btn_note.place(x=500, y=30)

        btn_next_player = Button(self.window, text='Next Player', height=2, width=15,
                                 command=lambda: [self.game.nextPlayer(), self.updateCurPlayer()])
        btn_next_player.place(x=275, y=30)

        # Game board in the middle
        self.image = ImageTk.PhotoImage(Image.open("assets/ClueBoard.png"))
        gameCanvas = Canvas(self.window, height=500, width=600)
        gameCanvas.create_image(0,0,image = self.image, anchor = NW)
        gameCanvas.place(x=50, y=100)

    def updateCurPlayer(self):
        self.playerName.set(self.game.curPlayer.name)

    # Open the suggestion screen when the suggestion button is clicked
    def openSuggest(self):
        suggestionScreen(self.game)
        # print(suggest.getSuggestion())
        # exec(open('Suggestion.py').read())

    # Open the accusation screen when the accusation button is clicked
    def openAccusation(self):
        accusationScreen(self.game)

    # Open the dice screen when the roll dice button is clicked
    def openrollDice(self):
        dice(self.game)
        # exec(open('rollDice.py').read())

    # Open the show cards screen when the show cards button is clicked
    def openCards(self):
        cardShow(self.game)
        # exec(open('cardShow.py').read())

    def buttonsBelow(self):

        # RollDice button
        btn_dice = Button(self.window, text='Roll Dice', height=2, width=15, command=self.openrollDice)
        btn_dice.place(x=34, y=630)
        # btn_dice["state"] = DISABLED

        # ShowCards button
        btn_showCards = Button(self.window, text='Show Cards', height=2, width=15, command=self.openCards)
        btn_showCards.place(x=197, y=630)

        # MakeSuggestion button
        btn_sug = Button(self.window, text='Make Suggestion', height=2, width=15, command=self.openSuggest)
        btn_sug.place(x=362, y=630)

        # MakeAccusation button
        btn_acc = Button(self.window, text='Make Accusation', height=2, width=15, command=self.openAccusation)
        btn_acc.place(x=524, y=630)



    # Function that creates pop-ups to ask if they want to quit the game
    def Quit(self):
        if mb.askyesno('Verify', 'Really quit?'):
            mb.showwarning('Yes', 'You are quitting the game', command=self.window.destroy())
        else:
            mb.showinfo('No', 'Quit has been cancelled')

    # Function that quits the game when quit is clicked on the menu
    def closeWindow(self):
        self.window.quit()

    # Function that restarst the game when restart is clicked in the menu (does not restart, only quits right now)
    def openStart(self):
        self.window.destroy()
        # exec(open("launch.py").read())

    # Function that creates pop-ups to ask if they want to restart the game
    def Restart(self):
        if mb.askyesno('Verify', 'Really restart?'):
            mb.showwarning('Yes', 'You are restarting the game.', command=self.openStart())
        else:
            mb.showinfo('No', 'Restart has been cancelled.')

    # Function that adds the menu options
    def addMenu(self):
        menubarmain = Menu(self.window)
        mainmenu = Menu(menubarmain, tearoff=0)
        mainmenu.add_command(label='Restart game', command=self.Restart)
        mainmenu.add_separator()
        mainmenu.add_command(label='Quit game', command=self.Quit)

        menubarmain.add_cascade(label='Menu', menu=mainmenu)

        self.window.config(menu=menubarmain)

    # Create the window
    def createWindow(self):
        self.window.title('Cluedo')
        self.window.geometry("700x700+10+10")
        self.window.mainloop()
