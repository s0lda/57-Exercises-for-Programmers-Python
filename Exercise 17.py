# exercise blood alcohol level 0.08

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

def string_input():
    valid = False
    while valid == False:
        try:
            word = input('>> ')
            if not word.isalpha():
                print('Can\'t use numbers.')
            else:    
                valid = True
                return word
        finally:
            pass

def blood_alcohol(A: float, W: float, r: float, H: float) -> float:
    # A alcohol consumed in oz
    # W body weight in pounds
    # r alcohol distribution ratio
    # H number of hours since last drink
    return (A * 5.14 / W * r) - 0.015 * H

def l_to_oz(liter: float) -> float:
    return liter * 33.814022558919

def kg_to_pound(kilo: float) -> float:
    return kilo / 0.45359237

def run_calculator():
    alcohol = 0
    weight = 0
    distribution_ratio = 0

    units_choice = ''

    print('Do you want to use metric units? Yes or No?')
    
    units_valid = False
    while units_valid == False:
        try:
            units = string_input()      
            if units.lower() == 'yes' or units.lower() == 'y':
                units_choice = 'metric'
                units_valid = True
            elif units.lower() == 'no' or units.lower() == 'n':
                units_choice = 'imperial'
                units_valid = True
            else:
                print('Need to choose on of the options.')
        finally:
            pass
    
    print('How much of alcohol you\'ve had?')
    alcohol_amount = float_input()
    print('What is your weight?')
    user_weight = float_input()
   
    if units_choice == 'metric':
        alcohol = l_to_oz(alcohol_amount)
        weight = kg_to_pound(user_weight)
    else:
        alcohol = alcohol_amount
        weight = user_weight

    print('Are you male or female?')
    sex_valid = False
    while sex_valid == False:
        try:
            sex = string_input()
            if sex.lower() == 'male':
                distribution_ratio = 0.73
                sex_valid = True
            elif sex.lower() == 'female':
                distribution_ratio = 0.66
                sex_valid = True
            else:
                print('You need to choose one of the options.')
        finally:
            pass

    print('How many hours ago you\'ve had your last drink?')
    time_since = float_input()

    bac = blood_alcohol(alcohol, weight, distribution_ratio, time_since)

    if bac >= 0.08:
        print(f'Your BAC is {bac}.\nIt is not legal for you to drive.')
    else:
        print(f'Your BAC is {bac}.\nIt is legal for you to drive.')

if __name__ == '__main__':
    run_calculator()
