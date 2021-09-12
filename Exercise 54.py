import random, webbrowser

database = [['https://docs.python.org/', 'http://short.url/12345', 0]]


def shorten_url(url):
    global database
    for lst in database:
        for info in lst:
            if lst[0] == url:
                return lst[1]
            else:
                short_valid = False
                while short_valid == False:
                    try:
                        short = random.randint(10000, 99999)
                        short = f'http://short.url/{str(short)}'
                        for lst in database:
                            if lst[1] != short:
                                new_web = [url, short, 0]
                                database.append(new_web)
                                short_valid = True
                                print(f'This is your short url: {short}.')           
                    finally:
                        pass


def check_url(short_url):
    for lst in database:
        if lst[1] == short_url:
            # entry counter for short url.
            lst[2] += 1
            return lst[0]
        return False


def main():
    print('Please eneter your website:')
    website = input('>> ')
    if check_url(website) == False:
        shorten_url(website)
    else:
        webbrowser.open(check_url(website))

main()
