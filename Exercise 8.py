import math

def check_people():
    valid = False
    while valid == False:
        try:
            people = int(input('How many people? '))
            if people > 0:
                valid = True
                break
            else:
                print('There need to be at least 1 person.')
        except ValueError:
            print('Amount of people need to be a positive number')
    return people

def check_status():
    valid = False
    while valid == False:
        try:
            choice = input('Sharing pizza or ordering? ')
            if choice.lower() == 'sharing' or choice.lower() == 'share':
                valid = True
                return 'sharing'
            elif choice.lower() == 'ordering' or choice.lower() == 'order':
                valid = True
                return 'ordering'
            else:
                print('You need to choose: share or order.')
        except TypeError:
            print('You need to choose on of the options.')

def check_slices():
    valid = False
    while valid == False:
        try:
            pizzas = int(input('How many pizzas do you have? '))
            slices = int(input('How many slices on each pizza? '))
            if pizzas >= 0 and slices >= 0:
                valid = True
                return pizzas * slices
            else:
                print('Well... that\'s not possible.\nCheck your stock again.\n')
        except ValueError:
            print('It need to be a number')

def check_share():
    people = check_people()
    slices = check_slices()
    share = slices / people
    if share < 1:
        print('There is not enough to share with everyone')
    else:
        slices_share = slices // people
        leftovers = slices - (slices_share * people)
        slices_str = ''
        leftovers_str = ''
        if slices_share == 1:
            slices_str = 'slice'
        else:
            slices_str = 'slices'

        if leftovers == 1:
            leftovers_str = 'slice'
        else:
            leftovers_str = 'slices'
        print(f'Each person get\'s {slices_share} {slices_str}. There is {leftovers} leftover {leftovers_str}.')

def order_pizzas():
    x = check_people()
    valid = False
    while valid == False:
        try:
            pizza_slice = int(input('How many slices each person want\'s? '))
            slices = int(input('How many slices on each pizza? '))
            if slices > 0:
                order = math.ceil((pizza_slice * x) / slices)
                leftovers = (order * slices) - (pizza_slice * x)
                pizza_str = ''
                slice_str = ''
                if order == 1:
                    pizza_str = 'pizza'
                else:
                    pizza_str = 'pizzas'

                if leftovers == 1:
                    slice_str = 'slice'
                else:
                    slice_str = 'slices'

                print(f'You need {order} {pizza_str}. You will have {leftovers} leftover {slice_str}.')
                valid = True
            else:
                print('There need to be at least 1 slice')
        except ValueError:
            print('It need to be a number.')

if __name__ == '__main__':
    check = check_status()
    if check == 'sharing':
        check_share()
    else:
        order_pizzas()