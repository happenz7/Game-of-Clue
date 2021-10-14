
from tkinter import *
from tkinter import messagebox as mb
import run


#Incorrect Guess - includes information on whether guess was correct and then allows user to click on of 
#two buttons





window=Tk()
frame_a=Frame()
label_a=Label(master=frame_a)
#Restart Function 
def Restart():
   mb.askyesno(title= "Restart", message="Do you want to Restart the game", command = lambda: run())

#Quit function
def Quit():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showwarning('Yes', 'You are quitting the game' , command = closeWindow())
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
window.title('Wrong Accusation!')
window.mainloop()
