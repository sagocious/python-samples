from stack import *

def reverse(text):
    s = Stack()
    for c in text:
        s.push(c)
    revText = ""
    while not s.isEmpty():
        revText += s.pop()
    return revText

def isPalindrome(text):
    if text == reverse(text):
        return True
    else:
        return False


##test
print(isPalindrome("abcba"))
print(isPalindrome("addds"))
print("aaa")
