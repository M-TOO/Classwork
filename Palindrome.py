#Using stacks to check if a word is a palindrome
#I imported string so that i can use the inbuilt ascii-letters
import string
class PalindromeC:
    def __init__(self):

        self.stack=[]
    #Push the characters into a stack
    def push(self,characters):
        self.stack.append(characters)

    def pop(self):
        return  self.stack.pop()

# This is the definition of a function that holds the inputed value
def is_palindrome(s):

    s = ''.join(c.lower() for c in s if c in string.ascii_letters)
    print(s)
    checker=PalindromeC()

    for char in s:
        checker.push(char)

    for i in range(len(s) //2):
        if checker.pop()!=s[i]:
         return False
    return True


if  __name__=="__main__":# This allow only this class to run

    s=input("Enter a word:\n").strip().lower()

    #To abide by the constraints given
    if not (1<=len(s)<=150):
        print("This value is not allowed")
        exit()#To exit the code
    if is_palindrome(s):
        print(f"The word is, {s}, is a palindrome.")

    else:
        print(f"The word is, {s}, is not palindrome.")

