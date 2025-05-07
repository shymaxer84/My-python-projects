# def createFile():
#     f = open("NewPython.txt", "w")
#     print("The file is created", f)
#
#
# createFile()
#
#
# def writeData():
#     mylist = [1123, 'ewrtw', 545454, 'fsfssf']
#     with open("NewPython.txt", "w+") as f:
#         for items in mylist:
#             f.write('%s\n' % items)
#             f.close()
#
#
# writeData()


def readFile():
    with open("NewPython.txt") as file:
        data = file.read()
        lst = [int(i) for i in data if i.isdigit()]

    print(lst)


readFile()
