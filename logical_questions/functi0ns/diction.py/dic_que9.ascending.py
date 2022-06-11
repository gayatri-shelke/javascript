# Write a program to sort a dictionary in ascending or descending according to its values .

# Input :-

dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# Visualize
for i in range(len(dict1)):
    for j in range(len(dict1)):
        if dict1[i]<dict1[j]:
            b=dict1[i]
            dict1[i]==dict1[j]
            dict1[j]==b
            print(dict1)
