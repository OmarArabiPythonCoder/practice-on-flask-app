
import random


questions = {
    'how many elements are in the periodic table?':'118',
    'what does x + 2.6 =4.6':'2',
    'what will this code return print(x)':'x',
    'in x proccess the water changes from liquid state into gas state': 'evaporation',
    'in x proccess water changes from gas state into liquid state': 'condensation',
    'in the equation 2 + 123':'125',
    'what does perpindicular mean': 'vertical',
    'hitler fought in x': 'ww2',
    'what does x + 5.6 = 11':'5.4'
}


grade = 0
choices = []
def main(grade):
    while len(choices) != 5:
        choose = random.choice(list(questions))
        choices.append(choose)
        if choices.count(choose) >= 2:
            choices.remove(choose)
    for ch in choices:
        print(ch)
        answer = input('> ')
        dict(key = choose, value = questions.get(ch))
        if answer == questions.get(ch):
            print('correct!')
            grade += 1
        else:
            print('wrong!')
    if grade == 3:
        print(f'your grade is {grade}/5')
        print('you passed')
    elif grade <= 2:
        print(f'your grade is {grade}/5')
        print('you failed')
    elif grade >= 4:
        print(f'your grade is {grade}/5')
        print('excellent!')


main(grade=grade)