from datetime import datetime

driving_age = {
    'Poland' : 18,
    'Germany': 17,
    'Isle of Man': 16,
    'Denmark': 17,
    'Estonia': 16,
    'Latvia': 16,
    'United Kingdom': 17
}


def check_age(date_of_birth):
    today = datetime.now()
    today = today.date()

    dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    dob = dob.date()
    if (today.year - dob.year) > 0:
        if today.month < dob.month:
            return (today.year - dob.year) - 1
        elif today.month == dob.month:
            if today.day < dob.day:
                return (today.year - dob.year) - 1
            else:
                return (today.year - dob.year)
        else:
            return (today.year - dob.year)
    else:
        return (today.year - dob.year)


def check_countries(user_age):
    allowed = []
    for country, age in driving_age.items():
        if user_age >= age:
            allowed.append(country)
    return allowed


def run_checker():
    date_of_birth = input('What is your date of birth? YYYY-MM-DD ')
    can_drive = check_countries(check_age(date_of_birth))
    x = ", ".join(map(str, can_drive))
    if len(can_drive) > 0:
        print(f'You are allowed to drive in:\n{x}')
    else:
        print('You are not allowed to drive.')

if __name__ == '__main__':
    run_checker()
