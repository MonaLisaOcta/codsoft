print("WELCOME TO MY CALCULATOR")

choice = input('''Please select the type of opreations you want to perform:
               + for addittion
               - for subtraction
               * for multiplication
               / for division''')
               
               
              
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if(choice == '+'):
    print('{} + {} = '.format(num1,num2))
    print(num1 + num2)
elif(choice == '-'):
    print('{} - {} ='.format(num1,num2))
    print(num1 - num2)
elif(choice == '*'):
    print('{} * {} ='.format(num1,num2))
    print(num1*num2)
elif(choice == '/'):
    print('{} / {}='.format(num1,num2))
    print(num1/num2)
else:
    print("Incorrect Choice")

    
    
    