'''3. Write a program which accepts one number and prints square of that number.

Input: 5
Output: 25'''

def Square(First):
    ans = First * First
    print("Square of the given no. is : ",ans)
        
def main():
    a = int(input("Enter the no : "))
    Square(a)

if __name__ == "__main__":
    main()