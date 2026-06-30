'''5. Write a program which accepts one number and prints that many numbers in reverse
order.

Input: 5
Output: 54321'''

def string(no1):
    for i in range((int(no1)) ,0,-1):
        print(i,end="")

def main():  
    No1 = int(input("Enter First Number : "))

    ans = string(No1)


if __name__ == "__main__":
    main()