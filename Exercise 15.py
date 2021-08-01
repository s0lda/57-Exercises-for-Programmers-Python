import stdiomask
import bcrypt


users = {
    'User 1': b'pass1',
    'User 2': b'pass2',
    'User 3': b'pass3'}


for user, password in users.items():
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    new = {user: hashed}
    users.update(new)
    read = bcrypt.checkpw(password, hashed)


def user_input() -> str:
    valid = False
    while valid == False:
        try:
            word = input('>> ')
            if len(word) == 0:
                print('Can\'t be empty.')
            else:
                return word
        finally:
            pass


def check_user_login(user_login) -> bool:
    user_list = []
    for user, password in users.items():
        user_list.append(user)
    
        if user_login in user_list:
            return True
        else:
            pass


def login():
    valid_login = False
    while valid_login == False:
        try:
            print('LOGIN:')
            login = user_input()
            if check_user_login(login) == True:
                valid_login = True
            else:
                print('Wrong login.')
        finally:
            pass
    
    valid_password = False
    while valid_password == False:
        try:
            print('PASSWORD:')
            user_pass = stdiomask.getpass(prompt='>> ', mask= '*')
            user_pass = user_pass.encode()
            for user, password in users.items():
                if user == login:
                    if bcrypt.checkpw(user_pass, password):
                        valid_password = True
                        print('Welcome!')
                    else:
                        print('Wrong password.')
        finally:
            pass


if __name__ == '__main__':
    login()
