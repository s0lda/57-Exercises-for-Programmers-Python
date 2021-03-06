class Employee():
    def __init__(self, first: str, last: str, position: str, separation: str) -> None:
        self.first = first
        self.last = last
        self.position = position
        self.separation = separation

    def fullname(self):
        return f'{self.first} {self.last}'


emp1 = Employee('Jake', 'Jacobson', 'Programmer', 'n/a')
emp2 = Employee('John', 'Johnson', 'Manager', '2016-12-31')
emp3 = Employee('Michaela', 'Michaelson', 'District Manager', '2015-12-18')
emp4 = Employee('Tou', 'Xiong', 'Software Engineer', '2017-10-05')
emp5 = Employee('Jacquelyn', 'Jackson', 'DBA', 'n/a')
emp6 = Employee('Sally', 'Webber', 'Web Developer', '2015-12-18')

employees = [emp1, emp2, emp3, emp4, emp5, emp6]


def sort_by_name(list_of_emps):
    print('\nNAME                     POSITION            SEPARATION\n')
    sorted_emps = []
    for emp in list_of_emps:
        full = emp.fullname()
        sorted_emps.append(full)
    sorted_emps = sorted(sorted_emps)
    for name in sorted_emps:
        for emp in list_of_emps:
            if name == emp.fullname():
                fullname = emp.fullname().ljust(25, ' ')
                position = emp.position.ljust(20, ' ')
                separation = emp.separation.ljust(20, ' ')
                print(f'{fullname}{position}{separation}')


def sort_by_position(list_of_emps):
    print('\nNAME                     POSITION            SEPARATION\n')
    sorted_emps = []
    for emp in list_of_emps:
        position = emp.position
        sorted_emps.append(position)
    sorted_emps = sorted(sorted_emps)
    for position in sorted_emps:
        for emp in list_of_emps:
            if position == emp.position:
                fullname = emp.fullname().ljust(25, ' ')
                position = emp.position.ljust(20, ' ')
                separation = emp.separation.ljust(20, ' ')
                print(f'{fullname}{position}{separation}')


def sort_by_separation(list_of_emps):
    print('\nNAME                     POSITION            SEPARATION\n')
    sorted_emps = []
    for emp in list_of_emps:
        separation = emp.separation
        if separation not in sorted_emps:
            sorted_emps.append(separation)
    sorted_emps = sorted(sorted_emps)
    for sep in sorted_emps:
        for emp in list_of_emps:
            if sep == emp.separation:
                fullname = emp.fullname().ljust(25, ' ')
                position = emp.position.ljust(20, ' ')
                separation = emp.separation.ljust(20, ' ')
                print(f'{fullname}{position}{separation}')


def run_the_program():
    print('Do you want to sort by (N)ame, (P)osition or (S)eparation? Type exit to exit.')
    valid = False
    while valid == False:
        try:
            choice = input('>> ')
            if choice.lower() == 'n':
                sort_by_name(employees)
            elif choice.lower() == 'p':
                sort_by_position(employees)
            elif choice.lower() == 's':
                sort_by_separation(employees)
            elif choice.lower() == 'exit':
                valid = True
            else:
                print('Choose one of the options.')
        finally:
            pass


if __name__ == '__main__':
    run_the_program()
