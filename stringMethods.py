# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                    Count Method                                                                    #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

print("hello".count("e"))  # 1

text = "happy birthday"
print(text.count("a"))  # 2
print(text.count("day"))  # 1

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                   Text Formatting                                                                  #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

x = "happy Birthday"

x = x.lower()
print(x)  # happy birthday
# strings are immutable data type so if we write x.lower and don't store the value in x, it will not change value of x.
# immutable means unchangable, mutable means changable

x = x.upper()
print(x)  # HAPPY BIRTHDAY

x = x.capitalize()
print(x)  # Happy birthday

x = x.title()
print(x)  # Happy Birthday

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

print(x.islower())  # False
print(x.istitle())  # True
print(x.isalpha())  # False because x contains a space which is not alpbhabet.
print(x.isalnum())  # False

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

y = "Aniket Prashar"
print(y.index("Prashar"))  # index position starts from 0, P is at 7th index
print(y.index("a"))  # 9 will take 1st occurance of letter
print(y.index("A"))  # 0 Case-sensitive

print(y.find("niket"))  # 1
print(y.find("nikt"))  # -1 still a valid output
# name error. So until you are sure whether the substring is present in the string don't use index method
print(y.index("nikt"))

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

z = "000ani000"
z = z.strip("0")
print(z)  # ani

zl = "000ani000"
zl = zl.lstrip("0")
print(zl)  # ani000
z.strip()  # without any parameter it will remove whitespaces

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                       Slicing                                                                      #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

s = "Aniket"
print(s[1])  # n

# string[start:end:steps] --> [start_position:end_position)
print(s[0:3:1])  # Ani
print(s[0:3:2])  # Ai
print(s[2:])  # iket
print(s[0::2])  # Aie
print(s[:3])  # Ani

# --------------------------------------------------------------- Reverse The String --------------------------------------------------------------- #

print(s[::-1])  # take steps in reverse direction
# string  A  n  i  k  e  t
# index  -6 -5 -4 -3 -2 -1
ss = "Parashar"
print(ss[-2])  # a
print(ss[::-2])  # rhaa # still we are counting the index.

print(ss[ss.index("ara"):])  # arashar

# ------------------------------------------------------ Slice Out Username From Email Address ----------------------------------------------------- #

email = "aniketprashar@hotmail.com"
username = email[:email.index("@")]
domain = email[email.index("@")+1:]

print("your username is {} and domain is {}".format(username, domain))
# your username is aniketprashar and domain is hotmail.com

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                    Split String                                                                    #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

sentence = "this is Aniket Prashar"
sentence = sentence.split()
print(sentence)  # ['this', 'is', 'Aniket', 'Prashar']
