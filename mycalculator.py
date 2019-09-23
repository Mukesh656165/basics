def add(x,y):
    return x+y

def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y

print('select operation')
print('1. add')
print('2. sub')
print('3. multiply')
print('1. devide')
choice = input('enter your choice 1/2/3/4:')
num1 = int(input('Enter your 1st number:'))
num2 = int(input('Enter your 2nd  number:'))

if choice == '1':
    print(add(num1,num2))
elif choice =='2':
    print(sub(num1,num2))
elif choice =='3':
    print(multi(num1,num2))
else:
    print(div(num1,num2))