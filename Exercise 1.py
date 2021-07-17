import random
import typing_extensions

def greeting():
    name = input('What is your name? ')
    if name.lower() == 'test':
        choices = [f'Hi {name}.', f'Hello {name}.', f'Good morning {name}.']
        print(random.choice(choices))
    else:
        print(f'Hi {name}, Goodbye {name}')



if __name__ == '__main__':
    greeting()
