from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import random


class GameScreen(Tk):
    def __init__(self):
        super().__init__()
        self.user_points = 0
        self.comp_points = 0
        self.choices = ['rock', 'paper', 'scissor']
        self.user_choice = 'default'
        self.comp_choice = 'default'
        self.bgcolor = '#eb4034'
        self.title("Rock Paper Scissor")
        self.photo = PhotoImage(file="./img/RockPaperScissor.png")
        self.iconphoto(False, self.photo)
        self.geometry("1000x550")
        self.resizable(False, False)
        self.configure(background=self.bgcolor)
        self.tframe = Frame(self,bg=self.bgcolor)
        self.tframe.pack(side=TOP)
        self.heading = Label(self.tframe, text='Rock Paper Scissor by Ayush Solanki', font=Font(size=25),
                             bg=self.bgcolor)
        self.heading.pack()

    def button_panel(self):
        self.lframe = Frame(self, bg=self.bgcolor)
        self.lframe.pack(side=LEFT, padx=(25,0))
        self.left_label = Label(self.lframe, text='Choose here', width=15, font=Font(size=15,), bg= self.bgcolor)
        self.left_label.pack(pady=5)
        self.left_rock = Button(self.lframe, text='Rock', width=15, font=Font(size=15,), bg='#61cf7b', 
                                        activebackground='#f2ce55', command=self.selectrock)
        self.left_rock.pack(pady=5)
        self.left_paper = Button(self.lframe, text='Paper', width=15, font=Font(size=15,), bg='#61cf7b', 
                                        activebackground='#f2ce55', command=self.selectpaper)
        self.left_paper.pack(pady=5)
        self.left_scissor = Button(self.lframe, text='Scissor', width=15, font=Font(size=15,), bg='#61cf7b', 
                                        activebackground='#f2ce55', command=self.selectscissor)
        self.left_scissor.pack(pady=5)

    def game_panel(self):
        self.rframe = Frame(self, bg=self.bgcolor)
        self.rframe.pack(side=RIGHT)
        self.lblframe = LabelFrame(self.rframe,width=500, bg=self.bgcolor, highlightthickness=0, border=0)
        self.lblframe.pack(side=TOP)
        self.user_label = Label(self.lblframe, text='User: 0', font=Font(size=25,), bg=self.bgcolor,fg='#ffffff')
        self.user_label.pack(side=LEFT, padx=(25,100))
        self.computer_label = Label(self.lblframe, text='Computer: 0', font=Font(size=25), bg=self.bgcolor,fg='#ffffff')
        self.computer_label.pack(side=RIGHT, padx=(100,25))
        self.user_canvas = Canvas(self.rframe, width=200, height=200, highlightthickness=0, bg='#32a852')
        self.user_canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.user_canvas.pack(side=LEFT, padx=(25,225),pady=0)
        self.comp_canvas = Canvas(self.rframe, width=200, height=200, highlightthickness=0, bg='#32a852')
        self.comp_canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.comp_canvas.pack(padx=(25,100)) 

    def selectrock(self):
        self.user_choice = 'rock'
        self.gameplay()
    def selectpaper(self):
        self.user_choice = 'paper'
        self.gameplay()
    def selectscissor(self):
        self.user_choice = 'scissor'
        self.gameplay()
    def gameplay(self):
        if self.user_points < 5 and self.comp_points < 5:
            self.comp_choice = random.choice(self.choices)
            user_image = PhotoImage(file=f"img/left/{self.user_choice}.png")
            comp_image = PhotoImage(file=f"img/right/{self.comp_choice}.png")
            self.user_canvas.delete("all")
            self.user_canvas.create_image(0, 0, anchor='nw', image=user_image)
            self.user_canvas.image = user_image
            self.comp_canvas.delete("all")
            self.comp_canvas.create_image(0, 0, anchor='nw', image=comp_image)
            self.comp_canvas.image = comp_image
            if self.comp_choice != self.user_choice:
                if self.user_choice == 'rock':
                    if self.comp_choice == 'paper':
                        self.comp_points += 1
                    elif self.comp_choice == 'scissor':
                        self.user_points += 1
                elif self.user_choice == 'paper':
                    if self.comp_choice == 'scissor':
                        self.comp_points += 1
                    elif self.comp_choice == 'rock':
                        self.user_points += 1
                elif self.user_choice == 'scissor':
                    if self.comp_choice == 'rock':
                        self.comp_points += 1
                    elif self.comp_choice == 'paper':
                        self.user_points += 1
            self.user_label.configure(text=f'User: {self.user_points}')
            self.computer_label.configure(text=f'Computer: {self.comp_points}')

            if self.user_points >=5:
                res = messagebox.askyesno("User Won!!", "User wins the game :) want to play again?")
                if res: 
                    self.resetgame()
            elif self.comp_points >=5:
                res = messagebox.askyesno("Computer Won!!", "Computer wins the game :( want to play again?")
                if res: 
                    self.resetgame()
        else:
            pass 
    
    def resetgame(self):
        self.user_points = 0
        self.comp_points = 0
        self.user_choice = 'default'
        self.comp_choice = 'default'
        user_image = PhotoImage(file=f"img/RockPaperScissor.png")
        comp_image = PhotoImage(file=f"img/RockPaperScissor.png")
        self.user_canvas.delete("all")
        self.user_canvas.create_image(0, 0, anchor='nw', image=user_image)
        self.user_canvas.image = user_image
        self.comp_canvas.delete("all")
        self.comp_canvas.create_image(0, 0, anchor='nw', image=comp_image)
        self.comp_canvas.image = comp_image
        self.user_label.configure(text=f'User: {self.user_points}')
        self.computer_label.configure(text=f'Computer: {self.comp_points}')

