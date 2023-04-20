#wriate a script to check if the list contains three consecutive common numbers in Python using udf.

def consecutivecoomon(p):
    count=0
    a=[]
    for i in range(len(p)-2):
        if p[i]==p[i+1] and p[i+1]==p[i+2]:
            a.append(p[i])
            count+=1
    if count>0:
        print(f"Consecutive common number in list {p} as follow:{a}")
    else:
        printf("No consecutive number in list!!")
def takeinput():
    m=[]
    n=int(input("How many number you want to enter in list:"))
    for i in range(m):
        d=int(input("Enter value:"))
        m.append(d)
    consecutivecoomon(m)        

takeinput()    
