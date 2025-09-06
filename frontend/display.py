from assets.art import hangman_art
from backend.database import showall,delete_one,add_one

def main_menu():
    print("***********")
    print("1) start hangman")
    print("2) Add new word to hangman game")
    print("3) Show all words")
    print("4) Delete one word")
    print("5) Quit")
    print("***********")

def add_word():
    adding_word = True
    while adding_word:
        word = str(input("What word would you like to add? ")).lower()
        add_one(word)
        choice = input("Do you whant to add another word?(y/n) ")

        if choice == "n":
            adding_word = False
        if choice == "y":
            continue

def display_man(wong_guesses):
    print("**************")
    for line in hangman_art[wong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def display_gusses(guesses):
    print(' '.join(guesses))

def delete():
    display_allwords()
    print("11: Back")
    selected_id = input("Please enter the number to delete: ")
    if not selected_id.isdigit():
        print("invalid input")
    elif selected_id == "11":
        return None
    elif selected_id <"11":
        delete_one(selected_id)
        display_allwords()

def display_allwords():
    words = showall()
    for word in words:
        print(f"{word[0]}: {word[1]}")