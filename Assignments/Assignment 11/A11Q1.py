'''1. Write a program which accepts one number and checks whether it is prime or not.

Input: 11
Output: Prime Number'''

def Prime(First):
    count = 0
    for i in range(1, First + 1):
        if First % i == 0:
            count = count + 1
    
    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime")

def main():
    num = int(input("Enter the no : "))
    Prime(num)

if __name__ == "__main__":
    main()