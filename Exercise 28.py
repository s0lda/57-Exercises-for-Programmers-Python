def user_input() -> str:
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) != 0:
                valid = True
                return usr_input
            else:
                print('Can\'t be empty')
        finally:
            pass


def check_input(usr_input) -> int:
    if usr_input.isdigit():
        return int(usr_input)
    else:
        return 0

#non numeric values to be treated as attempt (0).
def run_calculator():
    print('How many numbers would you like to add?')
    number_of_numbers = check_input(user_input())
    attempts = 0
    numbers_to_add = []
    print('Enter numbers to add:')
    while attempts != number_of_numbers:
        try:
            num = check_input(user_input())
            numbers_to_add.append(num)
            attempts += 1
        finally:
            pass
    
    print(f'The total is: {sum(numbers_to_add)}.')
    
if __name__ == '__main__':
    run_calculator()
