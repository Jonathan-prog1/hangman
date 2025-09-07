from assets.art import hangman_art
from backend import database
from backend.helper import check_input_number, check_input_word
def main_menu():
    print("***********")
    print("1) start hangman")
    print("2) Add new word to hangman game")
    print("3) Edit word")
    print("4) Show all words")
    print("5) Delete one word")
    print("6) Quit")
    print("***********")

# This is the menu to add a new word to the db
def add_word():
    adding_word = True
    while adding_word:
        word = str(input("What word would you like to add? ")).lower()
        database.add_one(word)
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

# This is the menu for deleting a word from the db
def delete():
    deleteing = True
    while deleteing:
        display_allwords()
        print("11: Back")
        selected_id = input("Please enter the number to delete: ")
        check_input_number(selected_id)
        if selected_id == "11":
            deleteing = False
            break
        elif selected_id <"11":
            database.delete_one(selected_id)
            display_allwords()
            deleteing = False

# This displays all words to the screen
def display_allwords():
    words = database.showall()
    for word in words:
        print(f"{word[0]}: {word[1]}")

# This is the menu to change a word in the db
def edit_word():
    editing = True
    is_not_word = True
    while editing:
        display_allwords()
        print("11: back")
        selected_id = input("What word do you want to edit? ")
        
        # checks to see if you entered a number
        check_input_number(selected_id)

        # brings you back to the main menu
        if selected_id == "11":
            editing = False
            break
        
        item = database.one_word(selected_id)
        while is_not_word:
            for word in item:
                print(f"you selected {word} to edit")
            new_word = input("What would you like to change it to? ")
            if new_word.isalpha():
                is_not_word = False
            check_input_word(new_word)

        database.update_word(new_word, selected_id)
        display_allwords()
        choice = input("would you like to edit anther word?(y/n) ")
        # Brings you back to the main menu
        if choice == "n":
            editing = False
        elif choice == "y":
            continue