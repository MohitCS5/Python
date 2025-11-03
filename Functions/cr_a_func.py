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

#----------------
def square(number): #------this is parameter in parenthesis
    return(number ** 2)

result = square(5)
print(result)
#this the right way to create or use a function use return to return the valueso that
#the value doesnt directly get print in in the console 
#use a variable to store the value of the parameters 

#function with 2 parameters
def add(num1,num2):
    return(num1+num2)

result = (2,5)
print(result)

#example to learn

def multiply(p1,p2):
    return(p1*p2)

result = multiply(8,5)
# result = multiply('b',5)
# result = multiply(5,'b')
print(result)

def myfunc(a1,a2):
    return(a1*a2)

result = myfunc(3,5)
print(result)