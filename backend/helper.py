
def check_input_number(number:str):
    """This is a helper fuc to see if the input is a number in a string"""
    if not number.isdigit():
        #print("Please Enter a number")
        raise ValueError("Please Enter a number")
    return 0


def check_input_word(word:str):
    """This is a helper fuc to see if the input is only letters in a string"""
    if not isinstance(word, str):
        raise ValueError("Please Enter a letter a-z")
    if not word.isalpha():
        raise ValueError("Please Enter a letter a-z")
    return 0