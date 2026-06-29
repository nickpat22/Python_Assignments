'''1. Write a program which accepts one character and checks whether it is vowel or consonant.

Input: a
Output: Vowel'''

def Check(First):
    ch = First.lower()

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Vowel")
    else:
        print("Consonant")

def main():
    a = input("Enter the character : ")
    Check(a)

if __name__ == "__main__":
    main()
