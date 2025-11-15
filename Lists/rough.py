# # import re
# # txt = "the rain in spain"
# # x = re.search("")


# # def find_min(lst):
# #     if len(lst) == 1:
# #         return lst[0]
# #     min_rest = find_min(lst[1:])
# #     return lst[0] if lst[0] < min_rest else min_rest

# # def greet():
# #     print("hello world")

# # greet()


# def make_multiplier(n):
#     return lambda x: x * n

# functions = [make_multiplier(i) for i in range(5)]
# print([f(10) for f in functions])

# def add(a,b,c):
#     return a+b+c

# add(*1,22,5)
# print(add)

# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)

# demo(1,2,3,x = 10,y=20)

# #-------------
# def myfunc(greeting,*names):
#     for name in names:
#         print(greeting,name)
    
# myfunc("hellow","emil","tobias","Linus")

# def myfunc(*numbers):
#     total =0
#     for num in numbers:
#         total +=num
#     return total
    
# print(myfunc(1,2,3))
# print(myfunc(10,20,30))
# print(myfunc(5))

# # def myfunction(*numbers):
# #     if len(numbers) == 0:
# #         return None
# #     max_num = numbers[0]
# #     for num in numbers:
# #         if  num>max_num:
# #             max_num = num
# #     return max_num

# # print(myfunction(2,3,5,6,7,8))

# def myfunction(*numbers):
#     if len(numbers)==0:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num>max_num:
#             max_num = num
#     return max_num
# print(myfunction(2,3,5,6,7,8))

# thislist =["apple","banana","cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple","banana","mango","cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)