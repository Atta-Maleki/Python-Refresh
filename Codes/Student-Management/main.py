import os


def showAll():
    studentFile = open("std.txt")
    print(studentFile.read())
    studentFile.close()

def showByID():
    userInput = input("Enter The Student's ID:")
    studentFile = open("std.txt")
    printed = False
    for lineInFile in studentFile:
        lineId = lineInFile[0:2]
        # if lineInFile[0] == userInput:
        if int(lineId) == int(userInput):
            print(lineInFile)
            string = lineInFile
            printed = True
    if printed==False:
            print("No Such Student or ID")              
    studentFile.close()
    return string, int(lineId)

def calculateAvg():
    studentFile = open("std.txt")
    scores = 0
    counter = 0
    for lineInFile in studentFile:
        scores += int(lineInFile[-3:-1])
        counter += 1
    average = scores / counter
    print("Class Average is:", average, "\n")
    studentFile.close()

def addNew():
    counter = 0
    fname = input("Enter The Student Name: ")
    lname = input("Enter The  Last Name: ")
    sscore = input("Enter Student's Score: ")
    studentFile = open("std.txt")
    for lineInFile in studentFile:
        counter += 1
    studentFile.close()
    finalString ="\n" + str(counter+1) + " " + fname + " " + lname+" "+ sscore
    with open("std.txt", "a") as studentFile:
        studentFile.write(finalString)
    studentFile.close()
    print(finalString, "\nADDED TO THE FILE SUCCESSFULLY")

def editStudent():
        counter = 0
        curser = -1
        string, lineId = showByID()
        print("Select the Field to Edit")
        userInput2 = int(input("1- First name \n2- Last name \n3- Score\n Choose:"))
        for letter in string:
            curser +=1
            # print("curser is: ", curser)
            if letter == str(" "):
                counter += 1
                # print("counter is: ", counter)
                if counter == userInput2:
                    # print ("counter and user input equal")
                    newValue = str(input("Enter New Value: "))
                    startP = curser + 1
                    # print(startP)
                    if counter == 3:
                        string2 = string.replace(string[startP:], newValue) +"\n"
                if counter-1 == userInput2:
                    # print("counter -1 is equal to user input")
                    endP = curser
                    # print(string[startP:endP])
                    string2 = string.replace(string[startP:endP], newValue)
        
        with open("std.txt", "r") as studentFile:
            lines = studentFile.readlines()
        # print(lines[int(lineId)-1])
        lines[int(lineId)-1] = string2
        studentFile.close()
        with open("std.txt", "w") as studentFile:
            studentFile.writelines(lines)
        studentFile.close()
        print(string, "Has Changed to ", string2)

def mainMenu(*args):
    if args[0] == 0:
        print("Student Management Panel")
        print("\n*****Menu*****")
        print("Choose one of the options below:")
        print("1. Show all the students")
        print("2. Show Student by ID")
        print("3. Calculate Class Avarage")
        print("4. Add a new Student")
        print("5. Edit a Student")
        print("6. Exit")
        userInput = int(input("Enter a number: "))
        os.system('clear')
        mainMenu(userInput)
    elif args[0] == 1:
        print("Show all the students")
        showAll()
        input("\nPress Enter to return to the Main Menu...")
        os.system('clear')
        mainMenu(0)
    elif args[0] == 2:
        print("Show Student by ID")
        showByID()
        input("\nPress Enter to return to the Main Menu...")
        os.system('clear')
        mainMenu(0)
    elif args[0] == 3:
        print("Calculate Class Avarage")
        calculateAvg()
        input("\nPress Enter to return to the Main Menu...")
        os.system('clear')
        mainMenu(0)
    elif args[0] == 4:
        print("Add a new Student")
        addNew()
        input("\nPress Enter to return to the Main Menu...")
        os.system('clear')
        mainMenu(0)
    elif args[0] == 5:
        print("Edit a Student")
        editStudent()
        input("\nPress Enter to return to the Main Menu...")
        os.system('clear')
        mainMenu(0)
    elif args[0] == 6:
        return
    else:
        print("end of function")
    return


mainMenu(0)
