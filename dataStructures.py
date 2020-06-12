# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                        Lists                                                                       #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

arr = [1, 2, 3, 4, 5]
print(arr)

# lists can contain multiple data types
arr = [1, 'aniket']
print(arr)
print(arr[1])  # aniket
print(arr[1][2])  # i
print(arr[1][2:])  # iket

# Lists can have other lists inside

l = [1, 2, [11, 22], 3]

# ------------------------------------------------------------------- In Keyword ------------------------------------------------------------------- #

print(1 in l)  # True
print(22 in l)  # False
print(22 in l[2])  # True

# -------------------------------------------------------------- Add/remove From List -------------------------------------------------------------- #
# Append - Adds its argument as a single element to the end of a list. The length of the list increases by one

l.remove(3)
print(l)  # [1, 2, [11, 22]]
l.append(4)
print(l)  # [1, 2, [11, 22], 4]

# Append method returns an empty value
ll = [1, 2, 3, 4, 5]
ll = ll.append(6)
print(ll)  # none

ll = [1, 2, 3, 4, 5]
ll.append(6)
print(ll)  # [1, 2, 3, 4, 5, 6]

# ------------------------------------------------------------------ Insert Method ----------------------------------------------------------------- #

numList = [1, 2, 3, 4, 5]
numList.insert(len(numList), 6)
print(numList)
# [1, 2, 3, 4, 5, 6]. This method also returns none. Lists are mutable


# ------------------------------------------------------------------ Extend Method ----------------------------------------------------------------- #

# Extends- Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
list3 = ["aniket"]
list1.extend(list3)
print(list1)  # [1, 2, 3, 4, 5, 6, 'aniket']
list4 = ['aniket']
list1.extend(list4)
print(list1)  # [1, 2, 3, 4, 5, 6, 'aniket', 'aniket']
list1.extend("aniket")
print(list1)
# [1, 2, 3, 4, 5, 6, 'aniket', 'aniket', 'a', 'n', 'i', 'k', 'e', 't']

listx = ['aniket', 'Prashar']
del listx[0]
print(listx)  # ['Prashar']

listy = [1, 2, 3, 4]
del listy[0:2]
print(listy)  # [3,4]

# lists can concatinate with lists and not int.
A = [1, 2, 3, 4, 5]
# A = A+1   Error
A = A+[1]
print(A)  # [1, 2, 3, 4, 5, 1]

string = ['A', 'B']
string += ["string"]
print(string)  # ['A', 'B', 'string']
string += list("string")
print(string)  # ['A', 'B', 'string', 's', 't', 'r', 'i', 'n', 'g']

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                       Tuples                                                                       #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Similar to lists but once it is created it cannot be changed. Immutable data type. They are used to protect data from changes

ourTuple = 1, 2, 3, 4, 5  # enclose in brackets for more clarity
ourTuple[2] = 7  # tuple' object does not support item assignment
strx = "aniket"
strx[2] = 'g'  # 'str' object does not support item assignment

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                    Dictionaries                                                                    #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

students = {}  # empty
dict_name = {"key": "value"}
students = {"Alice": 25, "Bob": 27, "Dan": 21}
print(students["Alice"])  # 25

students["Aniket"] = 24  # will be added in the dictionary
del students["Dan"]

keys = list(students.keys())
print(keys)  # ['Aniket', 'Bob', 'Alice']
values = list(students.values())
print(values)  # [24, 27, 25]

# --------------------------------------------------------------- Nested Dictionaries -------------------------------------------------------------- #

students = {"aniket": {"id": 001, "age": 24}}
print(students['aniket']['age'])  # 24
