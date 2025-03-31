# 1
def add2Nums():
    userInput1 = input("Please input your first number...\n>> ")
    userInput2 = input("Please input your second number...\n>> ")
    sum = int(userInput1) + int(userInput2)
    print("\nThe sum of your two numbers is: ", sum)

# 2
def makeAList():
    userList = []
    
    listLength = input("How many entries do you want in your list?\n>> ")
    
    for i in range(0, int(listLength)):
        listInput = input("Give me list entry #" + str(i) + "\n>> ")
        userList.append(listInput)
    
    print("\nHere is your list:\n>>", userList)
    
# 3
def readAFile():
    with open("userFile.txt", "r") as file:
        fileContent = file.read()
        print("Here is your file's contents:\n>> ", fileContent)
    
while True:
    userCommand = input("\nPlease choose a command from the following list by inputing the number that corresponds to the option you want to select: [1] Add 2 numbers, [2] Make a List, [3] Read from a file, [4] Exit\n>> ")

    # Add 2 Numbers Together
    if (userCommand == "1"):
        add2Nums()
        
    # Make a List
    elif (userCommand == "2"):
        makeAList()
    
    # Read From a File 
    elif (userCommand == "3"):
        readAFile()

    # Exit
    elif (userCommand == "4"):
        break
