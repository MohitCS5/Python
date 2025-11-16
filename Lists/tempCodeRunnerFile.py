a = input("Enter your word: ")
if "orange" in a:
    print ("yes," "orange is in the list")
else:
    print("no","This is not present in the list")

b = "hello world"
print(b[2:5])

list = ["apple","banana","cherry","pineapple"]
print(list[2:5])


mylist = ["apple","banana","cherry"]
mylist.append("apple")
print(mylist)
mylist = ["apple","banana","cherry"]
mylist1 = ["mango","cherrry","limejuice","coconut"]
mylist.extend(mylist1)
print(mylist)
