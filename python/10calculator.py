# calculator
from replit import clear

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():

    num1 = float(input("Enter the number : "))
    for symbol in operations:
        print(symbol)


    should_continue = True
    while should_continue:

        operation_symbol = input("Enter the operation symbol : ")
        num2 = float(input("Enter the number : ")) 
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2) 
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calulating with {answer} or type 'n' to start a new calculation...") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()



calculator()

