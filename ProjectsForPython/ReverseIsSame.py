def get_word():
    word = list(input("Enter the word you want to check you baka: "))
    copy_word = word.copy()
    copy_word.reverse()
    if word == copy_word:
        print("it is the same")
    else:
        print("these are not the same")
    return word


get_word()