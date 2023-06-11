#Advanced Version of EC2 Generator
x= int(input('How many EC2 Instances would you like? '))
dept= input('What department do you work for? ')
if dept == 'Marketing' or dept == 'Accounting' or dept == 'FinOps':
    print('Your randomized Instance Names: ')
    import random
    list1=['a', 'x', 'y', 'r', 'e', 'b', 'k', 'h']
    a=random.randint(0,7)
    b=random.randint(0,7)
    for z in range(x):
        print(random.randrange(1,100), dept + list1[a] + list1[b], random.randrange(1,100), sep='_')
else:
    print('Sorry you cannot use this Generator')