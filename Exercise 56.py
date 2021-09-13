import json


def int_input():
    valid = False
    while valid == False:
        try:
            num = input('>> ')
            if num.isdigit():
                valid = True
                return num
            else:
                print('Need to use numbers only.')
        finally:
            pass

    
def read_stock(file):
    print('NAME'.ljust(15) + 'SERIAL NO.'.ljust(25) + 'VALUE'.ljust(15))
    with open(file) as json_file:
        data = json.load(json_file)
        for item in data["stock"]:
            name = item["name"].ljust(15)
            serial = item["serial"].ljust(25)
            value = item["price"].ljust(15)
            print(f'{name}{serial}${value}')
        

def add_item():
    new_name = input('What is the name of new product?\n>> ')
    print('What is the price of new product? ')
    new_price = int_input()
    serial = input('What is the serial number of new product?\n>> ')
    return {"name": new_name, "price": new_price, "serial": serial}


def write_json(file, new_data):
    with open(file, 'r+') as data:
        file_data = json.load(data)
        file_data['stock'].append(new_data)
        data.seek(0)
        json.dump(file_data, data, indent= 4)


def main():
    valid = False
    while valid == False:
        try:
            print('Do you want to ADD or READ your inventory?')
            choice = input('>> ')
            if choice.lower() == 'exit':
                valid = True
            elif choice.lower() == 'add':
                write_json('ex56.json', add_item())
            elif choice.lower() == 'read':
                read_stock('ex56.json')
            else:
                print('You didn\'t choose right option.')
        finally:
            pass

main()
