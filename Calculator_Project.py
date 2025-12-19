import art

def add(n1, n2):
    return n1 + n2

#Substract, multiply and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Adding this 4 functions as values in the dictionary with keys as "+","-","*","/"

operations={"+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
            }
#Main Program


# first_num=float(input("What's the first number?:"))
# user_op=input("Pick an operation").lower()
# second_num=float(input("What's the next number?:"))

# result=operations[user_op](first_num, second_num)
# print(f"{first_num} + {second_num} = {result}")


def calculator():   # to handle no condition so that we can recursive function calling in case of No condition
    print(art.logo)
    first_num = float(input("What's the first number?:"))  # Imp to keep it outside of the while so that we dont override it again when we user choice y
    loop = True
    while loop:     # to handle yes condition

        for key in operations:
            print(key)
        user_op = input("Pick an operation").lower()
        second_num = float(input("What's the next number?:"))

        result = operations[user_op](first_num, second_num)
        print(f"{first_num} {user_op} {second_num} = {result}")

        user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if user_choice == 'y':
            first_num = result
        if user_choice == 'n':
            calculator()

calculator()

