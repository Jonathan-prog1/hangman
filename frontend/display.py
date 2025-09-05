from assets.art import hangman_art

def display_man(wong_guesses):
    print("**************")
    for line in hangman_art[wong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
