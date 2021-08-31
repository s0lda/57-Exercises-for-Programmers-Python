def user_input():
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) > 0:
                valid = True
                return usr_input
            else:
                print('Can\'t be empty')
        finally:
            pass


def last_first(name: str):
    names = name.split()
    if len(names) == 2:
        first = names[0]
        last = names[1]
        return f'{last}, {first}'
    elif len(names) == 1:
        return names
    else:
        return name


def sort_names(names_list):
    return sorted(names_list)

def run_list_of_names():
    print('Please input names to sort. Type exit to finish.')
    list_of_names = []

    valid = False
    while valid == False:
        try:
            name = user_input()
            if name.lower() == 'exit':
                valid = True
            else:
                list_of_names.append(last_first(name))
        finally:
            pass

    sorting_names = sort_names(list_of_names)
    number_of_names = len(list_of_names)

    with open(r'file_directory\ex41.txt', 'w') as outfile:
        outfile.write(f'Total names: {number_of_names}.\n')
        for name in sorting_names:
            outfile.write('%s\n' % name)

    print(list_of_names)

if __name__ == '__main__':
    run_list_of_names()
