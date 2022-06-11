# a=int(input("enter your age"))
# b=int(input("enter your year"))
# if a-b>0:
#     age=a-b
#     print("thise is your age",age)
# elif a-b<1:
#     print("your age is less than one year")
# else:
#     print("wrong yeg")


# a=[[0],[1,3],[5,4,9],[4,3],[5,3],6,[4,3]]
# i=0
# sum=0
# while i<len(a):
#     b=a[i]
#     if type(b) is list:
#         for j in range(len(b)):
#             sum=sum+b[j]
#     else:
#         sum=sum+a[i]
#     i=i+1
#     print(sum)


birth_year=int(input("enter the number"))
current_year=2021
a=birth_year-current_year
if birth_year<current_year:
    print(a)
else:
    print("no")