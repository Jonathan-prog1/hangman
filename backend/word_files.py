def add_word(text):
    file_path = "assets/wordslist.txt"

    try:
        with open(file_path, "a") as file:
            file.write("," +text)
            print({f"added {text} to the list of words"})
    except PermissionError: 
        print("You do not have permission to wright to that file")
        chioce = input("Would you like to quit now and get permission from your computer now and then come back?(y/n) ")
        if chioce == "y":
            quit()
        
            
def show_words():
    file_path = "assets/wordslist.txt"

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
    file_path = "assets/wordslist.txt"

    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split(',')
            return words
    except FileNotFoundError:
        print("That file was not found")
    except PermissionError: 
        print("You do not have permission to read that file")
