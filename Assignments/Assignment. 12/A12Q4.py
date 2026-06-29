'''4. Write a program which accepts one number and prints that many numbers starting from 1.

Input: 5
Output: 1 2 3 4 5'''

def Display(First):
    for i in range(1,First + 1):
        print(i,end = " ")

def main():
    a = int(input("Enter the no : "))
    Display(a)

if __name__ == "__main__":
    main()
