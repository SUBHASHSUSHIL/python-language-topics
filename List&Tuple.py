# List in Python (Array)
# = A built-in data types that stores set of values It can store elements of different types (integer, Float, String.etc)

#marks = [12.5, 54.6, 98.4, 54.6]
# print(marks)
# print(type(marks))
#print(len(marks))
# print(marks[0])


# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["Sushil", 89.6, "Bihar"]
# print(student[1])


# string python is immutable and list is mutable.

# List Slicing:-  similar to string slicing.

# marks = [543, 54.4, 543.4, 235, 2121]

# print(marks[1 : 4])
# print(marks[ : 4])
# print(marks[1 : ])
# print(marks[-3 : -1])


#List Method :- append ka matlab kishi chij ko last me jod dena.

# list = [2, 1, 3]  #Mutable
# list.append(4)
# print(list)

# Sorting:- (Accending And Descending)

# list = [12,53,55.6,76,85,32,54]
# list.append(21)
# print(list)
# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# list.reverse()
# print(list)

# list.insert(85, 32)
# print(list)

# Sorting :- 
# list = [3, 1, 2]
# print(list.append(4))
# print(list.sort())
# print(list)

# list = ["Banana", "Litchi", "Apple"]
# print(list.sort(reverse=True))
# print(list)

# Remove :-

# list = [21,53,65,664,34]
# list.remove(1)
# print(list)

# list = [2,1,3]
# list.pop(2)
# print(list)



# Tuples in python :-  only eshme round bracket use hoga
# = A built- in data type that lets us create immutable sequences of values.

# tup = (12,43,54,75,22)
# print(tup)
# print(type(tup))

# list = (32,34,24,55,22,11)
# #print(list)
# print(list.index(32))


# Q. WAP to ask the user to enter names of their 3 favorite movie & store them in a list.

# movie1 = input("enter first movie name : ")
# movie2 = input("enter first movie name : ")
# movie3 = input("enter first movie name : ")
# movie = []

# movie.append(movie1)
# movie.append(movie2)
# movie.append(movie3)
# print(movie)

# WAP to check if a list contains a palindrome of elements (Hint: use copy() method) :- palindrome ka matlab aage se bhi shidhe or pichhe se bhi sidhe
# [1, 2, 3, 2, 1]     [1, "abc", "abc", 1]

# list = [1, 2, 1]
# # list1 = [1, 2, 3]

# copy_list1 = list.copy()
# copy_list1.reverse()

# if(copy_list1 == list):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Q. WAP to count the number of students with the "A" grade in the following Tuple.
# {"c", "d", "e", "a", "r"}

# grade = ("c", "f", "r", "s", "r")
# print(grade.count("c"))

# Q. Store the above values in a list & sort them from "A" to "D".

# grade = ["c", "d", "a", "b", "a"]
# print(grade)