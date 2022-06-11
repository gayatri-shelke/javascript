# list=[1,-3,4,-6,2,-8,-9]
# i=0
# while i<len(list):
#     if list


dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,6:60}
# dic5={7:67,9:25}
d3 = {}
for i, j in dic1.items():
    for x, y in dic2.items():
        if i ==x:
            d3[i]=(j+y)
            print(d3)
dic4 = {}
for d in (dic1, dic2, dic3,d3):
    dic4.update(d)
print(dic4)





# dic1={1:10, 2:20} 
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic5 = {}
# for i in (dic1, dic2, dic3): 
#     dic4={7:10,8:10}
#     dic5.update(dic4)
# print(dic5)

# print(9%12)
# print(5%9)

# number=[1,2,4,5,6,7]
# i=0
# while i<len(number):
    
#     i=i+1
# print(i)
    
# number=[1,2,4,5,6,7]
# for i in range (len(number)):
#     print(i)


# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)




fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print (len(fruit))
print(fruit)





Student = {}
Age = {}
Details = {}
Student['name'] = "bikki"
Age['student_age'] = 14
Details['Student'] = Student
Details['Age'] = Age

print (len(Details["Student"])) 


