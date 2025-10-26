thistuple = ("apple", "banana", "Mango", "banan")
print(len(thistuple))
print(type(thistuple))

thistuple2 = ("kiwi")
print(type(thistuple2))

#accessign typle items
thistuple3 = ("apple", "banana", "cherry", "Mango", "banan")
print(thistuple3[1])

thistuple = ("apple", "banana", "cherry", "Mango", "banan")
print(thistuple[1:3])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#change the value of the tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(type(x))
print(x)

#adding items in the tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

#unpackign a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)