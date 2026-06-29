'''4. Write a program which accepts one number and prints binary equivalent.'''

def Binary(First):
    ans = ""
    no = abs(First)

    if no == 0:
        print("Binary equivalent is : ",0)
        return

    while no != 0:
        ans = str(no % 2) + ans
        no = no // 2

    if First < 0:
        ans = "-" + ans

    print("Binary equivalent is : ",ans)

def main():
    a = int(input("Enter the no : "))
    Binary(a)

if __name__ == "__main__":
    main()
