import tkinter as tk
from tkinter import messagebox



class myGame(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Tic - Tac - Toe")
        self.geometry("249x450+500+250")
        self.resizable(0, 0)

        # this variable tells the program understand the current playing user

        self.player = 1

        self.score_player1 = 0
        self.score_player2 = 0

        self.p1name = ""
        self.p2name = ""
        myGame.status(self)
        myGame.player_names(self)
        myGame.player_symbols(self)
        myGame.scoreboard(self)

        myGame.setup(self)

    # to display the player scores and update them

    def player_names(self):
        self.p1name = tk.Entry(self, font = ("Comic Sans MS", 16), width = 7)
        self.p1name.place(x = 1, y = 1)

        self.p2name = tk.Entry(self, font = ("Comic Sans MS", 16), width = 7)
        self.p2name.place(x = 125, y = 1)

    def player_symbols(self):
        symbol_x = tk.Label(self, text = "(X)", font = ("Comic Sans MS", 16))
        symbol_x.place(x = 90, y = 1)
        
        symbol_o = tk.Label(self, text = "(0)", font = ("Comic Sans MS", 16))
        symbol_o.place(x=210, y = 1)
        
    def scoreboard(self):
        p1score = tk.Label(self, text = f"Score = {self.score_player1}", font = ("Comic Sans MS", 16))
        p1score.place(x = 1, y = 35)
        
        p1score = tk.Label(self, text = f"Score = {self.score_player2}", font = ("Comic Sans MS", 16))
        p1score.place(x = 125, y = 35)
        
    # shows the status about turns and pressing start 
        
    def status(self):
        
        self.statuslive = tk.Label(self, text = "Enter your name and\n press start to play", font = ("Comic Sans MS", 15))
        self.statuslive.place(x = 20, y = 65)
        
    def player_turn(self):
        if self.player == 1:
                self.statuslive.config(text=f"Turn: {self.p1}")

        elif self.player == 2:
                self.statuslive.config(text = f"Turn: {self.p2}")
        

    def setup(self):
        

        button1 = tk.StringVar()
        button2 = tk.StringVar()
        button3 = tk.StringVar()
        button4 = tk.StringVar()
        button5 = tk.StringVar()
        button6 = tk.StringVar()
        button7 = tk.StringVar()
        button8 = tk.StringVar()
        button9 = tk.StringVar()
        
       

        # the list records the buttons pressed by the users

        self.player1 = []
        self.player2 = []

        # when the buttons are clicked

        def click(num):

            if self.player == 1:
                config_input(num, "X")
                self.player1.append(num)
                self.player = 2

            elif self.player == 2:
                config_input(num, "O")
                self.player2.append(num)
                self.player = 1
                
            check_if_win()

            #used here for updating the status of the turns
            
            myGame.player_turn(self)

         # the rules to validate a win event

        def check_if_win():

            # For player 1

            if (1 in self.player1) and (2 in self.player1) and (3 in self.player1):
                player1_won()

            elif (4 in self.player1) and (5 in self.player1) and (6 in self.player1):
                player1_won()

            elif (7 in self.player1) and (8 in self.player1) and (9 in self.player1):
                player1_won()

            elif (1 in self.player1) and (4 in self.player1) and (7 in self.player1):
                player1_won()

            elif (2 in self.player1) and (5 in self.player1) and (8 in self.player1):
                player1_won()

            elif (3 in self.player1) and (6 in self.player1) and (9 in self.player1):
                player1_won()

            elif (1 in self.player1) and (5 in self.player1) and (9 in self.player1):
                player1_won()

            elif (3 in self.player1) and (5 in self.player1) and (7 in self.player1):
                player1_won()

            # For player 2

            elif (1 in self.player2) and (2 in self.player2) and (3 in self.player2):
                player2_won()

            elif (4 in self.player2) and (5 in self.player2) and (6 in self.player2):
                player2_won()

            elif (7 in self.player2) and (8 in self.player2) and (9 in self.player2):
                player2_won()

            elif (1 in self.player2) and (4 in self.player2) and (7 in self.player2):
                player2_won()

            elif (2 in self.player2) and (5 in self.player2) and (8 in self.player2):
                player2_won()

            elif (3 in self.player2) and (6 in self.player2) and (9 in self.player2):
                player2_won()

            elif (1 in self.player2) and (5 in self.player2) and (9 in self.player2):
                player2_won()

            elif (3 in self.player2) and (5 in self.player2) and (7 in self.player2):
                player2_won()

            # special case for a draw event

            if (len(self.player1) == 5 and len(self.player2) == 4) or (len(self.player1) == 4 and len(self.player2) == 5):
                draw_game()

        def player1_won():

            tk.messagebox.showinfo(f"{self.p1} won", f"Sorry! Next Time, {self.p2}.\n Press start again to start")
            self.score_player1 += 1
            myGame.scoreboard(self)
            restart_game()

        def player2_won():
            tk.messagebox.showinfo(f"{self.p2} won", f"Sorry! Next Time, {self.p1}.\n Press start again to start")
            self.score_player2 += 1
            myGame.scoreboard(self)
            restart_game()

        def draw_game():
            tk.messagebox.showinfo("Draw!", "Nobody could win")
            restart_game()

        def restart_game():
            myGame.setup(self)

        def config_input(num, symbol):
            if num == 1:
                button1.set(symbol)
                btn1.config(state = 'disabled')

            elif num == 2:
                button2.set(symbol)
                btn2.config(state = 'disabled')

            elif num == 3:
                button3.set(symbol)
                btn3.config(state = 'disabled')

            elif num == 4:
                button4.set(symbol)
                btn4.config(state = 'disabled')

            elif num == 5:
                button5.set(symbol)
                btn5.config(state = 'disabled')

            elif num == 6:
                button6.set(symbol)
                btn6.config(state = 'disabled')

            elif num == 7:
                button7.set(symbol)
                btn7.config(state = 'disabled')

            elif num == 8:
                button8.set(symbol)
                btn8.config(state = 'disabled')

            elif num == 9:
                button9.set(symbol)
                btn9.config(state = 'disabled')

        def start():
            btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

            # the buttons are now active for user input

            for btn in btns:
                btn.config(state = 'active')

            score_board = [self.p1name, self.p2name]

            for score in score_board:
                score.config(state = 'readonly')
                
            btnStart.config(text = "Running")
            
            self.p1 = self.p1name.get()
            self.p2 = self.p2name.get()
            
            # if the players don't enter their names then the label for turns are not left blank
            if self.p1 == "" and self.p2 == "":
                
                self.p1 = "Player 1"
                self.p2 = "Player 2"
            
            # used here for the hitting enter or clicking on start
            
            myGame.player_turn(self)
            
        def exit():
            self.destroy()

        # the button for strating the main game

        btnStart = tk.Button(self, text = "Start", font = ("Calibri", 16), width = 6, command = start)
        btnStart.place(x = 1, y = 400)
        
        # the button for refresh
        
        btnRestart = tk.Button(self, text = "Restart", font = ("Calibri", 16), width = 7, command = restart_game)
        btnRestart.place(x = 80, y = 400)

        # the buttons to exit
        btnExit = tk.Button(self, text="Exit", font=("Calibri", 16), width = 6, command = exit)
        btnExit.place(x = 172, y = 400)

        btn_h = 2
        btn_w = 5
        
        

        # the main gaming buttons
        # the buttons are disabled to prevent unwanted input from the user before the game starts

        btn1 = tk.Button(self, state = 'disabled', textvariable = button1, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(1))
        btn1.place(x = 7, y = 126)

        btn2 = tk.Button(self, state = 'disabled', textvariable = button2, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(2))
        btn2.place(x = 87, y = 126)

        btn3 = tk.Button(self, state = 'disabled', textvariable = button3, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(3))
        btn3.place(x = 167, y = 126)

        btn4 = tk.Button(self, state = 'disabled', textvariable = button4, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(4))
        btn4.place(x = 7, y = 211)

        btn5 = tk.Button(self, state = 'disabled', textvariable = button5, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(5))
        btn5.place(x = 87, y = 211)

        btn6 = tk.Button(self, state = 'disabled', textvariable = button6, font = ("Comic Sans MS Bold", 16), height =btn_h, width = btn_w,  command = lambda: click(6))
        btn6.place(x = 167, y = 211)

        btn7 = tk.Button(self, state = 'disabled', textvariable = button7, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(7))
        btn7.place(x = 7, y = 296)

        btn8 = tk.Button(self, state = 'disabled', textvariable = button8, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(8))
        btn8.place(x = 87, y = 296)

        btn9 = tk.Button(self, state = 'disabled', textvariable = button9, font = ("Comic Sans MS Bold", 16), height = btn_h, width = btn_w, command = lambda: click(9))
        btn9.place(x = 167, y = 296)
        
       

        


if __name__ == "__main__":
    root = myGame()
    root.mainloop()
