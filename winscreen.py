
from tkinter import *
from tkinter import messagebox as mb


#Winscreen - appears when player wins the game
#similar structure to correctguess, incorrect guess and loss screen
class Win:
    #Constructor
    def __init__(self, game):
        self.game = game
        self.window=Tk()
        self.frame_a=Frame()
        self.window.resizable(False, False)
        self.start()

    #Start function - calls functions
    def start(self):
        self.addButtons()
        self.createWindow()

    #add buttons function - adds quit and restart button
    def addButtons(self):
        restartButton = Button(self.window, text='Restart', command=self.Restart())
        quitButton = Button(self.window, text='Quit', command=self.Quit())
        quitButton.place(x=200, y=250)
        restartButton.place(x=200, y=150)

    #Restart function using messagebox
    def Restart(self):
       mb.askyesno(title= "Restart", message="Do you want to Restart the game", command = self.startScreen())


    #Quit function using messagebox
    def Quit(self):
        if mb.askyesno('Verify', 'Really quit?'):
            mb.showwarning('Yes', 'You are quitting the game' , command = self.closeWindow())
        else:
            mb.showinfo('No', 'Quit has been cancelled')

    #Close window function - called when confirming to quit the game
    def closeWindow(self):
        self.window.quit()

    #create Window - window specifications
    def createWindow(self):
        self.window.geometry("400x300+10+10")
        self.window.title(f"{self.game.curPlayer.name} won the game!")
        self.window.mainloop()



# import tkinter as tk
#
# class Win:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'Restart', width = 25, command = self.new_window)
#         self.button2 = tk.Button(self.frame, text='Quit Game', width=25, command=self.new_window)
#         self.button1.pack()
#         self.button2.pack()
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Loss(self.newWindow)
#
# class Loss:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Win(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()