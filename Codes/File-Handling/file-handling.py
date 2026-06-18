# f = open("File-Handling/week-01-Python-Report.txt")
#print(f.read())

#the line above opens and reads the file, and prints them. uncomment the line in case of testing the code to see the results.
# the line below does the same as line above but this time with keyword with

# with open("File-Handling/week-01-Python-Report.txt") as myFile:
#     print(myFile.read())


# we should remember to close the file after opening it.
# f.close()
# myFile.close()

# with open("File-Handling/week-01-Python-Report.txt") as myFile:
#     print(myFile.read(100))
# myFile.close()

# f = open("File-Handling/week-01-Python-Report.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# #By looping through the lines of the file, you can read the whole file, line by line:
# f = open("File-Handling/week-01-Python-Report.txt")
# for x in f:
#     print(x)
# f.close()


# with open("File-Handling/week-01-Python-Report.txt", "a") as myFile:
#     myFile.write("Hello this line has appended to the end of file")

# with open("File-Handling/week-01-Python-Report.txt") as myFile:
#     print(myFile.read())
# myFile.close()

# with open("File-Handling/write-test.txt", "w") as myFile:
#     myFile.write("Hello this line will be overwritten after running the code over the previous lines")
# with open("File-Handling/write-test.txt") as myFile:
#     print(myFile.read())
# myFile.close()

newFile = open("File-Handling/new-file.txt", "x")
newFile.close

# import os

# os.remove("File-Handling/new-file.txt")
