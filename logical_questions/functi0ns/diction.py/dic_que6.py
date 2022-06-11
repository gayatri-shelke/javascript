# Count the total number of items from the values of the dictionary which are in the 
# form of a list.


dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
sum=[]
for x in dict1.values():
    sum=sum+x
# print(sum)
i=0
while i<len(sum):
    a=sum[i]
    count=count+1
    i=i+1
print(count)