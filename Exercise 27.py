from typing import final


def user_input() -> str:
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) != 0:
                valid = True
                return usr_input
            else:
                print('Invalid input.')
        finally:
            pass


def first_name():
    valid = False
    while valid == False:
        try:
            name = user_input()
            if len(name) != 0:
                if len(name) >= 2:
                    valid = True
                    return name
                else:
                    print(f'{name} is invalid first name. It is too short.')
            else:
                print('First name need to be filled in.')
        finally:
            pass


def last_name():
    valid = False
    while valid == False:
        try:
            name = user_input()
            if len(name) != 0:
                if len(name) >= 2:
                    valid = True
                    return name
                else:
                    print(f'{name} is invalid last name. It is too short.')
            else:
                print('Last name need to be filled in.')
        finally:
            pass


def zip_code():
    valid = False
    while valid == False:
        try:
            zipcode = user_input()
            if len(zipcode) != 0:
                if zipcode.isdigit():
                    valid = True
                    return zipcode
                else:
                    print('ZIP code must be numeric.')
            else:
                print('ZIP code must be filled in.')
        finally:
            pass


def employee_id():
    valid = False
    while valid == False:
        try:
            emp_id = user_input()
            if len(emp_id) != 0:
                if len(emp_id) == 7:
                    if emp_id[:1].isalpha() and emp_id[2] == '-' and emp_id[3:].isdigit():
                        valid = True
                        return emp_id
                    else:
                        print(f'{emp_id} is not a valid ID.')
                else:
                    print(f'{emp_id} is not correct format.')
            else:
                print('Employee ID must be filled in.')
        finally:
            pass

    
def validate_input():
    print('Enter first name:')
    first = first_name()
    print('Enter last name:')
    last = last_name()
    print('Enter the ZIP code:')
    zipcode = zip_code()
    print('Enter employee ID:')
    emp_id = employee_id()

    print(f'\n{first.capitalize()} {last.capitalize()}\nZIP CODE: {zipcode}\nEmployee ID: {emp_id}\nThere were no errors found.')


if __name__ == '__main__':
    validate_input()
