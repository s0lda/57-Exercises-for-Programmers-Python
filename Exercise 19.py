import math

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


def bmi_metric(weight: float, height: float) -> float:
    # weight in kilos height in meters
    return weight / (height * height)


def bmi_imperial(weight: float, height: float) -> float:
    # weight in pounds height in inches
    return (weight / (height * height)) * 703


def choose_metrics():
    print('Would you like to use imperial or metric?')
    valid = False
    while valid == False:
        try:
            choice = string_input()
            if choice.lower() == 'imperial':
                return 'imperial'
            elif choice.lower() == 'metric':
                return 'metric'
            else:
                print('You need to choose one of the options.')
        finally:
            pass


def check_bmi(bmi):
    if bmi >= 18.5 and bmi < 25:
        print(f'Your BMI is {bmi}.\nYou are within the ideal weight range.')
    elif bmi < 18.5:
        print(f'Your BMI is {bmi}.\nYou are underweight. You should see your doctor.')
    else:
        print(f'Your BMI is {bmi}.\nYou are overweight. You should see your doctor.')


def convert_feet_to_inches(height: float) -> float:
    base = math.floor(height)
    decimal = (height - base) * 10
    base_inches = base * 12
    return base_inches + decimal

def run_converter():
    metrics_choice = choose_metrics()
    if metrics_choice == 'imperial':
        print('What is your height? Please input inches after dot eg. 6\'22\'\' should be 6.2.')
        height = float_input()
        inches_height = convert_feet_to_inches(height)
        print('Please input your weight in pounds.')
        weight = float_input()
        bmi = bmi_imperial(weight, inches_height)
        check_bmi(bmi)
    else:
        print('What is your height in meters? eg. 187 cm should be 1.87.')
        height = float_input()
        print('What is your weight in kilos?')
        weight = float_input()
        bmi = bmi_metric(weight, height)
        check_bmi(bmi)


if __name__ == '__main__':
    run_converter()
