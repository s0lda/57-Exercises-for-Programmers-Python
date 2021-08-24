def list_input() -> str:
    valid = False
    while valid == False:
        try:
            l_input = input('>> ')   
            if len(l_input) > 0:
                valid = True
                return str(l_input)
            else:
                print('Can\'t be empty.')
        finally:
            pass


def check_if_only_digits(string: str) -> bool:
    check_str = string.replace(' ', '')
    if check_str.isdigit():
        return True
    return False


def convert_to_list(string: str) -> list:
    string = string.replace(' ','')
    return [int(i) for i in string]


def run_the_program():
    print('Please input digits separated with spaces.')

    even_numbers = []
    count = 0
    valid_input = False
    while valid_input == False:
        try:
            str_list = list_input()
            if check_if_only_digits(str_list) == True:
                int_list = convert_to_list(str_list)
                for i in int_list:
                    if i % 2 == 0:
                        even_numbers.append(i)
                valid_input = True
            else:
                print('Only digits separeted with spaces allowed.')
        finally:
            pass

    even_numbers = [str(i) for i in even_numbers]
    even_numbers = ', '.join(even_numbers)
    print(f'The even numbers are {even_numbers}.')


if __name__ == '__main__':
    run_the_program()
