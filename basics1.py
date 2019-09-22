# how to print to print statement in one single line

print('why so serious',end=' ')
print('Joker')

# Desicion making
i = 10
if i >5:
    print('i is greater')
else:
    print('i is small')

name = 'Joker'
if name == 'Joker':
    print('why so serious')
elif name == 'robert':
    print('hello robert')
elif name == 'jason':
    print('jason bourne')
else:
    print('Hero')

names = {'Joker':'why so serious','Bond':'OO7'}
print(names.get('Joker','idont know'))
print(names.get('jason','Idontknow'))

# checking with elif
var = 10
if 'J ' in 'Joker':
    print('a in joker')
elif 'b' in 'bond':
    print( 'Bond')
elif var:
    print('var')