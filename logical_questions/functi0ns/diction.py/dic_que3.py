dic=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
i=0
d={}
a=[]
while i<len(dic):
    d.update(dic[i])
    i=i+1
print(d)
for x in d.values():
    if x not in a:
        a.append(x)
print(a)