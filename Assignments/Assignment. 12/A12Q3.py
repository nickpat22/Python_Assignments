'''3. Write a program which accepts two numbers and prints addition, subtraction,
multiplication and division.'''

def Calculate(First,Second):
    print("Addition is : ",First + Second)
    print("Subtraction is : ",First - Second)
    print("Multiplication is : ",First * Second)

    if Second != 0:
        print("Division is : ",First / Second)
    else:
        print("Can not divide by zero")

def main():
    a = int(input("Enter First no : "))
    b = int(input("Enter Second no : "))
    Calculate(a,b)

if __name__ == "__main__":
    main()
