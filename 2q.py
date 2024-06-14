Mojodi = 0
while True:

    print("\nPlease choose:")
    print("\t1)Variz")
    print("\t2)Bardasht")
    print("\t3)Check Mojodi")
    A = int(input("your choice: "))

    if A == 1:
        add = int(input("how much you wanna add?"))
        Mojodi += add
    elif A == 2:
        Bardasht = int(input("how much you wanna take?"))
        Mojodi -= Bardasht
    elif A == 3:
        print("your mojodi is: ", Mojodi)



