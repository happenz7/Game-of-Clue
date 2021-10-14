from tkinter import *
from tkinter import messagebox as mb


#Lossscreen - appears when player wins the game
#similar structure to correctguess, incorrect guess and win screen
class Loss:
    # Constructor
    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.frame_a = Frame()
        self.window.resizable(False, False)
        self.start()

    # Start function - calls functions
    def start(self):
        self.addButtons()
        self.createWindow()

    # add buttons function - adds quit and restart button
    def addButtons(self):
        restartButton = Button(self.window, text='Restart', command=self.Restart)
        quitButton = Button(self.window, text='Quit', command=self.Quit)
        restartButton.place(x=150, y=100, height=25, width=100)
        quitButton.place(x=150, y=200, height=25, width=100)

    # Restart function using messagebox
    def Restart(self):
       mb.askyesno(title= "Restart", message="Do you want to Restart the game", command = self.startScreen)

    # Quit function using messagebox
    def Quit(self):
        if mb.askyesno('Verify', 'Really quit?'):
            mb.showwarning('Yes', 'You are quitting the game' , command = self.window.destroy())
        else:
            mb.showinfo('No', 'Quit has been cancelled')

    # start screen - returns to start menu - not implemented yet
    def startScreen(self):
        self.window.quit()
        # self.game.restart()


    def createWindow(self):
        self.window.geometry("400x300+10+10")
        self.window.title('You have lost the game!')
        self.window.mainloop()
