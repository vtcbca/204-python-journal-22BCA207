#Write a script to create dictionary from list which contain student id , name and percentage
#Take student id and name till user choise.

def dicto(n):
    dic={}
    for i in range(0,len(n),3):
        dic[n[i]]=n[i+1:i+3]

    print(dic)
def takeinput():
    x=[]
    i="y"
    while i=="y" or i=="y":
        b1=int(input("Student id:"))
        x.append(b1)
        b2=input("Student name:")
        x.append(b2)
        b3=float(input("Student percentage:"))
        x.append(b3)
        i=input("Do you add more ?(y/Y):")
    print(x)
    dicto(x)

takeinput()
