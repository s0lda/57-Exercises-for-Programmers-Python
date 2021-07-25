def user_input():
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

def check_state():
    valid = False
    while valid == False:
        try:
            state = input('>> ')
            if not state.isalpha():
                print('States don\'t contain numbers.')
            else:    
                valid = True
                return state
        finally:
            pass

def tax_calculator():
    print('What is the order amount?')
    order = user_input()
    print('What is the state?')
    state = check_state()
    if state.upper() == "WI" or state.capitalize() == 'Wisconsin':
        # 5.5 % tax is exercise requirement
        tax = (order / 100) * 5.5
        total = order + tax
        print(f'The subtotal is ${order}\nThe tax is ${tax}\nThe total is ${total}')
    else:
        print(f'The subtotal is ${order}\nThe total is ${order}')

if __name__ == "__main__":
    tax_calculator()
