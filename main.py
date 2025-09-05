import random

from frontend.display import display_man, display_hint, display_answer

from backend.word_files import add_word, show_words, load_words


def startup():
    startup = True

    while startup:
        print("***********")
        print("1) start hangman")
        print("2) Add new word to hangman game")
        print("3) Show all words")
        print("4) Quit")
        print("***********")
        
        choice = input("Please enter your choice (1-4) ")
        
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue  # Skip to the next loop iteration

        choice = int(choice)

        if choice >= 5:
            print("Invalid input")
        if choice == 1:
            main()
        if choice == 2:
            word = str(input("What word would you like to add? ")).lower()
            add_word(word)
        if choice == 3:
            show_words()
        if choice == 4:
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

        elif wrong_guesses >= len(art) - 1:
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