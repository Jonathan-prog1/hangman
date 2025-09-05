import random


# Dictionary of key:()
hangman_art = {
    0: (" __    ",
        "|  |   ",
        "|      ",
        "|      ",
        "|      "),
    1: (" __    ",
        "|  |   ",
        "|  o   ",
        "|      ",
        "|      "),
    2: (" __    ",
        "|  |   ",
        "|  o   ",
        "|  |   ",
        "|      "),
    3: (" __    ",
        "|  |   ",
        "|  o   ",
        "| /|   ",
        "|      "),
    4: (" __    ",
        "|  |   ",
        "|  o   ",
        "| /|\\ ",
        "|      "),
    5: (" __    ",
        "|  |   ",
        "|  o   ",
        "| /|\\ ",
        "| /    "),
    6: (" __    ",
        "|  |   ",
        "|  o   ",
        "| /|\\ ",
        "| / \\ ")}

def display_man(wong_guesses):
    print("**************")
    for line in hangman_art[wong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def add_word(text):
    file_path = "wordslist.txt"

    try:
        with open(file_path, "a") as file:
            file.write("," +text)
            print({f"added {text} to the list of words"})
    except FileExistsError:
        print("That file already exists")

def show_words():
    file_path = "wordslist.txt"

    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split(',')
            for word in words:
                print(word)
    except FileNotFoundError:
        print("That file was not found")
    except PermissionError: 
        print("You do not have permission to read that file")
            
def load_words():
    file_path = "wordslist.txt"

    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split(',')
            return words
    except FileNotFoundError:
        print("That file was not found")
    except PermissionError: 
        print("You do not have permission to read that file")

def startup():
    startup = True
    while startup:
        print("***********")
        print("1) start hangman")
        print("2) Add new word to hangman game")
        print("3) Show all words")
        print("4) Quit")
        print("***********")
        chioce = int(input("Please enter your choice (1-4) "))
        if chioce == 1:
            main()
        if chioce == 2:
            word = str(input("What word would you like to add? ")).lower()
            add_word(word)
        if chioce == 3:
            show_words()
        if chioce == 4:
            quit()
            
def main():
    show = load_words()
    answer = random.choice(show)
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
            wrong_guesses +=1
        
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
    startup()