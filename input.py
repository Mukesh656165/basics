#how to take multiple input in
a,b = input('Enter two values :').split()
print(a)
print(b)
print(type(a))
print(type(b))
print(hex(id(a)))
print(hex(id(b)))

# This way we can store only strings

# threee input at a time
a,b,c = input('Enter 3 values :').split(',')
print(a)
print(b)
print(c)
a, b = input('Enter two values :').split()
print(f'first input{a} and second{b}')

# Using List object in input
x = list(map(int, input("Enter a multiple value: ").split(',')))

print(f'U entered {x}')

# Using List comprehension to Create
a,b = [int(x) for x in input('enter two values:').split(',')]
print(a)
print(b)
print(type(a))
print(type(b))

# This way we can store str and int also
# To store strings in this way
a,b = [str(x) for x in input('enter two values:').split(',')]
print(a)
print(b)
print(type(a))
print(type(b))

# input Three values at a time
a,b,c = [int(x) for x in input('Enter Three values:').split(',')]
print(a,b,c)
print(type(a))

# Taking multiple values at a time

x = [int(x) for x in input('Enter multiple values:').split(',')]
print(x)
print(type(x))
