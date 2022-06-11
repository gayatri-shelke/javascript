# a=[2,4,5,6,7,4]
# i=0
# while i<len(a):
#     print(i,a[i])
#     i=i+1


a=[2,4,5,6,7,4,[2,4,5,6]]
i=0
while i<len(a):
    if type(a) is list:
        j=0
        while j<len(a):
            print(i,j,a[i][j])
            j=j+1
    else:
        print(i,a[i])
    i=i+1
