import math

#gallon is enough to paint 350 square feet and cannot buy partial gallons

def ceiling_type() -> str:
    valid = False
    while valid == False:
        try:
            print('What type of ceiling do you want to paint?\nRectangular, Round or L-shape?')
            choice = input('>> ')
            if choice.lower() == 'rectangular':
                valid = True
                return 'rectangular'
            elif choice.lower() == 'round':
                valid = True
                return 'round'
            elif choice.lower() == 'L-shape' or choice.lower() == 'lshape' or choice.lower() == 'l':
                valid = True
                return 'lshape'
            else:
                print('You need to choose one of the options.')
        except TypeError:
            print('Choose from options provided.')

def rectangular():
    valid = False
    while valid == False:
        try:
            length = int(input('What is the lenght of the ceiling? '))
            width = int(input('What is the widht of the ceiling? '))
            if length > 0 and width > 0:
                valid = True
                return length * width
            else:
                print('Values need to be a positive number. Check them again.')
        except ValueError:
            print('You need to use numbers.')

def round():
    valid = False
    while valid == False:
        try:
            diameter = int(input('What is a diameter of your ceiling? '))
            if diameter > 0:
                valid = True
                return math.pi * diameter
            else:
                print('Value need to be a positive number. Check them again.')
        except ValueError:
            print('You need to use numbers.')

def lshape():
    print('To check the area of L-shape you will need to divide it in to two smaller rectangulars')
    valid = False
    while valid == False:
        try:
            bigger_length = int(input('What is the lenght of bigger rectangular? '))
            bigger_width = int(input('What is the width of bigger rectangular? '))
            smaller_length = int(input('What is the length of smaller rectangular? '))
            smaller_width = int(input('What is the width of smaller rectangular? '))
            if bigger_length > 0 and bigger_width > 0 and smaller_length > 0 and smaller_width > 0:
                valid = True
                return (bigger_width * bigger_length) + (smaller_length * smaller_width)
            else:
                print('Values need to be a positive number. Check them again.')
        except ValueError:
            print('You need to use numbers.')

def paint_amount(area) -> int:
    return math.ceil(area / 350)

def run_calculator():
    print('All values need to be in feet.')
    choice = ceiling_type()
    if choice == 'rectangular':
        area = rectangular()
        paint = paint_amount(area)
        print(f'You will need to buy {paint} gallons of paint to cover {area} square feet.')
    elif choice == 'round':
        area = round()
        paint = paint_amount(area)
        print(f'You will need to buy {paint} gallons of paint to cover {area} square feet.')
    elif choice == 'lshape':
        area = lshape()
        paint = paint_amount(area)
        print(f'You will need to buy {paint} gallons of paint to cover {area} square feet.')

if __name__ == '__main__':
    run_calculator()
