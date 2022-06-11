# 1            *                           *
# 12           * *                       *   *
# 123          * * *                   *   *   * 
# 1234         * * * *               *    *   *   *
# 12345        * * * * *           *    *    *   *   *

# i=1
# while i<=5:
#     a=1
#     while a<=5-i:
#         print(end="")
#         a=a+1
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1


# i=5
# while i<=5:
#     a=1
#     while a<=5:
#         a=a+1
#         print(end=" ")
#     j=1
#     while j<=5-i:
#         print("*",end=" ")
#         j=j-1
#     print()
#     i=i+1

# i=1
# while i<30:
#     if i%3==0 and i%7==0:
#         print("hello",i)
#     elif i%3==0:
#         print("hi",i)
#     elif i%7==0:
#         print("navgurukul",i)
#     else:
#         print("no",i)
#     i=i+1


# i=0
# sum=0
# while i<10:
#     num=int(input("enter the number"))
#     sum=sum+num
#     print(sum)
#     i=i+1


# i=1
# while i<5:
#     j=1
#     while j<i:
#         print(j,end="")
#         j=j+1
#     i=i+1
#     print()


num=int(input("enter the number"))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(end=' ')
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
