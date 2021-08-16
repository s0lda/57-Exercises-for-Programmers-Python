def mult_table(num):
    X = 1
    Y = 1
    print ('{:>4}'.format(' '), end= ' ')
    for X in range(1, num + 1):
        print('{:>4}'.format(X), end=' ')
    
    print()
    
    for X in range(1, num + 1):
        print('{:>4}'.format(X), end=' ')
        while Y <= num:
            print('{:>4}'.format(X * Y), end=' ')
            Y+=1
        print()
        Y = 1

if __name__ == '__main__':
    mult_table(num)
