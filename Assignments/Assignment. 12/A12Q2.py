'''2. Write a program which accepts one number and prints its factors.

Input: 12
Output: 1 2 3 4 6 12'''

def Factors(First):
    for i in range(1,First + 1):
        if First % i == 0:
            print(i,end = " ")

def main():
    a = int(input("Enter the no : "))
    Factors(a)

if __name__ == "__main__":
    main()
