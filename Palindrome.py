#Using stacks to check if a word is a palindrome

class PalindromeC:
    def __init__(self):
        self.stack=[]
    #Push the characters into a stack
    def push(self,characters):
        self.stack.append(characters)

    def pop(self):
        return  self.stack.pop()

def is_palindrome(s):

    checker=PalindromeC()

    for char in s:
        checker.push(char)

    for i in range(len(s) //2):
        if checker.pop()!=s[i]:
         return False
    return True


s=input("Enter a word:\n").strip()
if is_palindrome(s):
    print(f"The word is, {s}, is a palindrome.")

else:
    print(f"The word is, {s}, is not palindrome.")

