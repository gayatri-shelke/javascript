# a=[1,2,3,[7,8,],6]
# i=0
# sum=0
# while i<len(a):
#     n=a[i]
#     if type(n)==list:
#         for j in range(len(n)):
#             sum=sum+n[j]
#     else:
#         sum=sum+n
#     i=i+1
# print(sum)


# a={1:5,4:9,5:9}
# b=a[::-1]
# print(a)

# def fun(food):
#     a=[]
#     for x in food:
#         # print(x)
#         a.append(x)
#     print(a)
# fruits=["apple","banana","cherry"]
# fun(fruits)


# num=int(input("enter a number"))
# a=[1,2,4,5,7,9,2]
# i=0
# k=[]
# while i<len(a)-num:
#     k.append(a[i])
#     i=i+1
# j=1
# while j<=num:
#     k.append(a[-j])
#     j+=1
# print(k)


# a=[1,3,6,5]
# b=[1,4,6,7]
# c=[]
# for i in range(0,len(a)):
#     c.append(a[i]+b[i])
# print(c)

# i=0
# while i<len(a):
#     c.append(a[i]+b[i])
#     i=i+1
# print(c)

# num=int(input("enter a number"))
# k=65
# i=0
# while i<num:
#     j=0
#     while j<i+1:
#         a=chr(k)
#         print(a,end=" ")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1


# list1=[1,2,4,6,7,8]
# list2=[-1,-2,3,4,-6,7]
# i=0
# b=[]
# while i<len(list2):
#     a=list2[i]
#     if a not in list1:
#         b.append(a)
#     i=i+1
# print(b)

# list1=[1,-3,6,-7,9]
# i=0
# b=[]
# while i<len(list1):
#     a=list1[i]
#     if a<0:
#         b.append((-a)*0)
#     else:
#         b.append(a)
#     i=i+1
# print(b)
    # i=i+1


#     if i not in list1:
#         b.append(i)
#     i=i+1
# print(b)


# word =input("enter the name :")
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)



# a=[-1,2,3,-4,5,-6]
# i=0
# c=[]
# while i<len(a):
#     b=a[i]
#     if b<0:
#         c.append((-b)*0)
#     else:
#         c.append(b)
#     i=i+1
# print(c)


# a=[1,2,[3,5],6,7,[9,4],6]
# i=0
# while i<len(a):
#     j=0
#     while j<i:
#         if a[i][j]==[3][0] or a[i][j]==[4] or a[i][j]==[6][0] or a[i][j]==[7]:
#             print(a*(13))
#         j=j+1
#     i=i+1


# n=int(input("enter any number"))
# a=n%10
# b=(n//10)%10
# c=(n//100)%10
# if n>0:
#     print((a*100)+(b*10)+(c*1))
# else:
#     print("not")


# def test(dictionary):
#     for key in dictionary:
#         dictionary[key].clear()
#     return dictionary

# dictionary = { 
#                'C1' : [10,20,30], 
#                'C2' : [20,30,40],
#                'C3' : [12,34]
#              }
# print("\nOriginal Dictionary:")
# print(dictionary)
# print("\nClear the list values in the said dictionary:")
# print(test(dictionary)) 


dictionary = { 
               'C1' : [10,20,30], 
               'C2' : [20,30,40],
               'C3' : [12,34]
             }
for key in dictionary:
    dictionary[key].clear()
    # return 
    
print(dictionary)