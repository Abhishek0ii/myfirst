def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def modulus(x,y):
    return x%y
def power(x,y):
    return x**y
def floor_division(x,y):
    return x//y

print("select an operation\n"
      "add \n"
      " # It can be used to add two values\n"
      "subtract\n "
      "# It can be used to subtract the second value from the first value.\n"
      "multiply\n"
      " # It can be used to find the product of 2 values\n"
      "divide\n"
      " # It can be used to find the quotient when first operand is divided by the second.\n"
      "modulus \n"
      " # It is used to find the remainder when first operand is divided by the second.\n"
      "power \n"
      " # It can be used to raise the first operand to power of second.\n"
      "floor_division \n"
      " # It can be used to conduct the floor division. It is used to find the floor of the quotient when first operand is divided by the second.\n"
      "history \n"
      " # It can be used to search the operatons used before\n "
      "end \n"
      " # It can be used to stop the program.")

history = []

while True:
    choice = input("enter the operation:\t")
    if choice in ('add','subtract','multiply','divide','modulus','power','floor_division'):
        num1 = float(input("enter the first num:\t"))
        num2 = float(input("enter the 2nd num:\t"))

        if choice == 'add' :
            print(add(num1,num2))
        elif choice == 'subtract':
            print(subtract(num1, num2))
        elif choice == 'multiply':
            print(multiply(num1, num2))
        elif choice == 'divide':
            print(divide(num1, num2))
        elif choice == 'modulus':
            print(modulus(num1, num2))
        elif choice == 'power':
            print(power(num1, num2))
        elif choice == 'floor_division':
            print(floor_division(num1, num2))
        history.append(choice)
    elif choice in ('history'):
        print(history)
    elif choice in ('end'):
        break
    else:
        print("invalid input")

