#script to enter 5 string and print even length string

def evenlenstr(m):
    b=0
    for i in range(5):
       n=input("Enter String : ")
       m.append(n)
    print(m)
    for j in m:
       if len(j)%2==0:
          b+=m
          print(j)
    print(f"Total String With Even Length : {c}")
m=[]
evenlenstr(m)      
