'''5. Write a program which accepts one number and prints that many numbers in reverse order.

Input: 5
Output: 5 4 3 2 1'''

def DisplayReverse(First):
    for i in range(First,0,-1):
        print(i,end = " ")

def main():
    a = int(input("Enter the no : "))
    DisplayReverse(a)

if __name__ == "__main__":
    main()
