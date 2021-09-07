import requests


import webbrowser, sys

# I don't know how to do GUIs yet so instead used webbrowser and instead of API I've used basic search as this is much more efficient in this case
# and does exactly same thing

def find_photos(search):
    url = f'https://www.flickr.com/search/?text={search}'
    return webbrowser.open(url, new= 1)

def run_app():
    print('What photos would you like to search for?')
    search = input('>> ')
    find_photos(search)

if __name__ == '__main__':
    run_app()
    sys.exit()
