# a=[[4,5,6],6,[5,6,7],11,[2,8,9]]
# for i in range(len(a)):
#     n=a[i]
#     if type(n) is list:

#         for j in range(len(n)):
#             b=n[j]
#             if b%2==0:
#                 print("even",b)
#             else:
#                 print("odd",b)
#     else:
#         if n%2==0:
#             print("eve",n)
#         else:
#             print("odd",n)



# num=input("enter the alphabet")
# if num>="a" and num>="z":
#     print("alphabet")
# elif num>="0" and num<="9":
#     print("digit")
# elif num=="@" or num=="#" or num=="$":
#     print("special character")
# else:
#     print("no")


a=[[4,5,6],6,[5,6,7],11,[2,8,9]]
sum=0
for i in range(len(a)):
    n=a[i]
    if type(n) is list:

        for j in range(len(n)):
            b=n[j]
            sum=sum+a[j]
            
    else:
        sum=sum+a[i]
print(sum)