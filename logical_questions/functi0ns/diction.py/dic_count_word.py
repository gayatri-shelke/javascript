# a='w3resource'

# d={}
# count=0
# for i in a:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]=d[i]+1
#         print(d)



# dic={}
# # count=0
# for i in a:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]=dic[i]+1
# print(dic)

a="3+0j"





# num=input("enetr the number")
# dic={}
# for i in num:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]=dic[i]+1
# print(dic)


# num=int(input("enetr the number"))
# dic={}
# i=1
# while i<num:
#     dic.update({i:i*i})
#     i=i+1
#     print(dic)


# i=0
# while i<=4:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     while j>=1:
#         print(j,end=" ")
#         j=j-1
#     print()
#     i=i+1



num=int(input("enetr the number"))
a=[]
i=1
while i<=num:
    j=1
    b=[]
    while j<=10:
        c=i*j
        b.append(c)
        j=j+1
    a.append(b)
    i=i+1
print(b)

