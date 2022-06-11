# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1:    
#     sum=sum+dict1[i]
# print(sum)


# def dict1():
#     d={}
#     for i in range(1,16):

#         d.update({i:i*i})
#     print(d) 
# dict1()


s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)