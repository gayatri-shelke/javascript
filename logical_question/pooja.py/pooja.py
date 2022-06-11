# d1 = {1: {'a': 11, 'b': 22}, 2: {'c': 4, 'd': 7}}

# for item in d1.values():
#     p = d1['a'] + d1['c']


# print(p)


# k=[{"a":20,"c":57},{"d":34,"o":2}]
# a=(input("entera a number"))
# t=(input("enter a number "))
# i=0
# sum=0
# while i<len(k):
#     b=k[i]
#     if a in k:
#         sum=sum+a[+t
#         # print(k[i][a])
#     print(sum)
#     i=i+1

# print(k[0]["a"]+k[1]["d"])
# print(k[0]["c"]+k[1]["o"])

# word =input("enter the name :")
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)

# d={}
# i=0
# while i<2:
    # name=input("enter a name:")
    # age=int(input("enter  a age :"))

# i=0
# num=input("enter a name")
# while i<3:
#     print(num)
#     i=i+1


# i=0
# num=int(input("enter a number "))
# num1=(num//100)%10
# while num1>0:
#     i=i+1
# print(num1)
#     # i=i+1

# lst = []
# num = int(input('How many numbers: '))
# for n in range(num):
#     numbers = int(input('Enter number '))
#     lst.append(numbers)
# print("Sum of elements in given list is :", sum(lst))


a=[1,3,6,8,9,23]
# b=[]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
print(a)
b=[]
i=1
while i<=len(a):
    b.append(a[-i])
    # print(b)
    i=i+1
print(b)

# a=[1,2,[3,4],5,6,[7,8],[9],10]
# i=0
# # while i<len(a):
# a[2].remove(3)
# a[2].append(13)
#     # a[2][0]=[13]
#     # i=i+1
# print(a)

# # L = ['a', ['bb', 'cc'], 'd']
# # L[1].append('xx')
# print(L)

# dic={'bijender':4,'deepak':60,'param':20,'anjili':30,'roshini':50}
# k={}
# for i in dic:
#     a=dic[i]
#     for j in dic:
#         b=dic[j]
#         if a>b:
#             k[j]=b
# for i in dic:
#     a=dic[i]
#     for j in dic:
#         b=dic[j]
#         if a<b:
#             k[j]=b
# print(k)

# a=10
# b=15*a
# d=15+a
# print(a//b*d//a)

# name=input("enter a name :")
# i=len(name)-1
# while i>=0:
#     print(name.upper()[i]+name.lower()[i]*(i),end="")
#     if i!=len(name):
#         print("_",end="")
#     i=i-1
# name= input("enter a name ")
# i=0
# while i<len(name):
#     print(name.upper()[i]+name.lower()[i]*(i),end="")
#     if i!=len(name):
#         print("_",end="")
#     i=i+1



# name=input("enter the number")
# i=len(name)-1
# while i>0:
#     if i!=len(name):
#         print(name[i]*(i))

#     i=i-1




# name=input("enter the number")
# i=0
# while i<len(name):
#     print(name.upper()[i]+name.lower()[i]*(i),end='')
#     if i!=len(name):
#         print("_",end="")
#     i=i+1

# vcount = 0;  
# # ccount = 0;  
# str = input("enter a name: ")
# str = str.lower(); 
# a=[] 
# for i in range(0,len(str)):   

#     if str[i] in ('a',"e","i","o","u","t"): 
#         a.append(str[i])
#         print((a),"vowel")
#         vcount = vcount + 1;  
#     elif (str[i] >= 'a' and str[i] <= 'z'):  
#         ccount = ccount + 1;
#         a.append(str[i])
#     print((a),"const")
#     print(sorted(a))

# n=input("enter a name:")
# # a="gayatri"
# if "g" in n:
#     print("g hai")
# elif "z" not in n:
#     print("z nahi hai")
# else:
#     print("no")



# num=int(input("enter the number"))
# i=1
# while i<=10:
#     print(2,'*',i,'=',i*i,'  ',3,'*',i,'=',i*i)
#     i=i+1