# A block of organised and reusable code that performs an action or give some result


def add(x, y):  # x and y are parameters
    return x + y


print(add(4, 5))  # 9    4,5 are arguments

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

a = 250


def fun1():
    a = 50
    print(a)


def fun2():
    a = 100
    print(a)


fun1()
fun2()
print(a)  # 50,100,250

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

a = 250


def fun1():
    # global a = 50 #syntax error
    global a
    a = 50
    print(a)


def fun2():
    a = 100
    print(a)


fun1()
fun2()
print(a)  # 50,100,50

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                  Keyword Arguments                                                                 #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #


def about(name, age, mobile):
    sentence = "Name is {}, age is {} and Mobile number is {}".format(
        name, age, mobile)
    print(sentence)


about("Aniket", 24, 0000000000)  # Name is Aniket, age is 24 and Mobile number is 0. They are called positional arguments

# -------------------------------------------------------------------------------------------------------------------------------------------------- #


def about(name, age, mobile):
    sentence = "Name is {}, age is {} and Mobile number is {}".format(
        name, age, mobile)
    print(sentence)


about(age=24, name="Prashar", mobile=9870987654)  # Name is Prashar, age is 24 and Mobile number is 9870987654

# -------------------------------------------------------------------------------------------------------------------------------------------------- #


def about(name, age, mobile=45678):  # set default values. Default parameters must be at the end
    sentence = "Name is {}, age is {} and Mobile number is {}".format(
        name, age, mobile)
    print(sentence)


about(age=24, name="Prashar")  # Name is Prashar, age is 24 and Mobile number is 45678

# -------------------------------------------------------------------------------------------------------------------------------------------------- #


def about(name="Aniket", age, mobile):
    sentence = "Name is {}, age is {} and Mobile number is {}".format(
        name, age, mobile)
    print(sentence)


about(age=24, name="Prashar", mobile=9870987654)  # non-default argument follows default argument

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                Packing And Unpacking                                                               #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

print(1, 2, 3, 4, 5)  # 5 argument
num = [1, 2, 3, 4, 5]  # 1 argument
print(num)  # [1, 2, 3, 4, 5]
print(*num)  # 1 2 3 4 5 unpacks all the elements

print("abc")  # abc
print(*"abc")  # a b c same as print("a","b","c")

# ----------------------------------------------------------------- Packing Example ---------------------------------------------------------------- #


def add(*num):
    total = 0
    for i in num:
        total += i
    return(total)


print(add(1, 2, 3, 4, 5, 6, 7, 8.5))  # any number of integers --> 36.5

# ---------------------------------------------------------------- Keyword Arguments --------------------------------------------------------------- #


def about(name, age, likes):
    string = "I am {}, I'm {} years old and I like {}".format(name, age, likes)
    return(string)


dictionary = {"name": "Aniket", "age": 24, "likes": "python"}
print(about(**dictionary))  # I am Aniket, I'm 24 years old and I like python

dictionary = {"age": 24, "name": "Aniket", "likes": "python"}
print(about(**dictionary))  # I am Aniket, I'm 24 years old and I like python. Order doesn't matter

# -------------------------------------------------------------------------------------------------------------------------------------------------- #


def foo(**dict):
    for key, value in dict.items():
        print("{}:{}".format(key, value))


foo(name="aniket", age=24, likes="python")
# name: aniket
# age: 24
# likes:python
