#Write a script to Replace list’s item with new value if found. Take value from user which you want to replace.


def change(n):
    a=[]
    b=int(input("Enter value you want to replace:"))
    c=int(input("Enter value you want to change with:"))
    for i in n:
        if b==i:
            a.append(c)
        else:
            a.append(i)    
    print(a)

def createlist():
    m=[]
    n=int(input("How many numbers you want to enter in list:"))
    for i in range(n):
        x=int(input("Enter a number:"))
        p.append(x)
    change(p)

createlist()
