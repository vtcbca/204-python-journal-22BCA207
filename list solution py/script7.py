#Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.
def changename(p):
    filechange=[]
    q=".m"
    for i in p:
        if q in i: 
            x=i.replace(".m",".py")
            filechange.append(x)
        else:
            filechange.append(i)    

    print(filechange)    

filesname = ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
changename(filesname)
