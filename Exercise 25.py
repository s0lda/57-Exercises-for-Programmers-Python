def user_input():
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) > 0:
                valid = True
                return usr_input
            else:
                print('Can\'t be empty.')
        finally:
            pass


def password_validator(password):
    specials = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\'', '|', '}', '{', '~', ':', ']']
    if len(password) < 8:
        if password.isdigit():
            return 1
        elif password.isalpha():
            return 2
        else:
            return 0
    else:
        storage = []
        for char in password:
            if char.isalpha() or char.isdigit() or char in specials:
                storage.append(char)
                compare = ''.join(storage)
                if compare == password:
                    for item in storage:
                        if item in specials:
                            return 4
                    return 3


def validator_output(password, validation):
    if validation == 0:
        print(f'The password {password} doesn\'t meet requirements. Try again.')
    elif validation == 1:
        output = 'very weak password'
    elif validation == 2:
        output = 'weak password'
    elif validation == 3:
        output = 'strong password'
    elif validation == 4:
        output = 'very strong password'

    if validation > 0:
        print(f'The password {password} is a {output}.')

if __name__ == '__main__':
    print('Please type in your password for validation.')
    password = user_input()
    validation = password_validator(password)
    validator_output(password, validation)
