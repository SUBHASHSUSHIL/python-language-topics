# String & Conditional Statement

# str1 = "Hi This is book"
# str2 = 'Hello Mr. How are you'
# str3 = """"Hi bro what's happend"""
# print(str1)
# print(str2)
# print(str3)
# print(str1 + str2) 

# str = "Hi Bipin How are you.\n i,m Good, hi do you running. \t nothing."  # Next Line Code(\n)
# print(str)



#Concadination

# str = "Hi Whats are your name?"
# str1 = "My name is Sushil Kumar Thakur."
# strs = str + str1
# print(strs)

# str1 = "Happy"
# len1 = len(str1)
# print(len1)

# str2 = "college"
# len2 = len(str2)
# print(len2)

# final_str = str1 + " " + str2
# print(final_str)
# print(len(final_str ))



# Indexing :-  (Find This Word)

# str = "Sushil Kumar Thakur"
# print(str[5])
# print(str[6])

# str = "Sushil Thakur"
# ch = str[0]
# print(ch)



# Slicing :- (find accessing part of string) +ve value

# str = "SubhashSushil Thakur"
# print(str[1 : 4])
# print(str[ : 5])
# print(str[1 : ])



#Slicing :- Negative Index

# str = "SubhashSushil"
# print(str[-6: -1])




# String Functions :-

# str = "i am Coder."
# print(str.endswith("r."))

# print(str.capitalize())

# print(str.replace("i am", "You are"))

# print(str.find("d"))

# print(str.count("am"))



# Q. WAP to input user's first name & print it's length

# name = input("enter your name : ")
# print("length of your name is ",len(name))



# Q. WAP to find the occurence of 's' in a string.

# str = "Hi $ i am $ currency"
# print(str.count("$"))



# Conditional Statement :-

#age = 35
# age = int(input("enter your age"))
# if(age >= 18):
#     print("can vote")
# else:
#     print("Can not vote")


# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("Go")
# else:
#     print("light is broken")

# num = 10
# if(num > 3):
#     print("greater than 3")
# if(num > 8):
#     print("greater than 8")


# marks = 82

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("Grade of the student -> ", grade)


# Nesting :- 

# age = 58

# if(age >= 18):
#     if(age >= 80):
#         print("Can not drive")
#     else:
#         print("Can Drive")
# else:
#     print("Can not drive")




# Q. WAP to check if a number entered  by the user is odd or even.

# num = int(input("enter number : "))
# rem = num % 2
# if(rem == 0):
#     print("even number")
# else:
#     print("odd number")


# num = int(input("enter number : "))
# if(num % 2 == 0):
#     print("even number")
# else:
#     print("odd number")



# Q. WAP to find the greatest of 3 numbers entered by the user.

# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# c = int(input("enter thid number : "))
# #d = int(input("enter fourth number : "))

# if(a >= b and a >= c):
#     print("First number is largest")
# elif(b >= c):
#     print("Second number is largest")
# else:
#     print("Third number is largest")



# Q. WAP to check if a number is a multiple of 7 or not.

# a = int(input("enter number : "))

# if(a % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple")



# Q. WAP to find the largest 4th number by the users.

# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# c = int(input("enter thid number : "))
# d = int(input("enter fourth number : "))

# if(a >= b and a >= c and a >= d):
#     print("First is largest number")
# elif(b >= c and b >= d):
#     print("Second is largest number")
# elif(c >= d):
#     print("Thid is largest number")
# else:
#     print("Fourth number is largest")

