def first_number():
    valid = False
    while valid == False:
        try:
            first = int(input('What is your first number? '))
            if first >= 0:
                valid = True
                break
            else:
                print('You need to provide a number greater or equal to 0.')
        except ValueError:
            print('You need to provide a number greater or equal to 0.')
    return first

def second_number():
    valid = False
    while valid == False:
        try:
            second = int(input('What is your second number? '))
            if second >= 0:
                valid = True
                break
            else:
                print('You need to provide a number greater or equal to 0.')
        except ValueError:
            print('You need to provide a number greater or equal to 0.')
    return second

first = first_number()
second = second_number()

def add(first: int, second: int) -> int:
    return first + second

def minus(first: int, second: int) -> int:
    return first - second

def multi(first: int, second: int) -> int:
    return first * second

def divide(first: int, second: int) -> int:
    return first / second

addition = add(first, second)
substraction = minus(first, second)
multiplication = multi(first, second)
division = divide(first, second)

result = f'''
{first} + {second} = {addition}
{first} - {second} = {substraction}
{first} * {second} = {multiplication}
{first} / {second} = {division}'''

def math_results(result):
    print(result)

if __name__ == '__main__':
    math_results(result)
    