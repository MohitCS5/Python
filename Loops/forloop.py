fruits = ("apple","banana","cherry")
for x in fruits[2]:
    print(x)
for x in fruits:
    print(x)
for x in "banana":
    print(x)

#will stop when it gets banana
fruits = ("apple", "cherry", "banana", "watermelon", "mango")
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ("apple","banana","watermelon","mango")
for x in fruits:
    if x=="banana":
     print(x)
     break


fruits = ("apple", "banana","mango")
for x in fruits:
    if x == "banana":
        continue
    print(x)

#range fuction
for x in range(9):
    print(x)
#specifing the start value
for x in range(2,5):
    print(x)

#specifying the increment by default 1 number increses
#but you can specify the increment
for x in range(2,10,2):
    print(x)

for x in range(20):
    if x ==4:break
    print(x)
else:
    print("the loop has ended")#usign break will not print else in bw

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)