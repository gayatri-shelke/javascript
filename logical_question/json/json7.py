import json
dict1={"name":"gayatri",
"age":19,
"education":12,
"subject":"english"}
with open("data1.json","w")as write_file:
    json.dump(dict1,write_file)
# with open("data1.json","r")as read_file:
#     a=json.load(read_file)
# print(a)





# for i in [1,2,3,4,5]:   
#     if(i==4):  
#         pass  
#         print("This is pass block",i)  
#     print(i)  