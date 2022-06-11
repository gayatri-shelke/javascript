# Take input of name and marks of 10 students and store to a dictionary.

# Output :-
# 
# student={
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 
# num=input("enter the student")
# num1=int(input("enter the marks"))
import json
d={}
i=0
while i<=2:
    num=input("enter the student")
    num1=int(input("enter the marks"))
    d.update({num:num1})
    with open("data.json","w") as f:
        json.dump(d,f,indent=4)
    i=i+1
print(d)
