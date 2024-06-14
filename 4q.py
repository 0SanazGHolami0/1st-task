#Fahrenheit
def to_f(temp):
    return (temp + 32) * 9 / 5

#Celsius 
def to_C(temp):
    return (temp - 32) * 5 / 9

while True:
    print("\nWhich one do you need? \
        \n\t1)Fahrenheit to Celsius \
        \n\t2)Celsius to Fahrenheit")
    fc = int(input("your choice: "))
    temp = int(input("\n\tEnter the temprature: "))

    if fc == 1:
        print("The temprature is" , to_C(temp), "celcius.")
    elif fc == 2:
        print("The temprature is" , to_f(temp), "fahrenheit.")
    else:
        print("Wrong!")   
