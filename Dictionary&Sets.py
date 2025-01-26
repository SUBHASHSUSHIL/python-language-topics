# Dictionary :- 
# = Dictionary are use to store data values in key : value pairs They are unordered, mutable(changeable) & don't allow duplicate keys.

# dic = {
#     "name": "sushil",
#     "cgpa" : 9.8,
#     "marks": [12,543,754,22]

# }
# print(dic)

# info = {
#     "name" : "Sushil Thakur",
#     "Village" : "Singaha, Gopalganj, Bihar",
#     "Class" : "MCA"
# }
# print(info)

# info = {
#     "name" : "Sushil Thakur",
#     "Subject" : ["Python", "C#", "Java"],  #Use list
#     "Topic" : ("Dict", "Set"),              #Use Tuple
#     "age" : 24
# }
# print(info)



# Nested Dictionaries :- 

# student = {
#     "name" : "Sushil",
#     "Score" : {
#         "Chem" : 48,
#         "Phy" : 87,
#         "Math" : 96
#     }
# }
# print(student)
# print(student["name"])


# Dictionary Methods :- 
# student = {
#     "name" : "Sushil",
#     "Score" : {
#         "Chem" : 48,
#         "Phy" : 87,
#         "Math" : 96
#     }
# }
# print(student.keys())
# print(list(student.values()))
# print(student.items())
# print(student.get("Score"))


# Set in Python :- 
# Set is the collection of the unordered items each element in the set must be unique & immutable.

# nums = {1,3,5,7,8,}
# set2 = {2,3,4,3,2,2,4,5,4,3}
# print(nums)
# print(set2)

# null_set = set()
# x = int(input("enter number"))
# null_set.update(x)
# print(null_set)


# Q. Store following ward meanings in a python dictionary.
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# }
# print(dictionary)

# Q. You are given a list of subjects assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# subjects = {
#     "python", "java", "python", "java"
# }
# print(subjects)
# print(len(subjects))

# Q. WAP to enter marks of 3 subject from the user and store them in a dictionary & add one by one use subject name as key & marks as value.

# marks = []
# x = int(input("enter phy : "))
# marks.append({"phy" : x})
# x = int(input("enter Math : "))
# marks.append({"phy" : x})
# x = int(input("enter Che : "))
# marks.append({"phy" : x})
# print(marks)


# Q. Figure out a way to store 9 & 9.0 as seprate values in the set (you can take help of built-in data type)

# value = {9, 9.0}
# print(value)

# values = {
#     ("float",9.0),
#     ("int",9)
# }
# print(values)