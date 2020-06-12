#!C:\Users\Philip\AppData\Local\Programs\Python\Python38\python.exe
# HTML Header
print("Content-Type: text/html\n")

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])

