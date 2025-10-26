list1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in list1:
    if "a" in x:
        newlist.append(x)
print(newlist)


#list comprehension
animals = ["cat", "dog", "rabbit", "fish", "elephant"]
filtered_animals =[ x.title() for x in animals]
print(filtered_animals)

#questions/practice
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
squared = [x**2 for x in numbers]
print(squared)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
new = []
for x in numbers:
   if x%2==0:
    new.append(x**2)
    print(new)

    
#question 3
numbers = [3,7,2,8,5,10,1]
even_numbers = []
for x in numbers:
   if x % 2 ==0:
      even_numbers.append(x)
print(even_numbers)
#list comprehension
numbers = [3,7,2,8,5,10,1]
even_numbers = [x for x in numbers if x % 2 ==0]
#iterable
x = [1,2,3,4,5,6,7,8,9]
newlist = [x for x in x if x >5]
print(newlist)





