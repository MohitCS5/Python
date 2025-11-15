age = int(input("Enter you age : "))
if age<13:
    print("you are a child")
elif age>=13 and age<=19:
    print("you are a teenager")
elif age>=20 and age<=59:
    print("you are adult")
elif age>=60:
    print("U are senior")
else:
    print("please enter again")
# ------------2nd question
age = 12
wednesday = False

price = 12 if age>=18 else 8
if wednesday == True:
    price = price - 2
else:
    print("no discount for the day ")
print("the price for  you is " , price)
#------------3rd question
score = int(input("Enter your score"))
if score>=90 and score<100:
    print("You got 'A' Grade" )
elif score>=80:
    print("You got 'b' Grade")
elif score>=70:
    print("You got 'C' Grade")
else:
    print("You have bad marks")
#-------------4th question
fruit = "mango"
color = "brown"
if fruit == "banana":
    if color =="green":
        print("unripe")
    elif color == "yellow":
        print("Ripe")
    elif color =="brown":
        print("overipe")

elif fruit == "mango":
     if color =="green":
        print("unripe")
     elif color == "yellow":
        print("Ripe")
     elif color =="brown":
        print("overipe")
else:
    print("unknown fruit")

#-------------5th question
weather = "rainy"
if weather == "sunny":
    activity = ("go for a walk")
elif weather == "rainy":
    activity = ("read a book")
elif weather == "snowy":
    activity = ("build a snowman")
else:
    activity =("drink a coffee")
print(activity)

#--------------6th question
distance = 100
if distance<=3 and distance>0:
    print("walk")
elif distance<=15:
    print("bike")
else:
    print("car")
#---------------7th question
password = "thisis new passord"
if len(password)<6:
    strength = "weak"
elif len(password)<12:
    strength = "medium"
elif len(password)<20:
    strength = "hard"
else:
    print("invalid password")
print(strength)
print(len(password))
#----------------8th quesiton
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"this is a leap year")
else:
    print("this is not a leap year")

# for i in range (5):
#     print(i)

# #with break and continue
# for in inrange(6):
#     if i == 3:
#         continue
#     if i ==5:
#         print(n)


# total = 0
# for in in range(1,6):
#     total  +=1
#     print(total)
# person = {"name" : "alex", "age": 22, "city": "Delhi"}
# for key in person:
#     print(key, ":" person[key])

# for i in range (10):
#     if i % 2 ==0:
#         print(i,"is even")

#variable == name that temporarily holds each item
#sequence == list , string, range ,tuple, or anything iterable
# the intended block under it run once for each item

for x in range (5):
    print(x)

marks = [80,67,8,79]
total =0 
for m in marks:
    total +=  m
print("total:", total)


# arks = [80, 75, 90, 85]
# total = 0
# for m in marks:
#     total += m
# print("Total:", total)

def my_func(name):
    print("hello", name)