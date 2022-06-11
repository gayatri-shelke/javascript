list1 = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
b=[]
while i<len(list1):
    a=list1[i]
    if a not in b:
        c=b[i]
        b.append(c)
        print(b)
    i=i+1
