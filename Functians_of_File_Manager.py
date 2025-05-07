import os
# Open a file in read mode
# file = open('example.txt', 'r')
#
# # Read the first 10 characters
# content = file.read(10)
# print(content)
#
# # Check the current position of the file pointer
# position = file.tell()
# print("Current position:", position)
#
# # Close the file
# file.close()








# try:
#     file = open("geeks.txt", "r")
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# def createFile():
#     f = open("NewPython.txt", "w")
#     print("The file is created", f)
#
#
# createFile()
#
#
# def writeData():
#     f = open("NewPython.txt", "w")
#     f.write("Hi, It's a geart day today!!!")
#     f.close()
#
#
# writeData()


# def writeAddData():
#
#     f = open("NewPython.txt", "a")
#     f.write("Thank you !!!")
#     f.close()
#
#
# writeAddData()


# def readFile():
#     f = open("NewPython.txt", "r")
#     # print(f.read())
#     # print(f.read(5))
#     # print(f.readline())
#     f = open("NewPython.txt", "r")
#     for x in f:
#         print(x)
#
#
# readFile()


# def deleteFile():
#     if os.path.exists("NewPython.txt"):
#         os.remove("NewPython.txt")
#     else:
#         print("The file does not exist")
#
#
# deleteFile()
# str = "Hello"
# str = input("Enter String:")
#
# print(str[1])

# lists = list()
# data = input("Enter data:")
# lists.append(data)
# for ch in lists:
#     print(ch[1])

# arr=[]
# data = input("Enter data:")
# arr.append(data)
# for ch in arr:
#     print(ch[1])

# person = {
#     'name': 'Alice',
#     'age': 25,
#     'city': 'New York'
# }
#
# for value in person:
#     print(person['age'])

# data = input("Enter data:")
# nums = set()
# nums.add(data)
# for info in data:
#     print(data)
# print(data[3])


# mylist = ['apple', 'banana', 'cherry']
# print(mylist[1])
# i = 338.34567
# print(round(i, 3))
# print(float(i))

n = input("enter your number")
n = int(n)
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
