a =20
b =65
if a==b:
    print("yes these are equal")
elif a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")

temp = 20
if temp>30:
    print("its hot outside")
elif temp>20:
    print("its little warm ")
elif temp>10:
    print("its cold outside")
else:
    print("its too cold ")

#shorthand if else in one line i can write the code 
a =40
b =2
print("a") if a>b else print("b")

#finding
a = 40
b = 55
max = a if a>b else b
print("this is the maximum number", max)

a = 62
b = 38
if a>b:
    print("a is greater")
else:
    print("b is greater")

#logical operators
a = 20
b = 23
c = 45
if a>b and c>a:
    print("")

temp = 23
raining = True
weekend = False
if (temp<20 and not raining) or weekend:
    print("good day for outing")

username = ""
password = ""
verified = True
if username and password and verified :
    print("login successful")
else:
    print("login failed")

