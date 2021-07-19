import datetime

def age() -> int:
    current_age = int(input('What is your age? '))
    retirement = int(input('At what age would you like to retire? '))
    return retirement - current_age


def retirement_checker():
    x = age()
    if x == 0:
        print('You can retire this year.')
    elif x < 0:
        if abs(x) == 1:
            print(f'You were able to retire year ago.')
        else:
            print(f'You were able to retire {abs(x)} years ago.')
    else:
        now = datetime.datetime.now()
        year = now.year
        if x == 1:
            print(f'You have {x} year until you can retire.')
        else:
            print(f'You have {x} years until you can retire.')
        print(f'It\'s {year} now. You can retire in {year + x}.')

if __name__ == '__main__':
    retirement_checker()