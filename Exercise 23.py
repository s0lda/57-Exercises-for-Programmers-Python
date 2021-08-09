def string_input() -> str:
    valid = False
    while valid == False:
        try:
            word = input('>> ')
            if ' ' in word:
                for char in word:
                    if char.isdigit():
                        valid = False
                        print('No numbers please.')
                    elif char.isalpha() or char.isspace():
                        valid = True
                        return word
            elif not word.isalpha():
                print('Wrong input.')
            else:
                valid = True
                return word
        finally:
            pass

def diagnose_vehicle():
    print('Answer Yes or No, Y or N.')
    print('Is the car silent when you turn the key?')
    choice = string_input()
    if choice.lower() == 'yes' or choice.lower() == 'y':
        print('Are the battery terminals corroded?')
        choice = string_input()
        if choice.lower() == 'yes' or choice.lower() == 'y':
            print('Clean terminals and try starting again.')
        elif choice.lower() =='no' or choice.lower() == 'n':
            print('Replace cables and try again.')
        else:
            print('Can\'t help you if you won\'t answer the question.')
    elif choice.lower() =='no' or choice.lower() == 'n':
        print('Does the car making clicking noise?')
        choice = string_input()
        if choice.lower() == 'yes' or choice.lower() == 'y':
            print('Replace battery.')
        elif choice.lower() =='no' or choice.lower() == 'n':
            print('Does the car crank up but fail to start?')
            choice = string_input()
            if choice.lower() == 'yes' or choice.lower() == 'y':
                print('Check spark plug connection.')
            elif choice.lower() =='no' or choice.lower() == 'n':
                print('Does the engine start then die?')
                choice = string_input()
                if choice.lower() == 'yes' or choice.lower() == 'y':
                    print('Does your car have fuel injection?')
                    choice = string_input()
                    if choice.lower() == 'yes' or choice.lower() == 'y':
                        print('Check to ensure the choke is opening and closing.')
                    elif choice.lower() =='no' or choice.lower() == 'n':
                        print('Get it in for service.')
                    else:
                        print('Can\'t help you if you won\'t answer the question.')
                else:
                    print('Can\'t help you if you won\'t answer the question.')
            else:
                print('Can\'t help you if you won\'t answer the question.')
        else:
            print('Can\'t help you if you won\'t answer the question.')
    else:
        print('Can\'t help you if you won\'t answer the question.')

if __name__ == '__main__':
    diagnose_vehicle()
