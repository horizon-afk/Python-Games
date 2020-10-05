import random

#imports the list of words from words.py
from words import words

class Hangman:
    def __init__(self):

        Hangman.game(self)

    def game(self):

        self.tries = 7
        
        #ramdomly selects a word from words.py
        self.word = random.choice(words).upper()
                
        print(self.word)
        
        #this list stores characters irrespective of them being right or wrong
        self.guessed_char = []
        
        #game events starts from here
        
        Hangman.graphics(self)
        self.word_display = "-" * len(self.word)
        Hangman.show_tries(self)
        print(self.word_display)
        self.prompt = list(self.word_display)
        
        while self.tries > 0:

            if len(self.guessed_char) > 0:
                
                Hangman.graphics(self)
                Hangman.display_prompt(self)
                Hangman.show_tries(self)
                Hangman.check_win_event(self)
            
            
            self.guess = input("Enter your guess: ").upper()
            Hangman.validation(self)
            self.guessed_char.sort()
            guessed = ",".join(self.guessed_char)
            
            print("Guessed characters: ", end="")
            print(guessed)
            
            #when user fails to guess the word

            if self.tries == 1:
                
                Hangman.graphics(self)
                Hangman.display_prompt(self)
                
                
                print(f"You lose. The corect answer was {self.word}. ")
                Hangman.end_sequence(self)
            
                
    def validation(self):
        
        if self.guess.isalpha():
              
            #for user entering the same character
        
            if self.guess in self.guessed_char:
                print("You already guessed that! Try something else.")
                
            # for user attempting a wrong guess

            elif self.guess not in self.word:
                print("\nWrong Guess. Try something else.")
                self.guessed_char.append(self.guess)
                self.tries -= 1
                   
                
            else:
                self.guessed_char.append(self.guess)

        else:
            print("Invalid Input! Please try again.")
            
            
            
    def check_win_event(self):
        
        # logic to understand when the whole word gets guessed correctly
        if "-" not in self.prompt:
            print(f"Good job. You got it. It is {self.word}")
            Hangman.end_sequence(self)
    
        # validating user's input when user enters the whole word instead of a single character
        elif self.guess == self.word:

            self.prompt = self.word

            # logic used for detemining in how many attempts the user entered the full word
            if self.tries == 6 and len(self.guessed_char) == 0:
                Hangman.graphics(self)
                Hangman.display_prompt(self)
                print("Congrats! You got it in one go.")
                Hangman.end_sequence(self)

                
            else:
                Hangman.graphics(self)
                Hangman.display_prompt(self)
                print("Congrats! You got it!")
                Hangman.end_sequence(self)
                
                
    def show_tries(self):
        if self.tries < 5:
            print(f"Warning! You have only {self.tries - 1} tries left.")
        else:
            print(f"Tries left: {self.tries - 1} ")


    # shows the main prompt for the users to see 
    def display_prompt(self):
            
        # gets the index of the letter in the word when guess is coorect and appends it to word completion as a prompt
        
        indices = [i for i, letter in enumerate(self.word) if self.guess == letter]
        for index in indices:
            self.prompt[index] = self.guess
        
        self.word_completion = "".join(self.prompt)
        
        print(self.word_completion)
        
     # the execution of the ending to let the user choose whether to paly again or quit       
    def end_sequence(self):
        
        #sequences to execute when the user wants to exit
        request = input("Press enter to play again or type exit to quit: ")

        if request == "":
            Hangman.game(self)
            
        elif request == "exit" or "quit":
            exit()
            
    def graphics(self):
       
        # the graphics of a man hanging
        stages = [
            
            """
            -------------
            |           |
            |
            |
            |
            |
            |
            |
              
            """,
            """
            -------------
            |           |
            |           O
            |  
            |
            |
            |
            |
            
            """,
            """
            
            -------------
            |           |
            |           O
            |           | 
            |           |
            |
            |
            |

            """,
            """
            
            -------------
            |           |
            |           O
            |         \ | 
            |          \|
            |
            |
            |
             
            """,
            """
     
            -------------
            |           |
            |           O
            |         \ | /
            |          \|/
            |
            |
            |
            
            """,
            """
            
            -------------
            |           |
            |           O
            |         \ | /
            |          \|/
            |           |
            |          /
            |         /
                
            """,
            """
             -------------
            |           |
            |           O
            |         \ | /
            |          \|/
            |           |
            |          / \\
            |         /   \\
            """    
        ]
        print(stages[-self.tries])
    
    
if __name__ == "__main__":
    print("Welcome to Umesh's Hangman made using Python.")
    print("Just guess the character or the full word.\n")
    Hangman()
