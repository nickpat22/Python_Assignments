'''4. Write a program which accepts one number and prints reverse of that number.

Input: 123
Output: 321'''

def Reverse(First):
    rev = 0
    no = abs(First)

    while no != 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    if First < 0:
        rev = -rev

    print("Reverse number is : ",rev)

def main():
    a = int(input("Enter the no : "))
    Reverse(a)

if __name__ == "__main__":
    main()
