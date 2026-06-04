def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
    print("--------------------------------")
def sub(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")
    print("--------------------------------")
def mul(a,b):
    print(f"Multiply of {a} and {b} is {a*b}")
    print("--------------------------------")
def div(a,b):
    print(f"divsion of {a} and {b} is {a/b}")
    print("--------------------------------")
def rem(a,b):
    print(f"remainder of {a} and {b} is {a%b}")
    print("--------------------------------")
while True:
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.divion")
    print("5.remainder")
    print("6.Exit")
    choice = int(input("Enter your choice:"))
    if choice ==6:
        break
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if choice == 1:
        add(a,b)
    elif choice == 2:
        sub(a,b)
    elif choice == 3:
        mul(a,b)
    elif choice == 4:
        div(a,b)
    elif choice == 5:
        rem(a,b)
    print("\n")