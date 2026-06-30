'''4. Write a program which accepts one number and prints reverse of that number.

Input: 123
Output: 321'''

def Reverse(no):
    rev = ""
    for i in range(len(str(no)) -1,-1,-1):
        rev = rev + str(no)[i]
    

    return rev

def main():  
    number = int(input("Enter number : "))

    ans = Reverse(number)
    print("Addition is : ",ans)

if __name__ == "__main__":
    main()