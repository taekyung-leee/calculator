# Create a simple calculator tool that asks a user to enter two numbers and the operation.
# Display the answer to the equation. Every equation entered by the user is written to a text file. 
# Use defensive programming to write the program that is robust and handles unexpected events and user inputs.

while True:
    option = input("Enter '1' to perform a calculation, '2' to read equations from a file, and '3' to exit:")

    if option == '1':
        # existing code for performing calculations goes here
        with open("sample.txt", "a+") as f:
            while True:
                operator = input("Enter an operator (+,-,*,/)")
        
                if operator in ["+", "-", "*", "/"]:
                    try:
                        num1 = float(input("Enter the first number:"))
                        num2 = float(input("Enter the second number:"))
        
                    except ValueError:
                        print("Invalid input. Please enter a number")
                        continue

                    if operator == "+":
                        print("{} + {} = {}".format(num1,num2,num1+num2))
            
                    elif operator == "-":
                        print("{} - {} = {}".format(num1,num2,num1-num2))
            
                    elif operator == "*":
                        print("{} * {} = {}".format(num1,num2,num1*num2))
            
                    elif operator == "/":
                        try:
                            print("{} % {} = {}".format(num1,num2,num1/num2))
                
                        except ZeroDivisionError:
                            print("You divided by 0. please enter a different number.")
                            continue
                    else: 
                        print("Invalid operator. Please enter again")
                        continue
        
                    continue_calculation = input("Do you want to continue the calculation?: (y/n)")
                    if continue_calculation.lower() == "n":
                        print("End of the calculation.")
                        break
            continue
                            
        
    elif option == '2':
        # ask user for filename
        filename = input("Enter the filename to read equations from (ex. calculator.txt) ")
        
        # use defensive coding to ensure the file exists        
        try:
            with open(filename, "r") as f:
                # read all lines from file and loop through them
                equations = f.readlines()
                for equation in equations:
                    # split equation into parts and perform calculation
                    parts = equation.split()
                    num1 = float(parts[0])
                    num2 = float(parts[2])
                    operator = parts[1]
                        
                    if operator == "+":
                        result = num1 + num2
                    elif operator == "-":
                        result = num1 - num2
                    elif operator == "*":
                        result = num1 * num2
                    elif operator == "/":
                        try:
                            result = num1 / num2
                        except ZeroDivisionError:
                            print("You divided by 0. Please enter a different number.")
                            continue
                            
                    # print equation and result
                    print(f"result: {equation.strip()} = {result}")
                    break
                        

        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")
            
    elif option == "3":
        print("Ending the programme. Thank you.")
        break    
           
    else:
        print("Invalid option. Please enter '1', '2', or '3'.")
        continue
