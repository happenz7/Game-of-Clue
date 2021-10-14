import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
window.resizable(False, False)

#Label does not show up
label_a = tk.Label(master=frame_a, text = "Welcome to Cluedo")

#Background image

#bg = tk.PhotoImage(file = "CluedoBackground.png")
#label1 = tk.Label(window, image = file)
#label1.place(x = 0, y = 0)

#First screen with new/join game

btn1 = tk.Button(window, text='New Game')
btn2 = tk.Button(window, text='Join Game')
btn1.place(x=150, y=200)
btn2.place(x=150, y=300)

#Window size and title

window.geometry("700x700+10+10")
window.title('Cluedo')
window.mainloop()
