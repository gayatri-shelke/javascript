
# Store the unique letters and their frequency of the letters from the 
# word "MISSISSIPPI" to a dictionary, were the letters are the keys and their 
# frequencies are the values.
# {'M':1,'I':4,'S':4,'P':2}


# a="MISSISSIPPI"
# count=0
# d={}
# for x in a:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]=d[x]+1
# print(d)


word=input("enter the words")
# count=0
d={}
for x in word:
    if x not in d:
        d[x]=1
    else:
        d[x]=d[x]+1
print(d)

