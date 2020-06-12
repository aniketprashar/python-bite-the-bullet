# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                     While Loop                                                                     #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #
num = 1
while num < 10:
    print(num)
    num += 1

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                      For Loops                                                                     #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

for i in range(0, 5):  # 0 to 6 not including 6-->[0...6)
    print(i)  # print 0 to 4 each in new line

for i in range(0, 6, 2):
    print(i)  # 0 2 4 each in new line

for i in "hello":
    if i in "aeiou":
        print(i+" "+i)

students = {  # dictionary
    "male": ["Tom", "Nick", "Harry"],
    "female": ["Kathrine", "Miley", "Sakura"]
}
for i in students.keys():
    print(i)  # male \n female

students = {  # dictionary
    "male": ["Tom", "Nick", "Harry"],
    "female": ["Kathrine", "Miley", "Sakura"]
}
for i in students.keys():
    for j in students[i]:
        print(j)  # it will print all the names

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                 List Comprehension                                                                 #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# it is basically a shortcut to combine loops, variables andif statements to create a list or comprehend a list

evenNumbers = [x for x in range(1, 100) if x % 2 == 0]
print(evenNumbers)
# the first x will store the nummbers
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

listOfWords = ["the", "quick", "brown", "fox",
               "jumps", "over", "the", "lazy", "dog"]
answer = [len(x) for x in listOfWords]
print(answer)  # [3, 5, 5, 3, 5, 4, 3, 4, 3]
