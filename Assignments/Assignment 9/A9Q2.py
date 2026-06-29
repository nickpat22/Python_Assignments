'''2. Write a program which contains one function ChkGreater () that accepts two numbers
and prints the greater number.

Input: 10 20
Output: 20 is greater'''

def ChkGreater(First, Second):
        if First > Second:
            print(First,"is Greater" )
        elif Second > First:
            print(Second, "is Greater")
        else:
            print("Both are Equal")
def main():
    a = input("Enter First no : ")
    b = input("Enter Second no : ")
    ChkGreater(a,b)

if __name__ == "__main__":
    main()