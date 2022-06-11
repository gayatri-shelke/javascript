# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

# List =[1,2,3,3,3,3,4,5]
def Unique(list1):
    # List1 =[1,2,3,3,3,3,4,5]
    i=1
    a=[]
    while i<len(list1):
        if i not in a:
            a.append(i)
            i=i+1
    print(a)


print(Unique([1,2,3,3,3,3,4,5]))

# .Write a Python function that takes a list and returns a new list with unique elements of the 
# first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5])) 

