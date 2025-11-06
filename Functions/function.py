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

#countdown---------
def countdown(n):
    if n<0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

countdown(5)

def factorial(n):
    if n==0 or n==1:
        return 1

    else:
        return n*factorial(n-1)

print(factorial(5))

#recursion with list
#calculating ths sum of al elements in a list
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list =[1,2,3,4,5,6,]
print(sum_list(my_list))

def myfunc():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("generator closed")

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ["apple","banana","cherry","mango"]
myit = iter[mytuple]

print(next([mytuple]))
print(next([mytuple]))
print(next([mytuple]))
# print(next[mytuple])