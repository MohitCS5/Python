# a =20
# b =65
# if a==b:
#     print("yes these are equal")
# elif a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")

# temp = 20
# if temp>30:
#     print("its hot outside")
# elif temp>20:
#     print("its little warm ")
# elif temp>10:
#     print("its cold outside")
# else:
#     print("its too cold ")

# #shorthand if else in one line i can write the code 
# a =40
# b =2
# print("a") if a>b else print("b")

# #finding
# a = 40
# b = 55
# max = a if a>b else b
# print("this is the maximum number", max)

# a = 62
# b = 38
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")

# #logical operators
# a = 20
# b = 23
# c = 45
# if a>b and c>a:
#     print("")

# temp = 23
# raining = True
# weekend = False
# if (temp<20 and not raining) or weekend:
#     print("good day for outing")

# username = ""
# password = ""
# verified = True
# if username and password and verified :
#     print("login successful")
# else:
#     print("login failed")

# a = 1
# while a<=10:
#     print(3*a)
#     a+=1

# str = ("arivansh","navrot","manmohak","nipul","nitin","mohit")
 
# num = (1,2,3,4,5,6,7,8,9,10)
# i =0
# while i<len(num):
#     print(num[i])
#     i += 1
    
#finding the number at nth index

num = (8,5,7,87,8,7,35,5,56,)
i = 35
x = 0
while x<len(num):
    print(num[x])
    if num[x] == i:
        print("found the number....")
        break
    x += 1


