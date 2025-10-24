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