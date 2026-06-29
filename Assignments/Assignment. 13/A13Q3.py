'''3. Write a program which accepts one number and checks whether it is perfect number or not.

Input: 6
Output: Perfect Number'''

def CheckPerfect(First):
    ans = 0

    for i in range(1,First):
        if First % i == 0:
            ans = ans + i

    if ans == First and First != 0:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    a = int(input("Enter the no : "))
    CheckPerfect(a)

if __name__ == "__main__":
    main()
