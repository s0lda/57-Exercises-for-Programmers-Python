def name_counter():
    valid = False
    while valid == False:
        try:
            name = str(input('What is your name? '))
            count = len(name.replace(' ', ''))
            if count > 0:
                valid == True
                print(f'{name} has {count} letters.')
                break
            else:
                print('There is no letters in your name. Please enter valid name.')
        finally:
                pass


if __name__ == '__main__':
    name_counter()
