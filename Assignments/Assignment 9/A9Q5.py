'''5. Write a program which accepts one number and checks whether it is divisible by 3 and

Input: 15
Output: Divisible by 3 and 5'''

def Check(First): 
    if First % 3 == 0:
        print(First,"is divisible by 3")
    else:
        print("The no is not Divisible by 3")
        
def main():
    a = int(input("Enter the no : "))
    Check(a)

if __name__ == "__main__":
    main()