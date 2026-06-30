'''3. Write a program which accepts two numbers and prints addition, subtraction,
multiplication and division.'''

def calculator(no1,no2):
    print("Addition of the numbers is :", no1 + no2)
    print("Substraction of the numbers is :", no1 - no2)
    if no1 < no2:
        div = no2 / no1
    else: div = no1 / no2
    print("Division of the numbers is :",div)
    print("Multiplication of the numbers is :", no1 * no2)
    
    

def main():  
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    ans = calculator(No1,No2)


if __name__ == "__main__":
    main()