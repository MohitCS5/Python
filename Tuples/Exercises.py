fruits = ("apple", "banana", "cherry")
print(len(fruits))

#2nd
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#3rd
fruits = ("apple", "banana", "cherry")
del fruits
print(fruits)

#4th
fruits = ("apple","banana","mango","cherry")
(x,*y,z) = fruits
print(y)
#in this x gets the first and z gets teh last the rest goes to y

#5th
for x in ("bananna","cherry", "mango"):
    print(x)

#6
fruits = ("apple", "banana", "cherry")
i = 0
while i<len(fruits):
    print(fruits [i])
    i = i+1

#7
tuple1 = (1,2,3,5,6)
tuple1 = tuple1*2
print(tuple1)

tuple1 = (1,2,3,5,6,76)
result = tuple(x*2 for x in tuple1)
print(result)