'''2. Write a program which accepts one number and prints its factors.

Input: 12
Output: 1 2 3 4 6 12'''

def factor(no):
    arr = []
    for i in range(1,no+1):
        x = no % i == 0
        if x:
            arr.append(i)
    
    return arr
    

def main():  
    number = int(input("Enter Number : "))

    ans = factor(number)
    print("Factors are :",ans)


if __name__ == "__main__":
    main()
