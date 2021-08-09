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

def isAnagram(first, second):
    return sorted(first) == sorted(second)

def check_words():
    print('What is the first word?')
    first = string_input()
    print('What is the second word?')
    second = string_input()
    result = isAnagram(first, second)
    if result == True:
        print(f'{first} and {second} are anagrams.')
    else:
        print(f'{first} and {second} are not anagrams.')

if __name__ == '__main__':
    check_words()
