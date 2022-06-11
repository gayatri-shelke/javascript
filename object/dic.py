# Write a Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
sum=0

for i in d1:
    for x in d2:
        sum=sum+d1[i]d2[x]
        dic.update(sum)
print(dic)
# // output should be this: {'a': 400, 'b': 400, 'd': 400, 'c': 300}


# a=[1,2,3,4,7,9]
# i=1
# a=0
# while i<len(a):
    
# i=1
# c=[]
# while i<len(a):
    
#     j=0
#     while j<len(a):
#         b=i*j
#         c.append(b)
#         j=j+1

#     i=i+1
# print(c)

# num=int(input("enter the number"))
# if 0<num:
#     print(-num)
# elif 0<num:
#     print(+num)
# else:
#     print(num)

# i = 1
# while(i <= 10):
#     i=i+1
#     if(i == 5):
#         # print("Skipped Element :", i)
#         continue
#     print(i)


# dic={'a':10}
# dic1={'a':20}
# a={}
# for i in dic:
#     for j in dic1:
#         a.update({dic:dic[i]+dic1[j]})
    