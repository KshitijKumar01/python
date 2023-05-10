# def test():
#     pass #won't be necessary to give the bodu of the function

# def test1():
#     print("this is test1")
# test1()

# def test2():
#     return "This is test2"
# print(test2() + " hello")

# #test3 will give the tuple of the different return data
# # (1, 'kshitij', [1, 2, 3, 4]) output
# def test3():
#     return 1, "kshitij", [1,2,3,4]
# print(test3())

# def test4():
#     a = 5+7/7
#     return a
# print(test4())

# def test5(a, b, c):
#     d = a+b/c
#     return d
# print(test5(1,2,3))


# l = [1,2,4,5, "Kshitij", [1,2,4,4], 3.4, 5.7]
# def test6(l):

#     """this is func to extract numbers from list"""
#     ans = []
#     for i in l:
#         if type(i) == int or type(i) == float:
#             ans.append(i)
#         if type(i) == list:
#             for j in i:
#                 ans.append(j)
#     return ans

# print(test6(l))


# # args allows us to give the multiple arguments to the functions we can also use the different name in the place of args
# def test7(*args):
#     return args
# print(test7(2,3,3,45,5))

# def test8(*args, a):
#     return args, a
# print(test8(2,3,4, a = 13))

# generator functions

# def fib(n):
#     a,b = 0, 1
#     for i in range(n):
#         # print(a)
#         yield(a) # yield keyword is used for making the generator function
#         a, b = b, a+b

# for i in fib(10):
#     print(i)


# lambda function

# n = 3
# p = 2
# def test10(n, p):
#     return n**p
# print(test10(n, p))

# a = lambda n, p : n**p
# print(a(n, p))

# c_to_f = lambda c : (9/5)*c +32
# print(c_to_f(45))

# # fiding the max
# finding_max = lambda x, y : x if x>y else y 
# print(finding_max(23, 42))


# map, reduce, filter function

# l = [1,2,3,4,5,6,7]

# def sq(x):
#     return x**2
# print(list(map(sq, l)))

# # using lambda function
# print(list(map(lambda x : x**2, l)))

# # adding elements of two lists
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# print(list(map(lambda x, y : x+y, l1, l2)))



# # reduce,: can take only 2 parameters
# from functools import reduce
# l3 = [1,2,3,4,5,6,7]
# print(reduce(lambda x,y : x+y, l3))
# print(reduce(lambda x, y : x if x>y else y, l3))

# # filter
# print(list(filter(lambda x : x%2 == 0, l3)))



# check prime number
def prime_checker(number):
    for i in range(2, number//2+1):
        if(number % i == 0):
            return "not prime"
    
    return "prime"

n = int(input("Enter the number : "))
print(prime_checker(n))