'''3. Write a program which accepts one number and prints factorial of that number.

Input: 5
Output: 120'''


def fact(no):
    output = int(no)

    for i in range(1,no):
        output = i * output
    
    print("Output :",output)



def main():  
    number = int(input("Enter number : "))

    fact(number)

if __name__ == "__main__":
    main()
