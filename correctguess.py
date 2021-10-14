from tkinter import *
from tkinter import messagebox as mb


# class UI:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.frame_a = tk.Frame()
#         self.window.resizable(False, False)
#         self.start()
#
#     def start(self):
#         self.addText()
#         self.addButtons()
#         self.createWindow()


window = Tk()
frame_a = Frame()
label_a = Label(master=frame_a)

#Restart Function
def Restart():
    mb.askyesno(title="Restart", message="Do you want to Restart the game", command=startScreen())

#Quit Function
def Quit():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showwarning('Yes', 'You are quitting the game', command=closeWindow())
    else:
        mb.showinfo('No', 'Quit has been cancelled')

#Close window function - called when Quit button is clicked
def closeWindow():
    window.quit()


restartButton = Button(text='Restart', command=Restart)
quitButton = Button(text='Quit', command=Quit)
quitButton.place(x=200, y=250)
restartButton.place(x=200, y=150)

window.geometry("400x300+10+10")
window.title('Correct guess! You have won the game!')
window.mainloop()
