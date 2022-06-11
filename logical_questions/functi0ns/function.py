def my_function():
    d=10
    b=5
    print(d+b)
my_function()



#  Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.


# def fun():
#     num=int(input("enter the number"))
#     if num%3==0 and num%5==0:
#         print("fizzbuzz")
#     elif num%3==0:
#         print("fizz")
#     elif num%5==0:
#         print("buzz")
#     else:
#         print("bye")
# fun()


# a=[1,'2',3,'4',5]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     i=i+1
# print(b)
# # i=i+1

# a=[1,2,4,5,6,8]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     # b.append(a[-i])
#     i=i+2
# print(sum)
# # i=i+1



marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks):
        sum=sum+marks[i][j]
        j=j+1
    i=i+1
print(sum)