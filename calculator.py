print('1. addition');
print('2. subtraction');
print('3. multiplication');
print('4. division');
print('5. exit')
choice = int(input('Enter your choice :'))
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
if choice == 1:

    res = num1 + num2
    print("Result = ", res)
elif choice == 2:

    res = num1 - num2
    print("Result = ", res)
elif choice == 3:

    res = num1 * num2
    print("Result = ", res)
elif choice ==4:

    res = num1 / num2;
    print("Result = ", res)
elif choice == 5:
           exit();
else:
    print("Wrong input..!!");