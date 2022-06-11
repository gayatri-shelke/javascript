# Q21.Write a Python program to print all unique values in a dictionary. 

# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dict1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, 
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]


# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# print("Original List: ",L)

# u_value = set( val for dic in L for val in dic.values())

# print("Unique Values: ",u_value)



# Q40. Write a Python program to convert more than one list to nested dictionary. 

# Original strings:
# dic1=['S001', 'S002', 'S003', 'S004']
# dic2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# dic3=[85, 98, 89, 92]
# # Nested dictionary:
# # [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

# d=[]
# i=0
# while i<len(dic1):
#     d.update(dic1[i])
#     print(d)
#     i=i+1




# def nested_dictionary(l1, l2, l3):
#      result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
#      return result

# student_id = ["S001", "S002", "S003", "S004"] 
# student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
# student_grade = [85, 98, 89, 92]
# # print("Original strings:")
# # print(student_id)
# # print(student_name)
# # print(student_grade)
# # print("\nNested dictionary:")
# # ch='a'
# print(nested_dictionary(student_id, student_name, student_grade))


# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# for info,info1 in people.items():
#      print("\nperson_ID",info)
#      for key in people.items():
#           print(key+':',info1[key])



# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
    
#     for key in p_info:
#         print(key + ':', p_info[key])

# a=[9,3,4,2,6,7]
# i=0
# while i<len(a):
#      j=0
#      while j<len(a):
#           if j%2==0:
#                a[2]==4
#                a[3]==2
#                a[4]==6
#           else:
#                if a[i]>a[j]:
#                     temp=a[i]
#                     a[i]=a[j]
#                     a[j]=temp
#           j=j+1
#      i=i+1
# print(a)


# a=[[1,2,3,43],[3,4,5],[2,4,5,6]]
# i=0
# sum=0
# while i<len(a):
#      j=0
#      while j<len(a[i]):
#           sum=sum+a[i][j]
#           j=j+1
#      i=i+1
# print(sum)



# dic={
#      'one':{'last':12,'last1':16},
#      'two':{'last2':13,'last3':4}
#      }
# d={}
# for i in dic:
#      for j in dic[i]:
#           d.update({j:dic[i][j]})
# print(d)



# Write a Python program to get the top three items in a shop. Go to the editor
# data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for i in data:
#      print(i,':',data[i])

# 32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# for i in dict_num:
#      count=count+1
#      print(i,dict_num[i],count)

# Sample Output:

# key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6



# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# sum=[]
# count=0
# for i in dict1.values():
#      sum=sum+i
# # print(sum)
# for j in range (len(sum)):
#      a=sum[j]
#      count=count+1
# print(count)


        
     # dict1[i]=1




# Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# d={}
# for i in dic:
#      for j in dic:

#           d.update({j:dic[j]})

#      print(d)
     # for j in dic:
     #      print(i,dic[j])
# Split said dictionary of lists into list of dictionaries:



# def list_of_dicts(marks):
#     keys = marks.keys()
#     vals = zip(*[marks[k] for k in keys])
#     result = [dict(zip(keys, v)) for v in vals]
#     return result

# marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# # print("Original dictionary of lists:")
# # print(marks)
# # print("\nSplit said dictionary of lists into list of dictionaries:")
# print(list_of_dicts(marks))



# dic={{'name':'arti','age':23},{'name':'gayatri','age':23}}
# dic1={}
# for i in dic:
#      for j in dic:
#           dic1.update(j)
#           print(dic1)
          # print(i,dic[j])



# dic1={'name':['gayatri','arti','devyani'],'age':[12,45,23],'subject':['math','marathi','science']}
# a=dic1.get('name')[0]
# b=dic1.get('age')[2]
# c=dic1.get('subject')[1]
# dic={}
# for i in (a,b,c):
#      dic.update({'name':i})
# print(dic)
# print(a)


# a=[2,4,5,7,6,9]
# b=[]
# i=0
# while i<len(a):
#      if a[i]%2==0:
#           b.append("*")
#      else:
#           b.append(a[i])
#      i=i+1
# print(b)


# a=[2,4,5,7,6,9]
# b=[]
# i=0
# while i<len(a):
#      if a[i]%2==0:
#           b.append(0)
#           # print(b)
#      else:
#           b.append(a[i])
#      i=i+1
# print(b)
# i=i+1





# a=[2,4,5,7,6,9]
# b=[]
# i=0
# while i<len(a):
#      b.append(a[-i])
#      print(b)
#      i=i+1
     # print(b)

