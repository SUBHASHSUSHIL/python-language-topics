# OOP :- (Object Oriented Programming)
                            # = To map with real world scenarios, we started using objects in code.  This is called object oriented programming.


# Class & Object :-
# = Class is a blueprint For Creating Objects.
                                # Creating Class
# Class Student:
        # name = "Subhashsushil"

# Creating Object (instance)

#s1 = Student()
# print(s1.name)

# class Car:                       # Ex:- 1 class & Object
#     color = "Blue"
#     brand = "Mercedes"

# Car1 = Car()
# print(Car1.color)
# print(Car1.brand)



# Constructor  (__init__) :-
# __init__ Function :- (Constructor) :-
# = All Classes have a function called __init__(), Which is always executed when the class is being initiated.

# #creating class
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# #creating object
# s1 = Student("Subhashsushil")
# print(s1.name)


# The self parameter is a references to the current instance of the class and is used to access variables that belongs to the class.

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("Adding new student in database")

# s1 = Student("Subhashsushil")
# print(s1.name)



# Class & Instance Attributes :-
#1. class.attr
#2. obj.attr


# class Student:
#     college_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in database")

# s1 = Student("Subhashsushil", 89)
# print(s1.name)


# Methods :-
# =  Methods are functions that belong to objects.

#Creating Class

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

#     def hello(self):
#         print("hello", self.name)


# # Creating Object

# s1 = Student("SubhashSushil")
# s1.hello()



# class Student:
#     college = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student, ", self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Subhashsushil", 98)
# s1.welcome()
# print(s1.get_marks())


# Q. Create Student Class that takes name & marks of 3 subjects as arguments in Constructor. Then Create a method to print the average.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("Hi", self.name, "Your avg Score is :", sum / 3)

# s1 = Student("Subhashsushil", [84, 47,98])
# s1.get_avg()



# Static Methods :-
# = Methods that don't use the self Parameter (work at class level)

# class Student:
#     @staticmethod           # Decorator
#     def college():
#         print("ABC College..")


# * Decorators allow us to Wrap another Function in order to extend the behaviour of the wrapped function, without Permanently modifying it.

# Important:-
                            #OOP-> Object oriented Programming

# There are four pillars in OOP.
# 1. Abstraction.
# 2. Encapsulation.
# 3. Inheritance.
# 4. Polymorphism.

# 1. Abstraction :-
                # Hiding the implementation details of a class and only showing the essential features to the user.

# 2. Encapsulation :-
                # Wrapping data and functions into a single unite(object).

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started..")

# Car1 = Car()
# Car1.start()


# Q. Create Account Class with 2 Attributes-balance & account no. Create methods for debit, creadit & printing the balance.

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self,amount):
#         self.balance -= amount
#         print("RS.", amount, "was debited.")
#         print("total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("RS.", amount, "was credited.")
#         print("total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(10000, 123456)
# acc1.debit(10000)
# acc1.credit(5000)
# acc1.debit(500)


# del Keyword :-
            # Used to delete object properties or object itself.
# del s1.name
# del s1

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Subhashsushil")
# print(s1.name)
# del s1.name



# Private (like) attributes & methods :-
                            # Conceptual Implementations in python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# class Person:
#     __name__ = "anonymous"

#     def __hello():
#         print("hello person!")

# p1 = Person()
# print(p1.__hello())



# Inheritance :-
            # When one class (child / derived) derives the properties & methods of another class (parent / base).

# class Car:
#     --------

# class ToyotaCar(Car):
#     ------------


# class Car:
#     color = "Black"
#     @staticmethod
#     def Start():
#         print("Car Started..")

#     @staticmethod
#     def Stop():
#         print("Car Stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# Car1 = ToyotaCar("Fortuner")
# Car2 = ToyotaCar("Prius")

# print(Car1.color, Car2.color)



# There are 3 types of Inheritance.
# 1.Single Inheritance.
# 2.Multi-level Inheritance.
# 3.Multiple Inheritance.

# 1.Single Inheritance :-
# Base Class --> Derived Class


# 2.Multi-level Inheritance :-
# Base Class --> Derived Class --> Derived Class -->etc..

# 3.Multiple Inheritance :-
#Base Class --> Derived Class <--Base Class


# class A:
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to Class B"
# class C(A,B):
#     varC = "Welcome to Class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)



# Super Method :-
            # Super() method is used to access method of the perent class.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def Start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car stopped.")
    
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().Start()

Car1 = ToyotaCar("Prius", "Electric")
print(Car1.type)
