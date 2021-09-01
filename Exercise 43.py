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
                print('Can\'t be empty.')
        finally:
            pass


def find_desktop_dir():
    return os.path.expanduser('~\\Desktop')


def create_folder(directory, folder_name):
    folder_name = f'\\{folder_name}'
    path = directory + folder_name
    return os.mkdir(path)


def create_web_files():
    print('Site name: ')
    site_name = user_input()
    
    main_folder = create_folder(find_desktop_dir(), site_name)
    main_dir = f'{find_desktop_dir()}\\{site_name}'
    
    print('Author: ')
    author = user_input()
    
    index_file = f'{main_dir}\\index.html'
    
    with open(index_file, 'w+') as index:
        index.write(f'<title>{site_name}</title>\n  <meta>{author}</meta>')

    print('Main files have been created on your desktop.')
    
    print('Do you want a folder for JavaScript?')
    java_valid = False
    while java_valid == False:
        try:
            java_s = user_input()
            if java_s.lower() == 'yes' or java_s.lower() == 'y':
                create_folder(main_dir, 'java script')
                print('Java Script folder have been created.')
                java_valid = True
            elif java_s.lower() == 'no' or java_s.lower() == 'n':
                java_valid = True
            else:
                print('Choose yes or no.')
        finally:
            pass

    print('Do you want a folder for CSS?')
    css_valid = False
    while css_valid == False:
        try:
            css = user_input()
            if css.lower() == 'yes' or css.lower() == 'y':
                create_folder(main_dir, 'css')
                print('CSS folder have been created.')
                css_valid = True
            elif css.lower() == 'no' or css.lower() == 'n':
                css_valid = True
            else:
                print('Choose yes or no.')
        finally:
            pass


if __name__ == '__main__':
    create_web_files()
