num=int(input("enter the number"))
i=0
while i<num:
    a=(num%10)
    b=(num//10)%10
    c=(num//100)%10
    if num>0:
        print(a*100)+(b*10)+(c*1)
    i=i+1