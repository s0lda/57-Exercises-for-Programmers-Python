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

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9

def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

def kelvin_to_celsius(temp):
    return temp - 273.15

def celsius_to_kelvin(temp):
    return temp + 273.15

def run_converter():
    temp_from = ''
    temp_to = ''

    print('What temperature do you want to convert? (K)elvin, (F)ahrenheit or (C)elsius?')
    first_temp_valid = False
    while first_temp_valid == False:
        try:
            first_temp = string_input()
            if first_temp.lower() == 'k':
                temp_from = 'Kelvin'
                first_temp_valid = True
            elif first_temp.lower() == 'c':
                temp_from = 'Celsius'
                first_temp_valid = True
            elif first_temp.lower() == 'f':
                temp_from = 'Fahrenheit'
                first_temp_valid = True
            else:
                print('Choose one of the options.')
        finally:
            pass
    
    
    print('What temperature do you want to convert it to? (K)elvin, (F)ahrenheit or (C)elsius?')
    second_temp_valid = False
    while second_temp_valid == False:
        try:
            second_temp = string_input()
            if second_temp.lower() == 'k':
                temp_to = 'Kelvin'
                second_temp_valid = True
            elif second_temp.lower() == 'c':
                temp_to = 'Celsius'
                second_temp_valid = True
            elif second_temp.lower() == 'f':
                temp_to = 'Fahrenheit'
                second_temp_valid = True
            else:
                print('Choose one of the options.')
        finally:
            pass

    print(f'What is your {temp_from} temperature?')
    temperature_in = float_input()
    temperature_out = 0
    
    if temp_from == 'Celsius' and temp_to == 'Kelvin':
        temperature_out = celsius_to_kelvin(temperature_in)
    elif temp_from == 'Celsius' and temp_to == 'Fahrenheit':
        temperature_out = celsius_to_fahrenheit(temperature_in)
    elif temp_from == 'Fahrenheit' and temp_to == 'Celsius':
        temperature_out = fahrenheit_to_celsius(temperature_in)
    elif temp_from == 'Fahrenheit' and temp_to == 'Kelvin':
        temporary = fahrenheit_to_celsius(temperature_in)
        temperature_out = celsius_to_kelvin(temporary)
    elif temp_from == 'Kelvin' and temp_to == 'Celsius':
        temperature_out = kelvin_to_celsius(temperature_in)
    else:
        temporary = kelvin_to_celsius(temperature_in)
        temperature_out = celsius_to_fahrenheit(temporary)

    print(f'Your {temp_from} temperature is {temperature_in}.\nConverted to {temp_to} this is {temperature_out}.')

if __name__ == '__main__':
    run_converter()
