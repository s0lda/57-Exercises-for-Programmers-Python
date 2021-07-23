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

def compounded_interest():
    print('What is the principal?')
    principal = user_input()
    print('What is the interest?')
    interest = user_input()
    print('Enter number of years.')
    years = user_input()
    print('How many times a year interest is compounded?')
    compound = user_input()

    result = round(principal * (((1 + ((interest / 100.0) / compound)) ** (compound * years))), 2)
    years_str = ''
    if years == 1:
        years_str = 'year'
    else:
        years_str = 'years'
    print(f'${principal} invested at {interest}% for {years} {years_str} compounded {compound} times per year is ${result}.')

def principal_checker():
    print('How much would you like to earn?')
    total = user_input()
    print('What is the interest?')
    interest = user_input()
    print('Enter number of years.')
    years = user_input()
    print('How many times a year interest is compounded?')
    compound = user_input()

    result = round(total / (((1 + ((interest / 100.0) / compound)) ** (compound * years))), 2)
    years_str = ''
    if years == 1:
        years_str = 'year'
    else:
        years_str = 'years'
    times = ''
    if compound == 1:
        times = 'time'
    else:
        times = 'times'
    print(f'''
To earn ${total} over {years} {years_str} with interest at {interest}% compounded {compound} {times} a year,
You will need to invest ${result}.''')

def run_calculator():
    valid = False
    print('Would you like to calculate income or check how much do you need to invest?\n Choose: calculate or check')
    while valid == False:
        try:
            choice = input('>> ')
            if choice.lower() == 'calculate':
                compounded_interest()
                valid = True
            elif choice.lower() == 'check':
                principal_checker()
                valid = True
            else:
                print('You need to choose one of the options.')
        except TypeError:
            print('You need to choose one of the options.')

if __name__ == '__main__':
    run_calculator()
