import random

passwords = []
numbers = []
letters = []
special_chs = []
characters = [numbers, letters, special_chs]
def passs():
    while True:
        num = random.randint(0, 5)
        str(num)
        numbers.append(num)
        letter = random.choice('zadhgetuZADHGETU')
        letters.append(letter)
        special_ch = random.choice('#@$!*&^%~')
        special_chs.append(special_ch)
        if characters.count(num or special_ch or letter) >= 2:
            characters.remove()
        elif len(numbers and letters and special_chs) == 5:
            for list in characters:
                for ele in list:
                    password = random.choice(list)
                    passwords.append(password)
                    random.shuffle(passwords)
            print('the password we recommend is:')
            print(''.join(map(str,passwords)))
            break
passs()