import random
import string
from sklearn.utils import shuffle

def int_input():
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if usr_input.isdigit():
                if int(usr_input) >= 0:
                    valid = True
                    return int(usr_input)
            else:
                print('Need to input numbers.')
        finally:
            pass


def generate_numbers(x):
    numbers = []
    while x != 0:
        try:
            ran_num = random.randint(0, 9)
            numbers.append(ran_num)
            x -= 1
        finally:
            pass
    return numbers


def generate_letter(x):
    letters = []
    while x != 0:
        try:
            ran_letter = random.choice(string.ascii_letters)
            letters.append(ran_letter)
            x -= 1
        finally:
            pass
    return letters


def generate_special(x):
    specials = []
    while x != 0:
        try:
            special_signs = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_')
            ran_special = random.choice(special_signs)
            specials.append(ran_special)
            x -= 1
        finally:
            pass
    return specials

def generate_password():
    print('What is the minimum lenght of your password?')
    lenght = int_input()
    print('How many special characters?')
    specials = int_input()
    print('How many numbers?')
    numbers = int_input()

    letters = lenght - specials - numbers
    pass_letter = generate_letter(letters)
    pass_special = generate_special(specials)
    pass_numbers = generate_numbers(numbers)

    pass_numbers = [str(int) for int in pass_numbers]

    password = pass_letter + pass_special + pass_numbers
    password_shuffle = shuffle(password)

    result = ''.join(password_shuffle)

    print(f'Your password is:\n{result}')

if __name__ == '__main__':
    generate_password()
