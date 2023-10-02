from replit import clear
import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}

def calculator():
    print (art.logo)
    num1 = float(input("What's your first number?: "))
    for sign in operations:
        print(sign)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's your next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {round(answer,1)}")
        to_continue = input(f"Type 'y' to continue calculating with {round(answer,1)}, or type 'n' to start a new calculation: ")
        num1 = answer
        if to_continue == 'y':
            clear()
            should_continue = True
        else:
            should_continue = False
            clear()
            calculator()

calculator()