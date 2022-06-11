a=[1,3,6,7,13,10,12]
i=0
# print(a)
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
    i+=1
print(b)


# a=[1,3,6,7,13,10,12]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             b=a[i]
#             a[i]=a[j]
#             a[j]=b
#         j=j+1
#     i=i+1
# print(a)

# name=input("enter the name")
# if len(name)%2==0:
#     print("even",name)
# else:
#     print("odd",name)
    





# c=[]
# i=1
# while i<len(a):
#     c.append(a[-1])
#     i=i+1
# print(c)

# a=[1,3,6,7,13,10,12]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):











# a=['n','i','t','i','n']
# i=len(a)-1
# n=a
# b=[]
# while i>=0:
#     t=(a[i])

#     b.append(t)
#     i=i-1
# print(b)
# if b==n:
#     print('it is palindrome number')

# else:
#     print('no')






# a=["gayatri"]
# i=0
# while i<len(a):
#     print(a[-i])
#     i=i+1
    



# a="gayatri"
# b=reversed(a)
# l=[]
# for i in b:
#     l.append(i)
# print(l)






# i=0
# c=reversed(a)
# b=[]
# while i<0:
#     if i in c:
#         b.append(i)
#     i=i+1
# print(b)


# a='gayatri'   
# i=0
# while i<len(a):
#     j=0
#     while j<i:
#         print(a[j],end='')
#         j=j+1
#     print()
#     i=i+1




# # a=["gayatri"]
# b=input("enter the name")
# a=0
# i=0
# while i<len(a):
#     # name=input("enter the name")
#     if a[i] in ("a" ,"e" , "i","o" ,"u"):
#         print("ovel",a[i])
#         a=a+1
#     elif (a[i]>="a" and a[i]<="z"):
#         i=i+1
#         print("consonat",a)
#     i=i+1


# name=input("enetr the name")
# vowel=["a","e","i","o","u"]
# new_list=list(name)
# v_count=0
# c_count=0
# for i in new_list:
#     if i in vowel:
#         v_count=v_count+1
#         print("v_count",i)
#     else:
#         print("c_count",i)
#         c_count=c_count+1
# print(v_count,"count of vowel",c_count,"count of consonant")
    
# var=123
# str(var)
# print(a)

# num1=input("enter the number")
# num2=input("enter the number")
# num3=input("enter the number")
# if num1>num2:
#     print("maximum",num1)
# elif num2>num3:
#     print("maximum",num2)
# elif num3>num1:
#     print("maximum",num3)
# else:
#     print("minimum")


# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# i=0
# a=[]
# while i<len(list1):
#     if list1 not in a:
#         a.append(list1)
    
#     i=i+1
# print(a)


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
sum=0
while i<len(marks):
    j=0
    while i<len(marks):
        sum=sum+marks[i][j]
        j=j+1
    i=i+1
print(sum)