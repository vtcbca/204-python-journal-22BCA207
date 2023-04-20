#check user inputted string is symmetrical or not.
def strsymmetric(d):
    a=len(d)//2
    f1=d[0:a]
    f2=d[a:]
    if f1==f2:
        print(f"\"{d}\"  Is Symmetircal  String")
    else:
        print(f"\"{d}\"  Is Not Symmetircal String")
def inputstr():
       s=input("Enter String:")        
       strsymmetric(s)
inputstr()
