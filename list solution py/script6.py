#WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().

def evenodd(n):
    even,odd=[],[]
    count1,count2=0,0
    for i in n:
        if i%2==0:
            even.append(i)
            count1+=1
        else:
            odd.append(i)
            count2+=1
    
    print(f"The even numbers are {count1} and numbers:")
    printlist(even)
    
    print(f"The odd numbers are {count2} and numbers:")
    printlist(odd)


def printlist(d):
    for i in d:
        print(i)

def createlist():
    p=[]
    q=int(input("How many numbers you want to enter in list:"))
    for i in range(q):
        r=int(input("Enter a number:"))
        p.append(r)
    evenodd(p)

createlist()
