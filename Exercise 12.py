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

# according to exercise interest * years + principal

def simple_interest():
    print('What is the principal?')
    principal = user_input()
    print('What is the interest?')
    interest = user_input()
    print('Enter number of years.')
    years = user_input()
    result = (((principal / 100) * interest) * years) + principal
    year_str = ''
    if years == 1:
        year_str = 'year'
    else:
        year_str = 'years'
    print(f'After {years} {year_str} at {interest}%, the investment will be worth ${result}.')
    for year in range(1, years + 1):
        yearly_interest = (((principal / 100) * interest) * year) + principal
        print(f'Year {year}: Interest: ${yearly_interest - principal} Balance: ${yearly_interest}')

if __name__ == '__main__':
    simple_interest()
