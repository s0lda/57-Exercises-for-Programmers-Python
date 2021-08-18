import random

def user_input() -> str:
    valid = False
    while valid == False:
        try:
            usr_inp = input('>> ')
            if len(usr_inp) == 0:
                print('No input. Try again.')
            else:
                valid = True
                return usr_inp
        finally:
            pass


def is_number(check: str) -> bool:
    if check.isdigit():
        return True
    return False


def difficulty(choice):
    if choice == 1:
        return 10
    elif choice == 2:
        return 100
    elif choice == 3:
        return 1000


def guess_the_number():
    print('Let\'s play Guess the Number.\nPick difficulty level (1, 2, 3):')
    difficulty_valid = False
    while difficulty_valid == False:
        try:
            diff_choice = user_input()
            if is_number(diff_choice) == True:
                diff_choice = int(diff_choice)
                difficulty_valid = True
            else:
                print('Pick level.')
        finally:
            pass

    secret_number = random.randint(1, difficulty(diff_choice))
    attempts = 0
    choosen_numbers = []

    print('I have my number. What is your guess?')
    guess_valid = False
    while guess_valid == False:
        try:
            guess = user_input()
            if is_number(guess) == True:
                if int(guess) in choosen_numbers:
                    attempts += 1
                    print('You have already choosen this number. Try again.')
                elif int(guess) not in choosen_numbers:
                    if int(guess) == secret_number:
                        guess_valid = True
                        attempts += 1
                    elif int(guess) < secret_number:
                        attempts += 1
                        choosen_numbers.append(guess)
                        print('Too low. Guess again.')
                    else:
                        attempts += 1
                        choosen_numbers.append(guess)
                        print('Too high. Guess again.')
            else:
                attempts += 1
                print('That is not a number.')
        finally:
            pass
    
    if attempts == 1:
        print('You’re a mind reader!')
    elif attempts == 2 or attempts == 3:
        print('Most impressive.')
    elif attempts >= 4 and attempts <= 6:
        print('You can do better than that.')
    else:
        print('Better luck next time.')

    print(f'Number of guesses: {attempts}')

if __name__ == '__main__':
    guess_the_number()
