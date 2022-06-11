"""
import json  
# Key:value mapping  
student  = {  
"Name" : "Peter",  
"Roll_no" : "0090014",  
"Grade" : "A",  
"Age": 20,  
}  
  
with open("data.json","w") as write_file:  
    json.dump(student,write_file,indent=4)  
  
with open("data.json", "r") as read_file:  
    b = json.load(read_file)  
print(b)  

"""
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
