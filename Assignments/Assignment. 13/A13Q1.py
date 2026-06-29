'''1. Write a program which accepts length and width of rectangle and prints area.'''

def Area(First,Second):
    ans = First * Second
    print("Area of rectangle is : ",ans)

def main():
    a = float(input("Enter length : "))
    b = float(input("Enter width : "))
    Area(a,b)

if __name__ == "__main__":
    main()
