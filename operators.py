a = True
b = False  # type-->boolean
b = "False"  # type-->string

print(2 > 3)  # False

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                  If-Else Statement                                                                 #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

if True:  # true or false condition
    print("it worked")  # it worked

num1, num2 = 100, 150
if num1 > num2:
    print("num1 is bigger")
elif num2 > num1:
    print("num2 is bigger")
else:
    print("Equal numbers")

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                  Logical Operator                                                                  #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

print(not True)  # False
print(not 2 > 3)  # True

if not 2 > 3:
    print("2 is less than 3")  # 2 is less than 3

# C++     Python
# !       not
# &&      and
# |       or
