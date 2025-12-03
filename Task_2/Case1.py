def main():
    import os
    os.system('cls')
    # 1. ADD | Add two numbers
    # 2. SUBTRACT | Subtract two numbers
    # 3. DIVIDE | Divide two numbers
    # 4. MULTPLY | Multiply two numbers

    print('-----------------------')
    print('  Mathlete Calculator  ')
    print('-----------------------')
    print('1. ADD')
    print('2. SUBTRACT')
    print('3. DIVIDE')
    print('4. MULTIPLY')
    print()

    operation = input('Enter 1, 2, 3 or 4 to choose operation and press Enter: ')

    if operation == '1':
        try:
            num1 = input('Enter first number: ') 
            num2 = input('Enter second number: ')
            result = float(num1) + float(num2)
            print()
            print('Result:', str(num1), '+', str(num2), '=', result)
            print()
        except ValueError:
            print()
            print('You have entered a invalid entry please restart the programme.')
            print()
        restart = input('Do you want to start over? Yes/No: ').lower()
        if restart == 'yes':
            main()
        else:
            print()
            input('Thank you! Goodbye :) Press enter to exit')  
            
    elif operation == '2':
        try:
            num1 = input('Enter first number: ')
            num2 = input('Enter second number: ')
            result = float(num1) - float(num2)
            print()
            print('Result:', str(num1), '-', str(num2), '=', result)
            print()
        except ValueError:
            print()
            print('You have entered a invalid entry please restart the programme.')
            print()
        restart = input('Do you want to start over? Yes/No: ').lower()
        if restart == 'yes':
            main()
        else:
            print()
            input('Thank you! Goodbye :) Press enter to exit')   
    elif operation == '3':
        try:
            num1 = input('Enter first number: ')
            num2 = input('Enter second number: ')
            result = float(num1) / float(num2)
            print()
            print('Result:', str(num1), '/', str(num2), '=', result)
            print()
        except ZeroDivisionError:
            print()
            print('Result = Infinte')
            print()           
        except ValueError:
            print()
            print('You have entered a invalid entry please restart the programme.')
            print()
        restart = input('Do you want to start over? Yes/No: ').lower()
        if restart == 'yes':
            main()        
        else:
            print()
            input('Thank you! Goodbye :) Press enter to exit')   
    elif operation == '4':
        try:
            num1 = input('Enter first number: ')
            num2 = input('Enter second number: ')
            result = float(num1) * float(num2)
            print()
            print('Result:', str(num1), '*', str(num2), '=', result)
            print()
        except ValueError:
            print()
            print('You have entered a invalid entry please restart the programme.')
            print()
        restart = input('Do you want to start over? Yes/No: ').lower()
        if restart == 'yes':
                main()    
        else:
            print()
            input('Thank you! Goodbye :) Press enter to exit')   
    else:
        print()
        print('You have entered a invalid entry please restart the programme.')
        print()
        restart = input('Do you want to start over? Yes/No: ').lower()
        if restart == 'yes':
            main()
        else:
            input('Thank you! Goodbye :) Press enter to exit') 
main()  
