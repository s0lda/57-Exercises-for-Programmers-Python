# in this version program will read from file, remove employees but won't write to file (so there is always something there to work with)
with open('ex34.txt', 'r+') as emp_list:
    file_contents = emp_list.readlines()
    
    def emp_removal():
        valid = False
        while valid == False:
            try:
                emp = input('Enter an employee name to remove: ')
                if len(emp) > 0:
                    valid = True
                    return emp
                else:
                    print('Try again.')
            finally:
                pass
    
    
    def check_if_emp_exists(name: str) -> bool:
        for item in file_contents:
            if item.strip('\n') == name:
                return True
        return False

    
    def remove_emp(name):
        for line in file_contents:
            x = f'{name}\n'
            name_index = file_contents.index(x)
            del file_contents[name_index]
            return file_contents


    def main_program():
        print(f'Number of employees: {len(file_contents)}')
        for item in file_contents:
            print(item.strip('\n'))
        
        valid = False
        while valid == False:
            try:
                emp_to_remove = emp_removal()
                if check_if_emp_exists(emp_to_remove) == True:
                    remove_emp(emp_to_remove)
                    print(f'\nNumber of employees: {len(file_contents)}')
                    for item in file_contents:
                        print(item.strip('\n'))
                    valid = True
                else:
                    print('Employee not on your list.')
            finally:
                pass


if __name__ == '__main__':
    main_program()
