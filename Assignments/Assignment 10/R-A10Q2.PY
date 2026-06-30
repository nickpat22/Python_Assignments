'''2. Write a program which accepts one number and prints count of digits in that number.

Input: 7521
Output: 4'''


def Count(no):
    print(len(str(no)))

def main():  
    number = int(input("Enter number : "))

    Count(number)

if __name__ == "__main__":
    main()
