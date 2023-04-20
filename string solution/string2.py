#script to enter any print palindrome word and total number of palindrome word
def sentpailndrome(s):
    a=[]
    b=0
    c=s.split()
    for i in c:
        cp=i[::-1]
        if cp==i:
            print(cp)
            a.append(cp)
            b=b+1
    print(f"Total {b} Palindrome Word In String :{set(a)}")
s=input("Enter Sentence:")
sentpailndrome(s)
 
