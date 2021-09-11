import os

def user_input():
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) > 0:
                valid = True
                return usr_input
            else:
                return False
        finally:
            pass


def if_exists(listName):
    csv_file = f'{listName}.csv'
    file = os.path.isfile(csv_file)
    if file == True:
        print('Found it!')
    elif file == False:
        with open(f'{os.path.dirname(__file__)}\{csv_file}', 'w') as f:
            f.close()
            print('There was no such list, so we have created one for you.')


def read_list(listName):
    with open(f'{os.path.dirname(__file__)}\{listName}.csv', 'r') as f:
        lst = f.read()
        print(lst)


def write_to(listName, task):
    with open(f'{os.path.dirname(__file__)}\{listName}.csv', 'a') as f:
        task = f'{task}\n'
        f.writelines(task)


def remove_task(listName, task):
    check = 0
    with open(f'{os.path.dirname(__file__)}\{listName}.csv', 'r') as f:
        data = f.readlines()
        for line in data:
            if line.strip('\n') == task:
                check += 1

    with open(f'{os.path.dirname(__file__)}\{listName}.csv', 'w+') as f:
        line = f.readlines()
        for line in data:
            if line.strip('\n') != task:
                f.writelines(line)
    
    if check == 0:
        print('No task found.')
    elif check == 1:
        print('Task removed.')
    else:
        print('Tasks removed.')


# secret command to remove all tasks
def remove_all(listName):
    with open(f'{os.path.dirname(__file__)}\{listName}.csv', 'w') as f:
        f.close()


def main():
    print('COMMANDS: READ ADD REMOVE EXIT')
    print('Please select your TO DO list.')
    todo = user_input()
    # crate the list if does not exist already
    if_exists(todo)
    print('What do you want to do with your list?')
    valid_work = False
    while valid_work == False:
        try:
            action = user_input()
            if action.lower() == 'exit':
                valid_work = True
                print('Bye Bye.')
            elif action.lower() == 'read':
                print('TO DO:')
                read_list(todo)
            elif action.lower() == 'add':
                print('Add your TO DOs. Add empty to stop adding.')
                valid_add = False
                while valid_add == False:
                    try:
                        add = user_input()
                        if add == False:
                            valid_add = True
                        else:
                            write_to(todo, add)
                    finally:
                        pass
            elif action.lower() == 'remove':
                print('What task would you like to remove?')
                remove = user_input()
                remove_task(todo, remove)
            elif action.lower() == 'remove all':
                remove_all(todo)
                print('All TO DOs removed.')
            else:
                print('Need to choose one of the COMMANDS.')
        finally:
            pass

main()
