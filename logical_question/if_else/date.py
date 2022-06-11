date=int(input("enter the date:"))
if date>=1 and date<=31:
    month=int(input("enter the month:"))
    if month>=1 and month<=12:
        year=int(input("enetr the year:"))
        if year>=0 and year<=2021:
            print(date+1,"/",month,"/",year)
        else:
            print("no")
    else:
        print("mo")
else:
    print("ascv")



temp=int(input("enter the number"))
if temp>=100:
    a=temp-100
    print(" already  water is  boil",a,"c")
    temp1=int(input("enter the number"))
    if temp1<=100:
        b=temp1+100
        print("please boil the water",b,"c")
        temp2=int(input("enter the number"))

        if temp2==10:
            print("just start boil the processe")
        else:
            print("dfg")
    else:
        print("nothing")
else:
    print("no")


