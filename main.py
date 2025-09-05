import random
import os

from assets.art import hangman_art
from frontend.display import display_man, display_hint, display_answer,delete
from backend.database import all_words,showall,add_one,create_table,add_sample


def checks():
    file_path = "wordlist.db"
    if os.path.exists(file_path):
        print(f"The file {file_path} is there")
    elif not os.path.exists(file_path):
        print("Genrtating sample word list")
        create_table()
        #this adds a simple list to let people try out hangman without haveing to add there own
        sample_list = [("apple",),("orange",),("banana",),("coconut",),("pineapple",)]
        add_sample(sample_list)

def startup():
    startup = True

    while startup:
        print("***********")
        print("1) start hangman")
        print("2) Add new word to hangman game")
        print("3) Show all words")
        print("4) Delete one word")
        print("5) Quit")
        print("***********")
        
        choice = input("Please enter your choice (1-4) ")
        
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue  # Skip to the next loop iteration

        choice = int(choice)

        if choice >= 6:
            print("Invalid input")
        if choice == 1:
            main()
        if choice == 2:
            word = str(input("What word would you like to add? ")).lower()
            add_one(word)
        if choice == 3:
            showall()
        if choice == 4:
            delete()
        if choice == 4:
            quit()
        
def main():
    word = all_words()
    answer = random.choice(word)
    print(answer)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False
    playagine = input("Do you want to play agin?(y/n) ").lower()

    if playagine == "y":
        main()
    if playagine == "n":
        quit()

if __name__ == "__main__":
    checks()
    startup()
    