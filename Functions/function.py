# def greet(name):
#     return "Hello " + name + "!"

# print(greet("vetan"))

def sum_all(x,num):
    return x+num

x = int(input("Enter your number :"))
num = int(input("Enter your 2nd number: "))
# result = sum_all()
print(sum_all)

def fehren(fahrenheit):
    return (fahrenheit -32 )*5/9

#-----------------\
def myfunc():
    x =300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x =300
def myfunc():
    x =200
    print(x)
myfunc()

print(x)

#lambda--------
cube = lambda x: x**2
print(cube(5))

def myfunc(n):
    return lambda a: a*n

double = myfunc(2)

print(double(11))

def myfunc(n):
    return lambda a: a*n
mytripler = myfunc(3)
print(mytripler(11))

def myfunc(n):
    return lambda a:a*n
double = myfunc(2)
triple = myfunc(3)

print(triple(11))
print(double(11))

numbers =[1,2,3,5,6]
doubled = list(map(lambda x:x*2,numbers))
print(doubled)

# numbers = [1,3,5,6,7]
# odd_numbers = list(filter(lambda x: x %2 ! =0 ,numbers))
# print(odd_numbers)

words =["apple","pie","mango","cherry"]
sorted_words = sorted(words ,key = lambda x:len(x))
print(sorted_words)

def countdown(n):
    if n<0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

countdown(5)