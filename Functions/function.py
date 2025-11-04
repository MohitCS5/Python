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