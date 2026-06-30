'''3. Write a program which accepts one number and prints sum of digits.

Input: 123
Output: 6'''

def Add(no):
    sum = 0
    str(no)
    for i in str(no):
        sum = sum + int(i)
    return sum

def main():  
    number = int(input("Enter number : "))

    ans = Add(number)
    print("Addition is : ",ans)

if __name__ == "__main__":
    main()