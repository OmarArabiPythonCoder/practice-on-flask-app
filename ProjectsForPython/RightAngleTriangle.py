def get_drawing():
    while True:
        shape = input("slect a shape: ")
        if shape == '' or shape == ' ':
                print("that is an invalid character!")
        else:
            break
    while True:
        amount = input("select the amount of lines you want: ")
        if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                break
        else:
            print("invalid syntax!")
    for i in range(1, amount+1):
        print(shape*i)
    
    choice = input("would you like to draw again (y/n): ").lower()
    if choice == 'y':
        get_drawing()
    else:
        print("ok see ya!")

get_drawing()