'''1. Write a program which accepts one number and checks whether it is prime or not.

Input: 11
Output: Prime Number'''

def fact(no):
    int(no)
    count = 0
    for i in range(1,no+1):
            if no % i == 0:
                 count = count + 1
    if count == 2:
        print("Prime no")
    else:print("Not Prime")

def main():  
    number = int(input("Enter number : "))

    fact(number)

if __name__ == "__main__":
    main()