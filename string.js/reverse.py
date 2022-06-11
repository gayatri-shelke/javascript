num=int(input('enter the number'))
a=[9,2,3,4,5,6,7,8,9]
b=[]
i=0
while i<len(a)-num:
    b.append(a[i])
    i=i+1
j=0
while j<=num:
    b.append(a[-j])
    j=j+1
# i=i+1
print(b)