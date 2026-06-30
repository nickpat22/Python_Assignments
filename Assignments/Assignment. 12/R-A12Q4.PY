'''4. Write a program which accepts one number and prints that many numbers starting
from 1.

Input: 5
Output: 12345'''

def string(no1):
    for i in range(1,(int(no1))+1):
        print(i,end="")

def main():  
    No1 = int(input("Enter First Number : "))

    ans = string(No1)


if __name__ == "__main__":
    main()