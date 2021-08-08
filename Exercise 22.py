def int_input() -> int:
    valid = False
    while valid == False:
        try:
            number = int(input('>> '))
            if number >= 0 or number < 0:
                valid = True
                return number
            else:
                print('You need to input number.')
        finally:
            pass

def add_numbers():
    list_of_numbers = []
    while len(list_of_numbers) < 10:
        try:
            number = int_input()
            if number not in list_of_numbers:
                list_of_numbers.append(number)
            else:
                print('This number already exists in the list.')
        finally:
            pass
    return list_of_numbers

def find_highest(numbers):
    highest = -99999999999999999999999999999999999999999999999999999999999999
    for number in numbers:
        if number > highest:
            highest = number
    return highest

if __name__ == '__main__':
    print('Please input numbers to compare')
    highest_number = find_highest(add_numbers())
    print(f'Highest number is: {highest_number}.')
