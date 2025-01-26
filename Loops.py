# Loop :-
# = Loops are used to repeat instruction.

# There are two types of loop in python.
# 1. While loop.
# 2. For Loop.

# While loop

# count = 1
# while count <= 5:
#     print("hello")
#     count += 1

# a = 1
# while a <= 100:
#     print("SubhashSushil")
#     a += 1

# i = 1
# while i <= 500:
#     print(i)
#     i += 1

# i = 110000
# while i >= 1:
#     print(i)
#     i -= 1

# Q. Print number from 1 to 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# Infinite Loop

# i = 5
# while i < 6:
#     print(i)
#     i -= 1

# Q. Print number from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Q. Print number from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Q. Print the multiplication table of a number n. 
# i = 1
# while i <= 10:
#     print(3*i)
#     i += 1

# i = 1
# while i <= 10:
#     print(4*i)
#     i += 1

# n = int(input("enter your number : "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

# Q. Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums  = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0 
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# Q. Search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36 
# i = 0 
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx : ", i)
#     else:
#         print("Finding...")
#     i += 1


# Break & Continue keyword use :-
# Break :- Used to terminate the loop when encountered.

# Continue :- Terminates execution in the current iteration & continue execution of the loop with the next iteration.

# Break Keyword use :-
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):     # (ham koi bhi value ya number ham ush number ke bad se break laga sakte hain)
#         break
#     i += 1
# print("Loop of end")

# Continue Keyword use :-
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue        # Skip Value  (koi bhi number ko ham skip kar sakte hain continue keyword se)
#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     if(i % 2 == 0):             # Odd number Print
#         i += 1
#         continue
#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     if(i % 2 != 0):                 # Even number Print
#         i += 1
#         continue
#     print(i)
#     i += 1


# Loops are used for sequential traversal. For traversing list, string, tuples etc.

# For Loops
# for el in list:
   # # some work


# list = [1, 2, 3]
# for el in list:
#     print(el)


# For loop with else

# for el in list:
#     # Some work
# else:
#     # Work when loopend


# list = [1, 2, 3, 4]
# for el in list:
#     print(el)
# else:
#     print("end")


# Use in for :-

# Vegetables = ["Potato", "Brinjal", "Ladyfinger", "Cucumber"]
# for val in Vegetables:
#     print(val)

# nums = [1, 2, 3, 4, 5, 6]         # Use in List
# for el in nums:
#     print(el)

# tup = (1, 2, 3, 4, 5, 6)            # Use in Tuple
# for num in tup:
#     print(num)


# str = "SubhashSushil"
# for char in str:
#     print(char)
# else:
#     print("end")


# Q. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# =

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)

# Q. Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 49
# index = 0
# for el in nums:
#     if(el == x):
#         print("Number found at index : ", index)
#         break
#     index += 1


# Range() :-
# Range functions returns a sequence of number starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# for el in range(5):
#     print(el)


# for el in range(1, 5):
#     print(el)

# for el in range(1, 5, 2):
#     print(el)


# seq = range(10)
# for el in seq:
#     print(el)


# for i in range(10):             # range (stop)
#     print(i)


# for i in range(10, 20):             # range(start, stop)
#     print(i)


# for i in range(2, 100, 2):        # Even Number
#     print(i)



# for i in range(1, 100, 2):          # Odd Number
#     print(i)



# Using for & Range()
# Q. Print numbers from 1 to 100.

# for i in range(1, 101):
#     print(i)


# Q. Print number from 100 to 1.

# for i in range(100, 0, -1):
#     print(i)

# Q. Print the multiplication table of a number n.

# n = int(input("Please enter number :"))
# for i in range(1, 11):
#     print(n * i)



# Pass Statement :-
# = Pass is a null statement that does nothing. It is used as a placeholder for future code.

# for el in range(10):
#     pass


# for i in range(5):
#     pass


# if i > 5:
#     pass
# print("Some useful work..")

# Q. WAP to find the sum of first n natural numbers. (using while)
# n = 10
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     print("total sum = ", sum)


# Q. WAP to find the factorial of first n natural numbers. (Using for)
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact += 1
#     i *= 1
#     print("factorial =", fact)


# n = 5 
# fact = 1
# for i in range(1, n+1):  # Notebook Practice  factorial number
#     fact *= i
#     print("factorial =", fact)