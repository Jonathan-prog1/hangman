import random
import os

from assets.art import hangman_art
from frontend import display
from backend.database import Database

def checks():
    
    # The path to the db
    file_path = "backend/wordlist.db"
    # This checks to see if the DB is there
    if os.path.exists(file_path):
        print(f"The file {file_path} is there")
    # this checks to see if there is no DB and if there is not it creates it and adds some sample words
    elif not os.path.exists(file_path):
        db = Database()
        print("Genrtating sample word list")
        db.create_table()
        #this adds a simple list to let people try out hangman without haveing to add there own
        sample_list = [("apple",),("orange",),("banana",),("coconut",),("pineapple",)]
        db.add_sample(sample_list)

def startup():
    startup = True
    
    while startup:
        # Displays all the choices of what to do
        display.main_menu()
        choice = input("Please enter your choice (1-6) ")
        
        # checks to see if you entered a number
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 5.")
            continue  # Skip to the next loop iteration
        
        # Changes the input string to a number
        choice = int(choice)
        # Checks to make the number is within the rang for all the ops of the main menu
        if choice >= 7:
            print("Invalid input")
        # Starts the hangman game
        if choice == 1:
            main()
        # Lets you add one word to the db
        if choice == 2:
            display.add_word()
        # Lets you edit a word in the db
        if choice == 3:
            display.edit_word()
        # Shows all words in the db
        if choice == 4:
            display.display_allwords()
        # Lets you delete one word from the db
        if choice == 5:
            display.delete()
        # Kills the programe
        if choice == 6:
            quit()
        
def main():
    db = Database()

    # This gets all the words from the db
    word = db.all_words()
    # This picks a word at random to use for hangman
    answer = random.choice(word)
    # This sets _ for all the letters of the word till you gusse the letter
    hint = ["_"] * len(answer)
    # This keeps track of how many times you guessed a wrong letter to update the hangman art 0-6
    wrong_guesses = 0
    # This setups the place to hold all the letters you have guessed so far
    guessed_letters = set()
    # This keeps track of if the game should still be running or not
    is_running = True
    

    while is_running:
        #this displays the art for hangman
        display.display_man(wrong_guesses)

        # This prints all the letter spots
        display.display_hint(hint)

        # This displays all the letters you have guessed so far
        display.display_gusses(guessed_letters)
        
        # This is where the user inputs there guess of what letter is on the board
        guess = input("Enter a letter: ").lower()
        
        # This checks the user input to make sure it is only one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        
        # This checks to see if you have already guessed that letter
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)

        # This places the letter where it is in the word
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        # This updates the hangman art if you guess the wrong letter
        else:
            wrong_guesses += 1
        
        # This sees if you have fully guessed the word and if you have before you make 6 wrong letters you win
        if "_" not in hint:
            display.display_man(wrong_guesses)
            display.display_answer(answer)
            print("YOU WIN!")
            is_running = False

        # This stops the game if you do 6 wrong words and tells you what the word was
        elif wrong_guesses >= len(hangman_art) - 1:
            display.display_man(wrong_guesses)
            display.display_answer(answer)
            print("YOU LOSE!")
            is_running = False

    # This lets you restart the game with a new word if you want to play agin
    playagine = input("Do you want to play agin?(y/n) ").lower()

    if playagine == "y":
        main()
    if playagine == "n":
        quit()

if __name__ == "__main__":
    checks()
    startup()
    