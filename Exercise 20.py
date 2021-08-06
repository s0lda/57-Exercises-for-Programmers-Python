def float_input() -> float:
    valid = False
    while valid == False:
        try:
            number = float(input('>> '))
            if number > 0:
                valid = True
                return number
            else:
                print('Need to be a positive number.')
        except ValueError:
            print('You need to input a number.')


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


def tax_calculator():
    print('What is the order amount?')
    order = float_input()
    tax = 0
    
    print('What is the state?')
    state = string_input()
    if state.upper() == "WI" or state.capitalize() == 'Wisconsin':
        # 5 % tax is exercise requirement and extra tax for two states
        print('What is your county of residence?')
        county = string_input()
        if county.lower() == 'eau claire':
            tax = (order / 100) * 5.005
        elif county.lower() == 'dunn':
            tax = (order / 100) * 5.004
        else:
            tax = (order / 100) * 5
    elif state.upper() == 'IL' or state.capitalize() == 'Illinois':
        tax = (order / 100) * 8
    else:
        print(f'The subtotal is ${order}\nThe total is ${order}')
    
    total = round(order + tax, 2)
    if tax > 0:
        print(f'The subtotal is ${order}\nThe tax is ${tax}\nThe total is ${total}')


if __name__ == "__main__":
    tax_calculator()
