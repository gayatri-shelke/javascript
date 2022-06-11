

square=int(input("enter the number"))
d={}
i=1
while i<=square:
    d.update({i:i*i})
    i=i+1
print(d)

