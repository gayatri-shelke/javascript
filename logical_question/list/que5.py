# list3 = []
# for i in range(len(list1)):
#       list3.append(list1[i] + list2[i])
# list3


# n = int(input("enter a number "))
# for i in range(5, n+1 ,5):
#     if i % 2 == 1:
#         print(-i, end =" ")
#     else:
#         print(i, end =" ")

num=int(input("enter the number"))
i=0
while i>num:
    n=i
    j=0
    while j<i:
        print(i,end=" ")
        j=j+1
    i=i+1
print()


# sub1=int(input("Enter marks of the first subject: "))
# sub2=int(input("Enter marks of the second subject: "))
# sub3=int(input("Enter marks of the third subject: "))
# sub4=int(input("Enter marks of the fourth subject: "))
# sub5=int(input("Enter marks of the fifth subject: "))
# avg=(sub1+sub2+sub3+sub4+sub4)/5
# if(avg>=90):
#     print("Grade: A")
# elif(avg>=80&avg<90):
#     print("Grade: B")
# elif(avg>=70&avg<80):
#     print("Grade: C")
# elif(avg>=60&avg<70):
#     print("Grade: D")
# else:
#     print("Grade: F")


# Basic_Salary = input("Enter Basic Salary :")

# DA = (Basic_Salary * 40) / 100
# HRA = (Basic_Salary * 20) / 100
# Gross_Salary = Basic_Salary + DA + HRA

# print ("\n\nDearness Allowance 40 % of Basic Salary :" , DA)
# print ("House Rent 20 % of Basic Salary :" , HRA)
# print ("Gross Salary :" , Gross_Salary)








# units=int(input("please enter the number of units you consumed in a month"))
# if(units<=100):
#     payAmount=units*1.5
#     fixedcharge=25.00
# elif(units<=200):
#     payAmount=(100*1.5)+(units-100)*2.5
#     fixedcharge=50.00
# elif(units<=300):
#     payAmount=(100*1.5)+(200-100)*2.5+(units-200)*4
#     fixedcharge=75.00
# elif(units<=350):
#     payAmount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
#     fixedcharge=100.00
# else:
#     payAmount=0
#     fixedcharge=1500.00

# Total=payAmount+fixedcharge;
# print("\nElecticity bill=%.2f" %Total)



# i=0
# while i<10:
#     if i==5:
#         continue
# # i=i+1
#     print(i)
#     i=i+1
    
# i = 1
# while(i <= 10):
#     if(i == 5):
#         i=i+1
#         print("Skipped Element :", i)
#     # i=i+1
#         continue
# print(i)
    # i=i+1

# my_file = open("people1.txt",)
# file_data = my_file.read()
# print (file_data)
# my_file.close()

# a=[1,2,[4,5],7,9,2,6]
# i=0
# product=1
# while i<len(a):
#     n=a[i]
#     if type(n)==list:   
#         for j in range(len(n)):
#             product=product*n[j]
#     else:
#         product=product*n

#     i=i+1
# print(product)



# a=[1,2,[4,5],6,7,8]
# i=0
# p=1
# while i<len(a):
#     if type(a[i])==list:
#         for j in range(len(a[i])):
#             p=p*a[i][j]
#     else:
#         p=p*a[i]
#     i=i+1
# print(p)

# vcount = 0;  
# ccount = 0;  
# str = input("enter a name: ")
       
# #     #Converting entire string to lower case to reduce the comparisons  
# str = str.lower();  
# for i in range(0,len(str)):   

#     if str[i] in ('a',"e","i","o","u",): 
#         print(str[i],"vowal") 
#         vcount = vcount + 1;  
#     elif (str[i] >= 'a' and str[i] <= 'z'):  
#         ccount = ccount + 1;
#         print(str[i],"constant")    


# a=[1,32,5,"pooja"]
# num=a.index(32)
# print(num)

# b=a[::-1]
# print(b)

# a=[1,2,3,[7,8,],6]
# i=0
# sum=0
# while i<len(a):
#     n=a[i]
#     if type(n)==list:
#         for j in range(len(n)):
#             sum=sum+n[j]
#     else:
#         sum=sum+n
#     i=i+1
# print(sum)

# a=[2,4,[1,],[9,],8]
# i=0
# sum=0
# while i<len(a):
#     n=a[i]
#     if type(n)==list:
#         for j in range(len(n)):
#             sum=sum+n[j]
#     else:
#         sum=sum+n
#     i=i+1
# print(sum)


# i=1
# while i<4:
#     if i==1 or i==3:
#         # print(i)
#         continue
#         print(i)
#     i=i+1



# i= 0                     
# while(i < 10):                
#    i = i+1  
#    if(i == 5):  
#        print(i)
#        continue  
    # print(i)



# NumList = []

# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)

# for i in range (Number):
#     for j in range(i + 1, Number):
#         if(NumList[i] > NumList[j]):
#             temp = NumList[i]
#             NumList[i] = NumList[j]
#             NumList[j] = temp

# print("Element After Sorting List in Ascending Order is : ", NumList)
