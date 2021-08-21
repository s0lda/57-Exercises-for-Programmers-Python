import random

def user_input():
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) > 0:
                valid = True
                return usr_input
            else:
                print('Can\'t be blank.')
        finally:
            pass


def winner():
    contestants = []
    runners_up = 0

    print('Add contestants. When finished type exit.')
    cont_valid = False
    while cont_valid == False:
        try:
            name = user_input()
            if name == 'exit':
                cont_valid = True
            else:
                contestants.append(name)
        finally:
            pass

    winner_valid = False
    while winner_valid == False:
        try:
            print('Choose (Y)es or (N)o?')
            choice = user_input()
            if choice.lower() == 'n':
                winner_valid = True
                print('Bye Bye.')
            elif choice.lower() == 'y':
                if len(contestants) > 0:
                    x = random.choice(contestants)
                    if runners_up == 0:
                        print(f'The winner is {x}.')
                        contestants.remove(x)
                    else:
                        print(f'The runner up is {x}.')
                        contestants.remove(x)
                else:
                    print('No more participants.')
                    winner_valid = True
            else:
                print('Wrong choice.')
        finally:
            pass


if __name__ == '__main__':
    winner()