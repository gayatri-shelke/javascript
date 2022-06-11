a=[1,'2',3,'4',5]
i=0
b=[]
for i in range(len(a)):
    if type(a[i])==str:
        b.append(i)
    i=i+1
print(b)



# name=input("enetr the name")
# vowel=['a','i','o','u','e']
# new_list=list(name)
# v_count=0
# c_count=0
# i=0
# while i<len(new_list):
#     for i in (new_list):
#         if i in vowel:
#             v_count=v_count+1
#             print(v_count)
#         else:
#             c_count=c_count+1
#             print(c_count)
#         # i=i+1
# print(v_count,c_count)


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



num=int(input('enetr the number'))
# num1=int(input('enter the number'))
i=1
b=[]
while i<=num:
    j=1
    a=[]
    while j<=10:
        c=i*j
        a.append(c)
        j=j+1
    b.append(a)
    i=i+1
print(b)



# number=[4,89,9,60,58,72,56,12]
# i=0
# max1=number[0]
# sec_max=number[0]
# while i<len(number):
#     if number[i]>(max1):
#         max1=number[i]
#     if number[i]>sec_max and number[i]!=max1:
#         sec_max=number[i]
#     i=i+1
# print(sec_max)




# name=input("enetr the name")
# vowel=["a","e","i","o","u"]
# new_list=list(name)
# v_count=0
# c_count=0
# k=65
# i=0
# while i<
# for i in new_list:
#     if i in vowel:
#         v_count=v_count+1
#         print("v_count",i)
#     else:
#         print("c_count",i)
#         c_count=c_count+1

# var=123
# a=str(var)
# print(a)

# a=[1,2,2,3,3,3,4,4,4,4]
# d={}
# for i in a:
#     x=a.count(i)
#     d.update({i:x//2})
# print(d)
