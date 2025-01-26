# Function & Recursion :-

# Function :-
            # = Function is a block of statements that perform a specific task.

# def func_name(param1, param2...):         # Create function
#     # Some Work
#     return val

# func_name(arguments1, arguments2...)        # Function Call

# def Sum(a, b):
#     s = a + b
#     return s
# print(sum(2, 3))


# Function create :-  one time create and multiple times call and use

# def Calc_Sum(a, b):             # Create Function
#     sum = a + b
#     print(sum)
#     return sum

# Calc_Sum(5, 10)                 # Multiple Calls
# Calc_Sum(36, 72)
# Calc_Sum(101, 339)


# def Calc_sum(a, b):
#     return a + b

# sum = Calc_sum(1, 2)
# print(sum)


# def print_hello():
#     print("SubhashSushil")

# print_hello()
# print_hello()
# print_hello()
# print_hello()

#---------------------------------------------

# Average of 3 numbers :- 

# def Calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg


# Calc_avg(1, 2, 3)


#----------------------------------------------

# print("SubhashSushil", end= "$")            # Sep = " "
# print("Subhashsushil")              # end = "\n"

#------------------------------------

# There are two types of function in python.
# 1. Built-in functions.
# 2. User Defined functions.
# -> Print()
# -> len()
# -> type()
# -> range()


# Default Parameters :-
            # Assigning a default value to parameter, which is used when no argument is passed.
# (kabhi bhee default value required wale value ke baad hi diya jata hain.)

# def Cal_Prod(b, a=2):
#     print(a * b)
#     return a * b

# Cal_Prod(8)




# Q. WAF to print the length of a list.  (List is the parameter)
# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
# heroes = ["thor", "ritikroshan", "Sunny deol", "pawan singh"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)



# Q. WAF to print the elements of a list in a single line. (list is the parameter)

# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end= " ")

# print_list(cities)
# print()



# Q. WAF to find the factorial of n. (n is the parameter)

# def Cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= 1
#     print(fact)


# Cal_fact(2)



# Q. WAF to Convert USD to INR.

# def Convert(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD = ", inr_val, "INR")

# Convert(10)




# Recursion :- 
        # = When a function calls itself repeatedly.
# print n to 1 backwords

# def Show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n -1)


# Q. Write a recursive function to calculate the sum of first n natural numbers.

# def Calc_sum(n):
#     if(n == 0):
#         return 0
#     return Calc_sum(n -1) + n

# Sum = Calc_sum(10)
# print(Sum)


# Q. Write a recursive function to print all elements in a list. Hint: use list & index as parameters.

# def print_list(list, index = 0):
#     if(index == len(list)):
#         return
#     print(list[index])
#     print_list(list,index + 1)


# fruits = ["Mango", "Litchi", "Apple", "Banana"]
# print_list(fruits)

