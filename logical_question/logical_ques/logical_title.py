# txt="gayatri"
# i=0
# while i<len(txt):
#     if i==0:
#         text=""+txt[i].upper()
#     else:
#         if txt[i]=="":
#             i=i+1
#             text=text+""+txt[i].upper()
#         else:
#             text=text+txt[i]
#     i=i+1
# print(text)



num=input("enter the name")
i=0
while i<len(num):
    if i==0:
        text=""+num[i].upper()
    else:
        if num[i]=="":
            i=i+1
            text=text+" "+num[i].upper()
        else:
            text=text+num[i]
    i=i+1
print(text)







# room=int(input("enter a number of girls "))
# if room==12:
#     print("stay here only 12 girls")
# elif room>12:
#     print("shift in another room")
# elif room<12:
#     print("add other girls ")
# else:
#     print("empty room")