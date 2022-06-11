list1 = [1, 2, 2, 5, 8, 4, 4, 8]
i=1
b=[]
while i<len(list1):
    if i not in b:

        b.append(i)
        i=i+1
print(b)
