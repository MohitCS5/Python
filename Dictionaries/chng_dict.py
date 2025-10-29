thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
thisdict.update({"year":2000})
print(thisdict)

for x ,y in thisdict.items():
    print(x,y)

mydict = thisdict.copy()
print(mydict)

#nested dictionaries
myfamily = {
    "child1":{
         "name" : "Emil",
         "year" : 2004
    },
    "child2":{
           "name" : "Tobias",
           "year" : 2007
    },
    "child3":{
            "name" : "Linus",
            "year" : 2011
    }
}
print(myfamily.items())
print(myfamily["child2"]["year"])

thisdict = {"name":"jaspreet","age": 23,}
for x ,y in thisdict.items():
  print(x,y)
