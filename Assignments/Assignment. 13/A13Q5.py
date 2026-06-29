'''5. Write a program which accepts marks and displays grade.

Condition Example:
>= 75 -> Distinction
>= 60 -> First Class
>= 50 -> Second Class
< 50 -> Fail'''

def DisplayGrade(First):
    if First >= 75:
        print("Distinction")
    elif First >= 60:
        print("First Class")
    elif First >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    a = int(input("Enter marks : "))
    DisplayGrade(a)

if __name__ == "__main__":
    main()
