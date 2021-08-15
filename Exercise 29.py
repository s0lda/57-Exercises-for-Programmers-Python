def user_input() -> int:
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if usr_input.isdigit():
                if int(usr_input) == 0:
                    print('Need to be a positive number.')
                else:
                    valid = True
                    return int(usr_input)
            else:
                print('That is not a valid input.')
        finally:
            pass

def rule_of_72(rate) -> int:
    return 72 / rate


def check_investment():
    print('What is the rate of investment?')
    years = rule_of_72(user_input())
    if years == 1:
        print(f'It will take 1 year to double your initial investment.')
    else:
        print(f'It will take {round(years, 2)} years to double your initial investment.')

if __name__ == '__main__':
    check_investment()
