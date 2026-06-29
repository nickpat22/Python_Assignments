'''5. Write a program which accepts one number and checks whether it is palindrome or not.

Input: 121
Output: Palindrome'''

def CheckPalindrome(First):
    temp = First
    rev = 0
    no = abs(First)

    while no != 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    if First < 0:
        rev = -rev

    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

def main():
    a = int(input("Enter the no : "))
    CheckPalindrome(a)

if __name__ == "__main__":
    main()
