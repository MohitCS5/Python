def greet():
    print("you called a function")
greet() 

def welcome():
    print("welcome you ran a funciton")
    return("you can run it again")

welcome()

def add(a,b):
    print(a+b)
    return("the number has been added")
print(add(2,3))

def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name,lname):
    print(name,lname, "hello")

my_function("mohit","verma")
def myfunc (animal,name):
    print("my animal is",name)
    print("i have a", animal)
myfunc(animal = "dog", name ="harry")

def myfunc(person):
    print("Name",person["name"])
    print("Age",person["age"])

person = {"name":"aril","age":22}
myfunc(person)

def myfunc(x,y):
    print(x+y)
    return("added the numbers")
myfunc(3,5)
def myfunc():
    return

def myfunc(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
    
# print(my_function(1,2,3))
# print(my_function(10,20,30,40))
# print(my_function(5))

# def myfunc(person):
#     print(x+y)
#     return("added the numbers")
# myfunc(4,5)
# def myfunc():
#     return


def my_function(*args):
    print("Type:",type(args))
    print("first argument:",args[0])
    print("second argument:", args[1])
    print("All arguments:" ,args)

my_function("Emil","tobias","Linus")

def my_function(greeting,*names):
    for name in names:
        print(greeting,name)

my_function("hello","Emil","Tobias","linus")

distance = 100
if distance<3 and distance>0:
    print("walk")
elif distance <=15:
    print("bike")
else:
    print("car")

#----------------------
def my_function(username,**details):
    print("username:",username)
    print("additional details:")
    for key,value in details.items():
        print(" ",key+":",value)

my_function("emil123", age = 25,city="oslo",hobby = "coding")