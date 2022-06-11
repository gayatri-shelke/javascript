# Q13.Write a Python program to sum all the items in a dictionary.

# dic1={1:12,3:24,2:13,4:34}
# dic={}
# sum=0

# for i in dic1:
#     sum=sum+dic1[i]
#     dic.update(sum)
#     print(dic)


# dic={}
# i=0
# while i<5:
#     num=int(input("enter the number"))
#     num1=int(input("enter the number"))
#     dic.update({num:num1})
#     i=i+1
#     print(dic)




# a=[[4,5,6],6,[5,6,7],11,[2,8,9]]
# sum=0
# for i in range(len(a)):
#     n=a[i]
#     if type(n) is list:

#         for j in range(len(n)):
#             b=n[j]
#             sum=sum+a[j]
            
#     else:
#         sum=sum+a[i]
# print(sum)



import json
file=open('data.json','r')
x=file.read()
finaldata=json.loads(x)
print(finaldata)
