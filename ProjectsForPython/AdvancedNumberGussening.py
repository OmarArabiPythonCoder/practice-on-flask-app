#do the normal number guessing game where you pick a random number and the user must guess it 🔥
#but add a twist there will be hints based on if it is higher or lower 🔥

import random
from rich.console import Console
from rich.text import Text

numbers = (13,23,39,44,76,89)
def get_num():
    return random.choice(numbers)

def get_assets():
    cs = Console()
    text = Text("🔥welcome to number guess🔥", style="red")
    cs.print(text)
    print("guess the number (0-100)")
    print("You have ten tries")
    return text

def get_guess(choice):
    num = 0
    while True:
        guess = input("enter your guess: ")
        if guess.isdigit() and 0 <= int(guess) <= 100:
            guess = int(guess) 
            num += 1
            chances = 10 - num
            if guess == choice:
                print("YOU WIN!")
                break
            else:
                print(f"you have {chances} chances left")
                if guess > choice:
                    print("the number is smaller than your choice")
                elif guess < choice:
                    print("the number is larger than your choice")
                elif num > 10:
                    print("YOU LOSE")
                    break
        else:
            print("invalid number")
    return guess

def main():
    getting_assets = get_assets()
    choice = get_num()
    getting_guess = get_guess(choice)
    y_n = input("would you like to play again (y/n): ").lower()
    if y_n == 'y':
        main()
    else:
        print("okay see ya!")

main()