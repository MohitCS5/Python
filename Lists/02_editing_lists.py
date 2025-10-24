a = ["apple", "banana", "cherry"]
if "apple" in a:
    print("yes, apple is in the list")
else:
    print("no, apple is not in the list")

#changing the valuen in the list
a = ["apple", "banana", "cherry"]
a[1] = "kiwi"
print(a)

#range values
a = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
a[1:3] = ["blackcurrant", "watermelon"]
print(a)

a = ["apple", "banana", "cherry"]
a[1:3] = ["watermelon"]
print(a)

b = ["apple", "banana", "cherry"]
b.insert(2,"watermelon")
print(b)

b = ["apple", "banana", "cherry"]
b.append("orange")
print(b)

c = ["apple", "banana", "cherry"]
d = ["orange", "kiwi", "melon"]
c.extend(d)
print(c)

#clear method
c = ["apple", "banana", "cherry"]
del c[1]
print(c)

c = ["apple", "banana", "cherry"]
c.remove("banana")

#in remove we specify the value name but in pop we have to 
#specify the index value so use accordingly to your need