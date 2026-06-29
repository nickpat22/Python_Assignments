'''4. Write a program which accepts one number and prints cube of that number.'''

def Cube(First):
    ans = First * First * First
    print("Square of the given no. is : ",ans)
        
def main():
    a = int(input("Enter the no : "))
    Cube(a)

if __name__ == "__main__":
    main()