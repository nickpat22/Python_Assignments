'''3. Write a program which accepts one number and prints sum of digits.

Input: 123
Output: 6'''

def SumDigit(First):
    ans = 0
    First = abs(First)

    while First != 0:
        digit = First % 10
        ans = ans + digit
        First = First // 10

    print("Sum of digits is : ",ans)

def main():
    a = int(input("Enter the no : "))
    SumDigit(a)

if __name__ == "__main__":
    main()
