# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"green",
#     "bat":3
#     }
# a=[]
# i=0
# for i ,j in dic.items():
#     j=i
#     if i==j:
#       print(dic)
#       break
    
# name=input("enter the name")
# # name=['gayatri']
# a=['a','e','i','o','u']
# new_list=list(name)
# v_count=0
# c_count=0
# # i=0
# # while i<len(new_list):
# for i in new_list:
#     if i in a:
#         v_count=v_count+1
#         print('v_count',i)
#     else:
#         print('c_count',i)
#         c_count=c_count+1
#         # i=i+1
# print(v_count,c_count)

    
#     

# num=int(input("enter the number"))
# count=0
# i=1
# while i<num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print('prime number')
# else:
#     print('not prime')

# num=int(input("enter the number"))
# x=0
# y=1
# z=0
# while z<=num:
#     print(x,z)
#     x=y
#     y=z
#     z=x+y


# num=input('enter tne name')
# i=0
# j=-1
# while i<len(num):
#     if num[i]==num[j]:
#         print('palindrome')
#         break

#     else:
#         print('not palidrome')
#     i=i+1
# sum=0
# num1=int(input("enetr the number"))
# a=num1
# # sum=0
# while a>0:
#     r=a%10
#     sum=sum+r
#     num1=num1//10
# if num1%sum==0:
#     print(num1,'harshad number')
# else:
#     print(num1,'not harshad number')

# n=int(input('enetr the number'))
# i=0
# a=[]
# while i<n:
#     num=input('enetr the name')
#     a.append(num)
#     print(a)
#     i=i+1

# a=[9,10,8,4,9,6,7]
# i=0
# b=[]
# while i<len(a)-1:
#     d=(a[i+1]-a[i])
#     b.append(d)
# # print(b)
#     i=i+1
# print(b)

# def num():
#     a=10
#     b=9
#     d=a+b
#     print(d)
# num()

# def square():
#     i=0
#     while i<=10:
#         a=i*2
#         print(a)
#         i=i+1
# square()

# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")

# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# def info(name, age = "12"):

#     print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")


# def student():
#     num=int(input('enetr the student'))
#     i=0
#     a=[]
#     while i<=num:
#         name=input('enetr the name')
#         a.append(name)
#         print(a)
#         i=i+1
# student()

# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()

# f1()


# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    
 
# first_function()


# def student():
#     num=int(input('enetr the number'))
#     if 18<num:
#         print('vote')
#     elif 18>num:
#         print('no vote')
#     else:
#         print('bye')
# student()

# years=int(input('enetr the years'))
# i=0
# while i<years:
#     if years%4==0 and years%100!=0 or years%400==0:
#         print('leap years')
#         break
#     else:
#         print('no')
#         break
#     i=i+1
    

# num=int(input('enetr the number'))
# num1=int(input('enetr the number'))
# if num>num1 and num1<num:
#     print(num)
# elif num1>num and num<num1:
#     print(num1)

# a=['gayatri']
# vowel=['a','e','i','o','u']
# v_count=0
# i=0
# while i<len(a):
#     if i in vowel:
#         print(v_count)
#         v_count=v_count+1
#     else:
#         print("c_count")
#     i=i+1
# print(v_count)


# max_word=int(input('enetr the number'))
# d_count=0
# a_count=0
# i=0
# while i<max_word:
#     if i.isalpha():
#         # print(i)
#         a_count=a_count+1
#     elif i.isdigit():
#         # print(i)
#         d_count=d_count+1
#     i=i+1
# print(d_count)
# print(a_count)

# name="navgurukul"
# year=2021
# year=str(year)
# A="navgurukul"
# B=name+year
# C=6**2
# print(A,B,C,"A")
# print(C)

# dic={'name':'gayatri',
# 'age':12,
# 'edcution':'12 complete'}
# for i in dic:
#     print(dic[i])


# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict: 
#     del myDict['a']
# print(myDict)

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)


# from collections import Counter
 
# # Initial Dictionary
# my_dict = {'A': 67, 'B': 23, 'C': 45,
#            'D': 56, 'E': 12, 'F': 69}
 
# k = Counter(my_dict)
 
# # Finding 3 highest values
# high = k.most_common(3)
 
# # print("Initial Dictionary:")
# # print(my_dict, "\n")
 
 
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
 
# for i in high:
#     print(i[0]," :",i[1]," ")


# a_dictionary = {"a": 1, "b": 2, "c": 3}

# # get key with max value
# max_key = max(a_dictionary, key=a_dictionary.get)

# print(max_key)


a=[2,'4',5,'54','5']
print(a[2])
# i=0
# b=[]
# while i<len(a):
#     if i in (a[0]):
#         b.append(i)
#     print(b)
