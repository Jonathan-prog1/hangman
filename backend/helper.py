# This is a helper fuc to see if the input is a number
def check_input_number(number):
    if not number.isdigit():
        print("Please Enter a number")

# This is a helper fuc to see if the input is only letters
def check_input_word(word):
    if not word.isalpha():
        print("Please enter letters a-z")