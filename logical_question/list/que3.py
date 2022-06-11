# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# d=[]
# for i in list1:


# def main():
#     list1 = [10,20,30,40,50,60,70]
#     list2 = [100,200,300,400,500,600,700]
#     cnt = -1
#     for i in range(len(list1)):
#         print(list1[i],list2[cnt])
#         cnt = cnt - 1

# main()

# list1 = [10,20,30,40,50,60,70]
# list2 = [100,200,300,400,500,600,700]
# a=[]
# c = -1
# for i in range(len(list1)):
#     c.append(list1[i],list2[c])
#     # print(c)
#     # print(list1[i],list2[c])
#     c = c - 1

# list1 = [10,20,30,40,50,60,70]
# list2 = [100,200,300,400,500,600,700]
# i=0
# c=-1
# while i<len(list1):
#     print(list1[i],list2[c])
#     i=i+1
#     c=c-1


# a=[1,2,3,4,5,6]
# i=0
# while i<len(a)-1:
#     d=a[i+1]-a[i]
#     i=i+1
#     print(d)

# a=["one","two","three","four"]
# b=[1,2,3,4]
# i=0
# c=-1
# while i<len(a):
#     print(list[i],list2[
#         c])
#     i=i+1
#     c=c-1


# Write a Python program to convert more than one list to nested dictionary. 

# Original strings:
dic1=['S001', 'S002', 'S003', 'S004']
dic2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
dic3=[85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

i=0
d={}
while i<len(dic1):
    d.update(dic1)
    print(d)
    i=i+1
