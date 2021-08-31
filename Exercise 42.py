def read_data(file):
    data = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            x = line.replace('\n', '')
            data.append(x)
    return data


def clean_data(data):
    cleaned_data = []
    for item in data:
        x = item.split(',')
        cleaned_data.append(x)
    return cleaned_data


#salary from highest to lowest
def sort_by_income(data):
    sorted_list = []
    income = []
    for item in data:
        income.append(item[2])
    income = sorted(income)
    for i in income:
        for item in data:
            if i == item[2]:
                sorted_list.append(item)
    return sorted_list[::-1]


def output():
    out = sort_by_income(clean_data(read_data('ex42.csv')))
    print('Last        First       Salary\n')
    for item in out:
        first = item[0].ljust(12)
        last = item[1].ljust(12)
        salary = item[2]
        print(f'{first}{last}{salary}')

if __name__ == '__main__':
    output()
