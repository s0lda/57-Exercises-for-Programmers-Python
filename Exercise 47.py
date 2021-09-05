import requests, json

def who_is_in_space(url):
    response = requests.get(url)
    data = response.json()

    number_of_astros = data['number']
    print(f'Number of people in space right now: {number_of_astros}.\n')

    print('NAME'.ljust(20) + 'CRAFT\n')
    for item in data['people']:
        for name in item['name'].split('  '):
            for craft in item['craft'].split():
                name = name.ljust(20)
                print(f'{name}{craft}')


if __name__ == "__main__":
    who_is_in_space('http://api.open-notify.org/astros.json')
