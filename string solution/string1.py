#Script To Check String Is Palindrome Or Not
def strpalindrome(p):
    re=p[::-1]
    print("Reverse Of Inputted String Is \"{}\" ".format(re))
    if re==p:
         print("\"{}\"  Is Palindrome ".format(p))
    else:
        print("\"{}\" Is Not Palindrome".format(p))
s=input("Enter String To Check:")
strpalindrome(s)
