# File Input / Output :-
                # Python can be used to perform operations on a file. (Read & Write Data).
# Types of all Files.
        #There are 2 types of File.
# 1. Text Files :- .txt, .docx, .log etc..
# 2. Binary Files :- .mp4, .mov, .png, .jpeg etc..


# Open, Read & Close Files :- 
                    # = We have to open a file before reading or writting.

# f = open("file_name", "mode")

# file_name = sample.txt, demo.txt
# mode = r: read mode, w: write mode


# data = f.read()
# f.close()


# f = open("demo.txt", "rt")
# data = f.data()
# print(data)
# print(type(data))
# f.close()

# Reading a file :-
# data = f.read()    # reads entire file

# data = f.readline()     #reads one line at a time

# f = open("demo.txt", "r")         # -> Read Files
# data = f.read()
# print(data)


# Writting to a files :- 

# f = open("demo.txt", "w")
# f.write("this is a new line")               # overwrites the entire file.


# f = open("demo.txt", "a")
# f.write("this is a new line")                   # adds to the file.


# Deleting a File :-
            # Using the OS Module.

# = Module (like a code library) is a file written by another programmer that generally has a functions we can use.

# import os 
# os.remove("filename")


# Q. Create a new file "Practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning file I/O
# using Java
# I like Programming in Java


# with open("Practice.txt", "w") as f:
#     f.write("Hi everyone \n we are learning file I/O \n")
#     f.write("using Java. \n I like programming in Java.")



# Q. WAF that replace all occurences of "Java" with "Python" in above File.

# with open("Practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("Practice.txt", "w") as f:
#     f.write(new_data)


# Q. Search if the word "learning" exists in the file or not.

# def Check_for_word():
#     word = "learning"
#     with open("Practice.txt", "r") as f:
#         data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("Not Found")


# Q. WAF to find in which line of the file does the word "learning" Occur first. Print -1 if word Not found.

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 line_no += 1
            
#         return -1 
#     print(check_for_line())