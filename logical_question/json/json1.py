
# convert from json to python

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
print( json.loads(x))

# the result is a Python dictionary:
# print(y)