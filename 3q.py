def sum_(n1, n2):
    return n1 + n2

def difference(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



while True:

    print("\nChoose:\n\t1)sum\n\t2)difference\n\t3)multiple\n\t4)divide")
    operation = int(input("Your choice: "))
    n1 = int(input("number1: "))
    n2 = int(input("number2: "))

    if operation == 1:
        print(n1, "+", n2, "=", sum_(n1, n2))
    elif operation == 2:
        print(n1, "+", n2, "=", difference(n1, n2))
    elif operation == 3:
        print(n1, "+", n2, "=", multiple(n1, n2))
    elif operation == 4:
        print(n1, "+", n2, "=", divide(n1, n2))
    else:
        print("Wrong!")