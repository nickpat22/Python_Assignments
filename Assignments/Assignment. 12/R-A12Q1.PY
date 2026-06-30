'''1. Write a program which accepts one character and checks whether it is vowel or
consonant.

Input: a
Output: Vowel'''

def Vowel(letter):
    
    if str(letter)  == str("a"):
        print("Letter is Vowel")

    elif str(letter)  == str("e"):
        print("Letter is Vowel")

    elif str(letter)  == str("i"):
        print("Letter is Vowel")

    elif str(letter)  == str("o"):
        print("Letter is Vowel")
    
    elif str(letter)  == str("u"):
        print("Letter is Vowel")
    else:
        print("Letter is not Vowel")

def main():  
    aplphabet = str(input("Enter letter : "))

    ans = Vowel(aplphabet)


if __name__ == "__main__":
    main()
