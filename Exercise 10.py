def scan_item():
    valid = False
    while valid == False:
        try:
            price = int(input('Please enter the price of the item: '))
            quantity = int(input('Please enter quantity: '))
            if price > 0 and quantity > 0:
                valid = True
                return price * quantity
            else:
                print('You need to input positive numbers.')
        except ValueError:
            print('You need to input numbers.')

def shopping_basket():
    basket = 0
    valid = False
    while valid == False:
        try:
            print('Add item or exit?')
            choice = input('>> ')
            if choice.lower() == 'exit':
                valid = True
            elif choice.lower() == 'add':
                item = scan_item()
                basket += item
            else:
                print('You need to choose add or exit')
        except TypeError:
            print('You need to choose the right option')
    return(basket)

#tax for exercise 5.5%
def tax(amount):
    return (amount / 100) * 5.5

def run_till():
    amount = shopping_basket()
    tax_to_pay = tax(amount)
    print(f'''
    Subtotal: ${amount}
    Tax: ${tax_to_pay}
    Total: ${amount + tax_to_pay}''')

if __name__ == '__main__':
    run_till()
