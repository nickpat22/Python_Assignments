'''2. Write a program which accepts one number and prints count of digits in that number.

Input: 7521
Output: 4'''

def CountDigit(First):
    cnt = 0
    First = abs(First)

    if First == 0:
        cnt = 1
    else:
        while First != 0:
            cnt = cnt + 1
            First = First // 10

    print("Count of digits is : ",cnt)

def main():
    a = int(input("Enter the no : "))
    CountDigit(a)

if __name__ == "__main__":
    main()
