
#add a number to your balnce but the amount can"t be less than or equal to zero ✅
#they can take an amount that can"t be higher than their balance ✅
#they can add money to their balance ✅
#full project is successfull ✅

def get_balance():
    global balance
    while True:
        balance = input("Enter the amount you want in your balance: ")
        if balance.isdigit() and int(balance) > 0:
            balance = int(balance)
            print(f"your current balance is {balance}")
            break
        else:
            print("invalid number!")
    return balance

def get_number():
    global balance
    while True:
        taken_num = input("Enter the amount you want to take: ")
        if taken_num.isdigit() and 0 < int(taken_num) <= balance:
            taken_num = int(taken_num)
            print(f"your current balance is {balance} and you took {taken_num}")
            balance -= taken_num
            print(f"now your balance is {balance}")
            break
        else:
            print("invalid number! you can't take more or less than your balance")
            print(f"your current balance is {balance} and you took {taken_num}")
    return taken_num

def get_addition():
    global balance
    while True:
        added_num = input("Enter the amount you want to add: ")
        if added_num.isdigit() and int(added_num) > 0:
            added_num = int(added_num)
            print(f"your current balance is {balance} and you added {added_num}")
            balance += added_num
            print(f"your current balance is {balance}")
            break
        else:
            print("that is an invalid number to add!")
    return balance

def get_choice():
    while True:
        choice = input("would you like to quit (y/n): ").lower()
        if choice == 'y':
            break
        else:
            choice2 = input("would you like to add an amount or take an amount (a/t): ").lower()
            if choice2 == 'a':
                getting_added_num = get_addition()
                continue
            elif choice2 == 't':
                getting_number = get_number()
                continue
            else:
                print("that isn't an option!")
        return choice or choice2
        
def main():
    getting_balance = get_balance()
    getting_choice = get_choice()

main()