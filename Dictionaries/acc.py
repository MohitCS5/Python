thisdict = {
    "name": "apple",
    "color": "red",
    "code": 1235
}
print(thisdict["name"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

thisdict = {
    "brand":"Ford",
    "electric": False,
    "year": 1983,
    "colors": ["red","white","blue"]

}
print(thisdict)

thisdict = dict(age = 22 , name = "arush", rollno = 21)
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
thisdict = ["year"] = 2020
print(thisdict)

car ={"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

car ={"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x =car.keys(
)
car["model"] = "apple"
print(x)
if "model" in car:
    print("yes this exist")

#methods in dictionaries
'''update()
pop()
popitem
copy
clear
fromkeys'''

