'''5. Write a program which accepts one number and checks whether it is palindrome or not.

Input: 121
Output: Palindrome'''

def Palindrome(no):
    rev = ""
    for i in range(len(str(no)) - 1,-1,-1):
        rev = rev + str(no)[i]

    if rev == str(no):
        print("Palindrome : ",rev)
    else:
        print("Not Palindrome")

def main():  
    number = int(input("Enter number : "))

    ans = Palindrome(number)


if __name__ == "__main__":
    main()