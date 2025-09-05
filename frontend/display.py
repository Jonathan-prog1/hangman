from assets.art import hangman_art
from backend.database import showall,delete_one
def display_man(wong_guesses):
    print("**************")
    for line in hangman_art[wong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def display_gusses(letter):
    letters = []

def delete():
    showall()
    id = input("Please enter the number to delete: ")
    delete_one(id)
    showall()
