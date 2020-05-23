  
import random
line = ''
lineNum = 1
commands = ["random", "say", "var", "printvar", "whats"]
space = []
varNames = []
varValues = []

def run(code):
    global space
    if(space[0] == "random"):
        print(random.randint(0,10))
    if(space[0] == "say"):
        print(space[1])
    if(space[0] == "var"):
        if(" " not in code):
            print("SyntaxError: Invalid use of variables; Variables upon creation must have a name and a value")
            print("")
        else:
            if(space[1] not in varNames):
                varNames.append(space[1])
                varValues.append(space[2])
            else:
                varValues[varNames.index(space[1])] = space[2]
    if(space[0] == "printvar"):
        print(varNames)
        print(varValues)
    if(space[0] == "whats"):
        if(space[1] in varNames):
            print(varValues[varNames.index(space[1])])
        else:
            print("ExistenceError: Variable does not exist")
            print("")
    space = []

while True:
    line = input(str(lineNum)+': ').lower()
    lineNum += 1
    if(" " in line):
        space = line.split(' ')
    else:
        space.append(line)
        #print(space)
    if(space[0] in commands):
        run(line)
    else:
        print("Error: Not a defined function/command; All commands are lowercase")
        print("")
        space = []
