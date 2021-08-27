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


def check_search(list_of_emps, search: str):
    for emp in list_of_emps:
        if search in emp.first or search in emp.last or search in emp.position or search in emp.separation:
            return True
    return False


def search_for(list_of_emps, search: str):
    for emp in list_of_emps:
        # search must be case sensitive
        if search in emp.first or search in emp.last or search in emp.position or search in emp.separation:
            fullname = emp.fullname().ljust(25, ' ')
            position = emp.position.ljust(20, ' ')
            separation = emp.separation.ljust(20, ' ')
            print(f'{fullname}{position}{separation}')
    

def search_engine():
    print('What are we looking for?\nTo exit type exit.')
    valid = False
    while valid == False:
        try:
            search = input('>> ')
            if search.lower() == 'exit':
                valid = True
            else:
                if check_search(employees, search) == True:
                    print('\nNAME                     POSITION            SEPARATION\n')
                    search_for(employees, search)
                else:
                    print('No match.')
        finally:
            pass

if __name__ == '__main__':
    search_engine()
