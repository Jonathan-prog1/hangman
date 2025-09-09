from assets.art import hangman_art
from backend.database import Database 
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

def add_word():
    """This is the menu to add a new word to the db"""
    db = Database()
    while True:
        
        while True:
            word = ""
            try:
                word = str(input("What word would you like to add? ")).lower()
                check = check_input_word(word) # this raises ValueError if invalid
            except ValueError as e:
                print(e)
                continue
            if check == 0:
                db.add_one(word)
            while True:
                choice = input("Do you whant to add another word?(y/n) ")
                if choice == "n":
                    db.close()
                    return # exit function
                elif choice == "y":
                    break  # break inner loop and prompt for next word
                else:
                    print("Please enter y or n.")

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
    """This is the menu for deleting a word from the db"""
    db = Database()
    deleteing = True
    while deleteing:
        display_allwords()
        print("0: Back")
        try:
            selected_id = input("Please enter the number to delete: ")
            check = check_input_number(selected_id)
        except ValueError as e:
                print(e)
                continue
        if selected_id == "0":
            deleteing = False
            db.close()
            break
        
        db.delete_one(selected_id)
        display_allwords()

def display_allwords():
    """This displays all words to the screen"""
    db = Database()
    words = db.showall()
    for word in words:
        print(f"{word[0]}: {word[1]}")

def edit_word():
    """This is the menu to change a word in the db"""
    db = Database()
    editing = True
    is_not_word = True
    while editing:
        display_allwords()
        print("0: back")
        try:
            selected_id = input("What word do you want to edit? ")
            check =check_input_number(selected_id)
        except ValueError as e:
            print(e)
            continue

        # brings you back to the main menu
        if selected_id == "0":
            editing = False
            break
        
        item = db.one_word(selected_id)
        while is_not_word:
            for word in item:
                print(f"you selected {word} to edit")
            try:
                new_word = input("What would you like to change it to? ")
                check = check_input_word(new_word)
                break
            except ValueError as e:
                print(e)
                continue

        db.update_word(new_word, selected_id)
        display_allwords()
        choice = input("would you like to edit anther word?(y/n) ")
        # Brings you back to the main menu
        if choice == "n":
            db.close()
            editing = False
        elif choice == "y":
            continue
        else:
            print("Please enter y or n.")