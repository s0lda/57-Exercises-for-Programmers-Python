import math

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


def months_to_payoff(balance: float, payment: float, interest: float) -> int:
    interest = interest / 1200
    months = math.log(1 + (interest / ((payment / balance) - interest))) / math.log(1 + interest)
    return int(math.ceil(months))

def monthly_payment(principal: float, interest: float, months: float) -> float:
    rate = interest / 1200
    return round(principal * ((rate * ((1 + rate) ** months)) / (((1 + rate) ** months)- 1)), 2)

def run_calculator():
    print('Do you want to calculate fixed (RATE) or number of (PAYMENTS)?')
    choice = string_input()

    if choice.lower() == 'rate':
        print('What is the amount of your loan?')
        principal = float_input()
        print('What is your APR?')
        interest = float_input()
        print('How many months do you have to pay it off?')
        months = float_input()
        payment = monthly_payment(principal, interest, months)
        print(f'For {principal} loan with {interest}% APR and {months} months term your monthly payment will be {payment}.')
    elif choice.lower() == 'payments':
        print('What is your balance?')
        balance = float_input()
        print('What is your monthly payment?')
        payment = float_input()
        print('What is the APR?')
        interest = float_input()
        payments = months_to_payoff(balance, payment, interest)
        if payments == 1:
            print('You will need 1 month to pay it off.')
        else:
            print(f'You will need {payments} months to pay it off.')
    else:
        print('You have to choose rate or payments.')

if __name__ == '__main__':
    run_calculator()
