'''4. Write a program which accepts one number and prints all even numbers till that
number.

Input: 10
Output: 2 4 6 8 10'''

def fact(no):
    output = list()
    for i in range(1,no+1):
        if i % 2 == 0:
            output.append(i)

    
    print("Output :",output)

def main():  
    number = int(input("Enter number : "))

    fact(number)

if __name__ == "__main__":
    main()