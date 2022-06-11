# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=[]
# sum=0
# for i in d1:
#     for x in d2:
#         sum=(i+x)
# #         print(sum)


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=[]
# sum=0
# for i in d1:
#     for x in d2:
#         sum=(d1[i]+d2[x])
#         print(sum)

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}

# for i,j in d1.items():
#     for x,y in d2.items():
        
#         if i==x:
#             d3[i]=(j+y)
# # print(d3)
d4={}
# for k in (d1,d2,d3,d4):
#     d4.update(k)
# print(d4)

for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
        # print(d3)
for k in (d1,d2,d3,d4):
    d4.update(k)
print(d4)




# num=int(input("eneter the number"))
# i=10
# a=[]
# while i>0:
#     num=int(input("enetr the number"))
#     a.append(num)
#     i=i-1
# print(a)
# n=int(input("enetr the number"))
# i=9
# count=0
# while i>=0:
#     if n==a[i]:
#         print("in list")
#         count=count+1
#     i=i-1
# if count==0:
#     print("not in list")





# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


# dic={0: 10, 1: 20}
# dic1={2:30}
# dic2={}
# sum=0
# for x in (dic,dic1):
#     dic2.update(x)
# print(dic2)



# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}




