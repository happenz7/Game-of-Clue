import tkinter.font as tkFont
from tkinter import *

from src.CharacterSelect import CharacterSelect


class UI:
    def __init__(self, game):
        self.game = game
        self.window = Tk()
        self.frame_a = Frame()
        self.window.resizable(False, False)
        self.start()

    # Doesn't work rn :(
    def backgroundImage(self):
        """
        self.background = PhotoImage(file='../assets/background.png', height=300, width=300)
        imageCanvas = Canvas(self.window, height=700, width=700)
        imageBack = imageCanvas.create_image(300, 300, image=self.background, anchor='n')
        imageCanvas.place(x=0, y=0)
        imageCanvas.tag_lower(imageBack)
        """

        '''
        FILENAME = 'image.png'
        root = tk.Tk()
        canvas = tk.Canvas(root, width=250, height=250)
        canvas.pack()
        tk_img = ImageTk.PhotoImage(file = FILENAME)
        canvas.create_image(125, 125, image=tk_img)
        quit_button = tk.Button(root, text = "Quit", command = root.quit, anchor = 'w',
                            width = 10, activebackground = "#33B5E5")
        quit_button_window = canvas.create_window(10, 10, anchor='nw', window=quit_button)    
        root.mainloop()
        '''

        # backgroundImage.create_image(0, 0, image=background, anchor="nw")

        # gameCanvas = Canvas(self.window, height=400, width=600, bg='blue')
        # gameCanvas.place(x=50, y=180)

    def start(self):
        self.addText()
        self.addButtons()
        self.backgroundImage()
        self.createWindow()

    def addText(self):
        # Welcome to Cluedo text
        fontStyle = tkFont.Font(size=20)
        welcome = Label(self.window, text='Welcome to Cluedo!', width=16, font=fontStyle)
        welcome.place(x=250, y=150)

    def next_screen(self):
        for wid in self.window.winfo_children():
            wid.destroy()
        self.frame_a.destroy()
        CharacterSelect(self.window, self.game)

    def addButtons(self):
        # New game button
        btn_new = Button(self.window, text='New Game', height=2, width=16, command=lambda: self.next_screen())
        btn_new.place(x=270, y=250)

        # Join game button
        btn_join = Button(self.window, text='Join Game', height=2, width=16)
        btn_join.place(x=270, y=350)

    # Create window
    def createWindow(self):
        self.window.title('Cluedo')
        self.window.geometry("700x700+10+10")
        self.window.mainloop()
