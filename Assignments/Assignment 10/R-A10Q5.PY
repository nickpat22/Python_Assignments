'''5.Write a program which accepts one number and prints all odd numbers till that number.'''

def fact(no):
    output = list()
    for i in range(1,no+1):
        if i % 2 == 1:
            output.append(i)

    
    print("Output :",output)

def main():  
    number = int(input("Enter number : "))

    fact(number)

if __name__ == "__main__":
    main()