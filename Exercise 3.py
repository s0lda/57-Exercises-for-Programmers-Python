def quotes():
    quote = str(input('What is the quote? '))
    author = str(input('Who is the author? '))
    print(author + ' says: ' + quote)   # concentation was required for this exercise


if __name__ == '__main__':
    quotes()
