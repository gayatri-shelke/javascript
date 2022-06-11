# Python: Print a dictionary line by line
students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}


for i in students:
    for j in students:
        print(i)
        print(i,':',students[i][j])
        break
        print(j)
        break



# Sample Output:

# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2           
