import os

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def subtraction(a, b):
    return a - b

operations_dict = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    continue_flag = True
    
    while continue_flag:
        num1 = int(input("Enter First Number: "))
        for symbol in operations_dict:
            print(symbol)
        
        should_continue = True
        while should_continue:
            op_symbol = input("Pick any one operation: ")
            num2 = int(input("Enter Second Number: "))
            calculator_function = operations_dict[op_symbol]
            output = calculator_function(num1, num2)
            print(f"{num1} {op_symbol} {num2} = {output}")
            
            should_continue = input(f"Enter 'y' to Continue Calculation with {output}\nEnter 'n' to start a New Calculation \nEnter 'x' to exit\nType your Choice: ").lower()
            if should_continue == 'y':
                num1 = output
            elif should_continue == 'n':
                should_continue = False
                os.system('cls')  # Clear the screen (for Windows)
            else:
                should_continue = False
                continue_flag = False
                print("BYE")

calculator()
