def float_input() -> float:
    valid = False
    while valid == False:
        try:
            number = float(input('>> '))
            if number > 0:
                valid = True
                return number
            else:
                print('Need to be a positive number.')
        except ValueError:
            print('You need to input a number.')


def string_input() -> str:
    valid = False
    while valid == False:
        try:
            word = input('>> ')
            if ' ' in word:
                for char in word:
                    if char.isdigit():
                        valid = False
                        print('No numbers please.')
                    elif char.isalpha() or char.isspace():
                        valid = True
                        return word
            elif not word.isalpha():
                print('Wrong input.')
            else:
                valid = True
                return word
        finally:
            pass


Polish = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Pażdziernik', 'Listopad', 'Grudzień']
English = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def language_choice():
    list_of_languages = ['Polish', 'English']
    list_string = ', '.join(str(i) for i in list_of_languages)
    print(f'What language would you like to use?\nLanguages available {list_string}.')
    
    valid = False
    while valid == False:
        try:
            choice = string_input()
            if choice.capitalize() in list_of_languages:
                valid = True
                return choice.capitalize()
            else:
                print('You can only choose from the list.')
        finally:
            pass


def month_pick():
    print('What month would you like to translate?\nEnter number of the month.')
    valid = False
    while valid == False:
        try:    
            choice = float_input()
            if choice >= 1 and choice <= 12:
                valid = True
                return int(choice)
            else:
                print('You can only choose between 1 and 12.')
        finally:
            pass


def result_month(language, number):
    return language[number - 1]


def run_translator():
    language_user_choice = language_choice()
    if language_user_choice == 'Polish':
        language = Polish
    elif language_user_choice == 'English':
        language = English
    else:
        pass #awaiting for more languages to add

    month = month_pick()
    result = result_month(language, month)
    print(f'Month number {month} in {language_user_choice} is {result}.')


if __name__ == '__main__':
    run_translator()
