def room_lenght():
    valid = False
    while valid == False:
        try:
            lenght = int(input('>> '))
            if lenght > 0:
                valid = True
                break
            else:
                print('It need to be more than 0.')
        except ValueError:
            print('It need to be a number.')
    return lenght

def rectangular_room():
    print('What is the lenght of the room?')
    lenght = room_lenght()
    print('What is the widht of the room?')
    widht = room_lenght()
    return lenght * widht

def converter_feet_meter(x):
    return x * 0.09290304

def converter_meter_feet(x):
    return x / 0.09290304

def run_converter():
    valid = False
    while valid == False:
        try:
            choice = str(input('Do you want to convert to meters or feet? '))
            if choice.lower() == 'meters':
                print('Please provide dimensions in feet.')
                x = rectangular_room()
                z = converter_feet_meter(x)
                print(f'The area is {x} feet or {z} meters.')
                valid = True
                break
            elif choice.lower() == 'feet':
                print('Please provide dimensions in meters.')
                x = rectangular_room()
                z = converter_meter_feet(x)
                print(f'The area is {x} meters or {z} feet.')
                valid = True
                break
            else:
                print("Please choose right option")
        except TypeError:
            print('Please choose right option')

if __name__ == '__main__':
    run_converter()