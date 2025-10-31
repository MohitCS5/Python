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