import json

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


def check_stock(item):
    with open(r'filedirectory\ex44.json', 'r') as data:
        data = json.load(data)
        for items in data['products']:
            for key, value in items.items():
                if key == 'name' and value == item:
                    return items
        return False


def add_item():
    new_name = input('What is the name of new product? ')
    new_price = float(input('What is the price of new product? '))
    new_quantity = int(input('What is the quantity of new product? '))
    return {"name": new_name, "price": new_price, "quantity": new_quantity}


def write_json(new_data, filename= r'filedirectory\ex44.json'):
    with open(filename, 'r+') as data:
        file_data = json.load(data)
        file_data['products'].append(new_data)
        data.seek(0)
        json.dump(file_data, data, indent= 4)


def stock_manager():
    price = 0
    quantity = 0

    valid = False
    while valid == False:
        try:
            print('What is the product name?')
            product = user_input()
            check = check_stock(product)
            if check == False:
                print('Sorry, product was not found in our inventory.')
                choice_valid = False
                while choice_valid == False:
                    try:
                        print('Do you want to add item to the inventory?')
                        choice = user_input()
                        if choice.lower() == 'yes' or choice.lower() == 'y':
                            new_item = add_item()
                            write_json(new_item)
                            choice_valid = True 
                        elif choice.lower() == 'no' or choice.lower() == 'n':
                            choice_valid = True
                        else:
                            print('You need to choose yes or no.')
                    finally:
                        pass
            else:
                price = check.get('price')
                quantity = check.get('quantity')     
                valid = True
        finally:
            pass
    
    print(f'NAME: {product}\nPRICE: {price}\nQUANTITY: {quantity}')

if __name__ == '__main__':
    stock_manager()
