'''2. Write a program which accepts radius of circle and prints area of circle.'''

def Area(First):
    ans = 3.14 * First * First
    print("Area of circle is : ",ans)

def main():
    a = float(input("Enter radius : "))
    Area(a)

if __name__ == "__main__":
    main()
