
s = "SlyesKimo123"
r = ""
for item in s:
    r = item + r
print(r)

#--------------------

def findPalindrome(theWord):
    if theWord.lower() == theWord[::-1].lower():
        print(theWord, " is a Palindrome!")
    else:
        print("This is not a Palindrome.")
findPalindrome("Able was I ere I saw elba")
