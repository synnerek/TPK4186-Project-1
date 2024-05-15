# TPK4186 - 2023 - Assignment 1

# 1. Imported modules
# -------------------

import sys
import random

# 2. Containers
# -------------
# This section consists of functions to create containers, and functions to get the variables and set new ones. 

# Creates a new container with inputs serial number, length and cargo. The function uses the two functions Container_NewSmall()
# and container Container_NewBig) implicit
def Container_New(serialNumber, length, cargo):
    if length==20:
        return Container_NewSmall(serialNumber, cargo)
    elif length==40:
        return Container_NewBig(serialNumber, cargo)
    else:
        print("Length not valid")
    

# Creates a new small container. Verifies if the cargo is suitable for a small container
def Container_NewSmall(serialNumber, cargo):
    if 0 <= cargo <= 22:
        return [serialNumber, 20, 2, cargo]
    else:
        print("Cargo out of range")

# Creates a new small container. Verifies if the cargo is suitable for a big container
def Container_NewBig(serialNumber, cargo):
    if 0 <= cargo <= 24:
        return [serialNumber, 40, 4, cargo]
    else:
        print("Cargo out of range")

# Gives the serialnumber of a certain container as output
def Container_GetSerialNumber(container):
    return container[0]

# Sets a new serialnumber for a certain container
def Container_SetSerialNumber(container, serialNumber):
    container[0] = serialNumber

# Gives the length of a certain container as output
def Container_GetLength(container):
    return container[1]

# Sets a new length for a certain container
def Container_SetLength(container, length):
    container[1] = length

# Gives the weight of a certain container as output
def Container_GetWeight(container):
    return container[2]

# Sets a new weight for a certain container
def Container_SetWeight(container, weight):
    container[2] = weight

# Gives the cargo of a certain container as output
def Container_GetCargo(container):
    return container[3]

# Sets a new cargo for a certain container
def Container_SetCargo(container, cargo):
    container[3] = cargo
    
# Gives the total weight of a container (cargo pluss initial weight)
def Container_GetTotalWeight(container):
    return int(Container_GetWeight(container) + Container_GetCargo(container))


    

# 3. Ships
# --------
# This sections consists of functions to create a new ship with measurements, get initial variables and set new ones

# Creates a new ship with a given length, height and width. When created, each ship will consist if the three variables, and in 
# addition an empty list for containers, a dictionary with all possible positions on the ship, and a variable stating whether the ship
# is completed with loading will be created
def Ship_New(length, width, height):
    return [int(length/2), width, height, [], MakeDictionaryOfPositions(length, width, height), False]

# Gives the length of a certain ship as output
def Ship_GetLength(ship):
    return ship[0]

# Sets a new length for a certain ship
def Ship_SetLength(ship, length):
    ship[0] = length/2

# Gives the width of a certain ship as output
def Ship_GetWidth(ship):
    return ship[1]

# Sets a new width for a certain ship
def Ship_SetWidth(ship, width):
    ship[1] = width

# Gives the heigth of a certain ship as output
def Ship_GetHeight(ship):
    return ship[2]

# Sets a new heigth for a certain ship
def Ship_SetHeight(ship, height):
    ship[2] = height


# Creates a dictionary with all possible positions on the ship. Each positions has the values (x, y, z) = (width, length, height).
# The length of the variable length is halved in order to easier keep track of the containers. Each position stores either
# one 40 feet container or a pair of 20 feet containers. 
def MakeDictionaryOfPositions(length, width, height):
    Ship_Dict = {}
    for x in range(0, width):
        for y in range(0, int(length/2)):
            for z in range(0, height):
                Ship_Dict[(x,y,z)] = None
    return Ship_Dict


# Gived the position of containers
def Ship_GetPositionOfContainers(ship):
    dicten = Ship_GetContainerDictionary(ship)
    newdict = {}
    for x in range(0, int(Ship_GetWidth(ship))):
        for y in range(0, int(Ship_GetLength(ship))):
            for z in range(0, int(Ship_GetHeight(ship))):
                if (dicten[(x,y,z)] != None):
                    newdict[(x,y,z)] = dicten[(x,y,z)]
    return newdict


# Gives the number of containers supposed to be loaded on the ship
def Ship_GetContainers(ship):
    return ship[3]

# Gives the number of containers. Since they are stored as either a single 40 feet container or a pair of two 20 feet containers,
# the function must iterate through the list to find wheter each element is only a 40 feet container, or a set of two 20 feet containers
# in order to calculate the total number of containers.
def Ship_GetNumberOfContainers(ship):
    number = 0
    containerlist = ship[3]
    for element in containerlist:
        if (len(element)==2):
            number +=2
        else:
            number +=1
    return number

# Gives the nth (index input) container
def Ship_GetNthContainer(ship, index):
    newcontainerlist = []
    containers = Ship_GetContainers(ship)
    for container in containers:
        if (len(container)==2):
            newcontainerlist.append(container[0])
            newcontainerlist.append(container[1])
        else:
            newcontainerlist.append(container)
    return newcontainerlist[index]

# Returns the dictionary in the ship
def Ship_GetContainerDictionary(ship):
    return ship[4]

# Inserts container
def Ship_InsertContainer(ship, container, index):
    containers = Ship_GetContainers(ship)
    containers.insert(index, container)
    Ship_AppendContainerToDictionary(ship, container)

# Appends container
def Ship_AppendContainer(ship, container):
    containers = Ship_GetContainers(ship)
    containers.append(container)
    #Ship_AppendContainerToDictionary(ship, container)

# finds a container in the ship with the serial number that matches the input
def Ship_LookForContainer(ship, serialNumber):
    return ship[4].get(serialNumber, None)

# Appends container to dictionary
def Ship_AppendContainerToDictionary(ship, container):
    Ship_Dict = ship[4]
    for key in Ship_Dict:
        if Ship_Dict[key] == None:
            Ship_Dict[key] = container
            break

# removes a container from the dictionary in the ship
def Ship_RemoveContainerFromDictionary(ship, container):
    Ship_Dict = ship[4]
    # er dette riktig?
    if (Ship_Dict.getKeys.contains(Container_GetSerialNumber(container))):
        del Ship_Dict[Container_GetSerialNumber(container)]

    

#Gjøre om listen til dictionary når alle containers er lagt inn i lista. Først da kan de få en posisjon (x, y, z)

# Method to lock so that you cannot load on any more containes
def ShipLock(ship):
    ship[5] = True

# Returns the ship lock
def Ship_GetShipLock(ship):
    return ship[5]

# sorts the containers based on length
def sortContainersLength(ship):
    while (ShipLock(ship) == False):
        break
    containerList = ship[3]
    newContainerList = []

    for container in containerList:
        length = Container_GetLength(container)
        if length==20:
            newContainerList.append(container)

    for container in containerList:
        length = Container_GetLength(container)
        if length==40:
            newContainerList.append(container)
    ship[3] = newContainerList
    return newContainerList

# sorts the containers based on weight and length. puts 20 feet containers in pairs
def sortContainers(ship):
    if (ShipLock(ship) == False):
        containerList = sortContainersLength(ship)
        containerList20 = []
        newContainerList = []

        for container in containerList:
            length = Container_GetLength(container)
            if length == 40:
                newContainerList.append(container)
        
        for container in containerList:
            length = Container_GetLength(container)
            if length == 20:
                containerList20.append(container)
        
        for i in range(len(containerList20)):
            while (i+1)<len(containerList20)-1:
                pair = [containerList20[i], containerList20[i+1]]
                newContainerList.append(pair)
                containerList20.remove(containerList20[i+1])
                i += 1
        if containerList20:
            newContainerList.append(containerList20[len(containerList20)-1])
        
        ship[3] = newContainerList


# Loads the containers
def Ship_LoadContainer(ship, newContainer):
    while (ShipLock(ship) != True):
        break
    newContainerWeight = Container_GetTotalWeight(newContainer)
    newContainerLength = Container_GetLength(newContainer)
    loaded = False
    i = 0
    while i<Ship_GetNumberOfContainers(ship):
        container = Ship_GetNthContainer(ship, i)
        containerWeight = Container_GetTotalWeight(container)
        containerLength = Container_GetLength(container)
        if containerWeight<=newContainerWeight and containerLength<=newContainerLength:
            Ship_InsertContainer(ship, newContainer, i)
            loaded = True
            break
        i += 1
    if not loaded:
        Ship_AppendContainer(ship, newContainer)

# checks if the ship is empty
def Ship_IsEmpty(ship):
     return Ship_GetNumberOfContainers(ship)==0

# Pushes a container to the ship
def Ship_PushContainer(ship, container):
    containers = Ship_GetContainers(ship)
    containers.append(container)

# Pushes containers to ship
def Ship_PushContainers(ship, containers):
    while len(containers)!=0:
        container = containers.pop()
        Ship_PushContainer(ship, container)
    

# Pops the last container in the containers list
def Ship_PopContainer(ship):
     if Ship_GetNumberOfContainers(ship)==0:
         return
     containers = Ship_GetContainers(ship) #lista
     containers_dict = Ship_GetContainerDictionary(ship) #dicten
     containers.pop()
     #containers_dict[]

# Pops the lighter containers on the ship
def Ship_PopLighterContainers(ship, thresholdWeight):
    poppedContainers = []
    while not Ship_IsEmpty(ship):
        container = Ship_GetTopContainer(ship)
        totalWeight = Container_GetTotalWeight(container)
        if totalWeight>=thresholdWeight:
            break
        Ship_PopContainer(ship)
        poppedContainers.append(container)
    return poppedContainers

# Returns the last container in the list
def Ship_GetTopContainer(ship):
     if Ship_GetNumberOfContainers(ship)==0:
         return None
     containers = Ship_GetContainers(ship)
     return containers[-1]

# Piles the container on the ship
def Ship_PileContainer(ship, container):
    totalWeightContainer = Container_GetTotalWeight(container)
    poppedContainers = Ship_PopLighterContainers(ship, totalWeightContainer)
    Ship_PushContainer(ship, container)
    Ship_PushContainers(ship, poppedContainers)
    


# Calculating loads
# ------------
# Calculates total load from dictionary
def calculateLoadFromDict(dict):
    load = 0
    for key in dict:
        container = dict[key]
        if len(container) != 2:
            load += Container_GetTotalWeight(container)
        if len(container) == 2:
            load += Container_GetTotalWeight(container[0]) + Container_GetTotalWeight(container[1])
    return load

# Returns the total weight of all the containers on the starboard side of the ship
def LoadOfContainersStarboard(ship):
    dicten = Ship_GetContainerDictionary(ship)
    newdict = {}
    for x in range(0, int(Ship_GetWidth(ship)/2)):
        for y in range(0, int(Ship_GetLength(ship))):
            for z in range(0, int(Ship_GetHeight(ship))):
                if (dicten[(x,y,z)] != None):
                    newdict[(x,y,z)] = dicten[(x,y,z)]
    return calculateLoadFromDict(newdict)
    
# Returns the total weight of all the containers on the portside of the ship
def LoadOfContainersPortside(ship):
    newdict = {}
    dicten = Ship_GetContainerDictionary(ship)
    for x in range(int(Ship_GetWidth(ship)/2), int(Ship_GetWidth(ship))):
        for y in range(0, int(Ship_GetLength(ship))):
            for z in range(0, int(Ship_GetHeight(ship))):
                if dicten[(x,y,z)] != None:
                    newdict[(x,y,z)] = dicten[(x,y,z)]
    return calculateLoadFromDict(newdict)

# Returns the total weight of all the containers on the ship
def TotalLoadContainers(ship):
    return LoadOfContainersPortside(ship) + LoadOfContainersStarboard(ship)

def LoadOfContainersFront(ship):
    newdict = {}
    dicten = Ship_GetContainerDictionary(ship)
    for x in range(0, int(Ship_GetWidth(ship))):
        for y in range(0, int(Ship_GetLength(ship)/3)):
            for z in range(0, int(Ship_GetWidth(ship))):
                if dicten[(x,y,z)] != None:
                    newdict[(x,y,z)] = dicten[(x,y,z)]
    return calculateLoadFromDict(newdict)

# Returns the total weight of all the containers on the middle of the ship
def LoadOfContainersMiddle(ship):
    newdict = {}
    dicten = Ship_GetContainerDictionary(ship)
    for x in range(0, int(Ship_GetWidth(ship))):
        for y in range(int(Ship_GetLength(ship)/3), int(Ship_GetLength(ship)*2/3)):
            for z in range(0, int(Ship_GetWidth(ship))):
                if dicten[(x,y,z)] != None:
                    newdict[(x,y,z)] = dicten[(x,y,z)]
    return calculateLoadFromDict(newdict)

# Returns the total weight of all the containers on the rear of the ship
def LoadOfContainersRear(ship):
    newdict = {}
    dicten = Ship_GetContainerDictionary(ship)
    for x in range(0, int(Ship_GetWidth(ship))):
        for y in range(int(Ship_GetLength(ship)*2/3), int(Ship_GetLength(ship))):
            for z in range(0, int(Ship_GetWidth(ship))):
                if dicten[(x,y,z)] != None:
                    newdict[(x,y,z)] = dicten[(x,y,z)]
    return calculateLoadFromDict(newdict)


# Returns True id the ship is balanced
def ShipIsBalanced(precentageDiffStarPort, percentageDiffFrontRear, ship):
    balanced = False
    diffStarPort = abs(1 - (LoadOfContainersStarboard(ship)/LoadOfContainersPortside(ship)))
    diffFrontMiddle = abs(1- (LoadOfContainersFront(ship)/ LoadOfContainersMiddle(ship)))
    diffMiddleRear = abs(1 - (LoadOfContainersMiddle(ship)/ LoadOfContainersRear(ship)))
    diffFrontRear = abs(1 - (LoadOfContainersFront(ship)/ LoadOfContainersRear(ship)))
    if (diffStarPort*100 < precentageDiffStarPort):
        if (diffFrontMiddle*100 < percentageDiffFrontRear) and (diffFrontRear*100 < percentageDiffFrontRear) and (diffMiddleRear*100 < percentageDiffFrontRear):
            balanced = True
    else:
        balanced = False
    return balanced

    

    
# Read from and write to file
# ---------------------------
# Returns the information from the file, separates on the separator
def ReadContainersFromFile(filename, separator):
    file = open(filename, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        print(lines[i].split(separator))
    file.close()
    return lines

def LoadContainersFromFile(filename, separator):
    containerlist = []
    file = open(filename, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        containerlist.append(lines[i].split(separator))
    file.close()
    return containerlist

# Writes the information about the input ship to the file
def WriteShipToFile(filename, ship, separator):
    file = open(filename, "w")
    file.write("Length of ship: " + str(ship[0]) + "\n" + "Width of ship: " + str(ship[1]) + "\n" + "Height of ship: " + str(ship[2]) + 
    "\n" + "Number of containers: " + str(len(ship[3])) + "\n" + "List of containers: " + "\n")
    WriteContainersToFile(filename, ship, separator)
    file.close()

# Writes the information about the containers on the input ship to the file
def WriteContainersToFile(filename, ship, separator):
    file = open(filename, "w")
    for i in range(0, Ship_GetNumberOfContainers(ship)):
        line = ""
        for j in range(0, len(ship[3][i])):
            line += str(ship[3][i][j]) + str(separator)
        file.write(line[:-1] + "\n")
    file.close()

# Writes the information about the input container to the file
def WriteContainerToFile(filename, container, separator):
    file = open(filename, "w")
    line = ""
    for i in range(len(container)):
        line += str(container[i]) + str(separator)
    file.write(line[:-1] + "\n")
    file.close()

    

# Calculating loadtime
# ----------
# Returns the time it takes to load all the containers to the ship with one crane available
def LoadTimeOneCrane(ship):
    containers = Ship_GetNumberOfContainers(ship)
    resultstring = "It will take " + str(containers*4) + " minutes to unload the ship with one crane."
    return resultstring

# Returns the time it takes to load all the containers to the ship with four cranes available
def LoadTimeFourCranes(ship):
    dict = Ship_GetPositionOfContainers(ship)
    # 1 = foran, 4 = bak
    loadtime1 = 0
    loadtime2 = 0
    loadtime3 = 0
    loadtime4 = 0
    for key in dict.keys():
        if (len(dict[key])==4):
            if (0 <= key[1] < int(Ship_GetLength(ship)/4)):
                loadtime1 += 4
            if (int(Ship_GetLength(ship)/4) <= key[1] < int(Ship_GetLength(ship)/2)):
                loadtime2 += 4
            if (int(Ship_GetLength(ship)/2) <= key[1] < int(Ship_GetLength(ship)*3/4)):
                loadtime3 += 4
            if (int(Ship_GetLength(ship)*3/4) <= key[1] < int(Ship_GetLength(ship))):
                loadtime4 += 4
        else:
            if (0 <= key[1] < int(Ship_GetLength(ship)/4)):
                loadtime1 += 8
            if (int(Ship_GetLength(ship)/4) <= key[1] < int(Ship_GetLength(ship)/2)):
                loadtime2 += 8
            if (int(Ship_GetLength(ship)/2) <= key[1] < int(Ship_GetLength(ship)*3/4)):
                loadtime3 += 8
            if (int(Ship_GetLength(ship)*3/4) <= key[1] < int(Ship_GetLength(ship))):
                loadtime4 += 8
    newList = [loadtime1, loadtime2, loadtime3, loadtime4]
    resultstring = "It will take " + str(max(newList)) + " minutes to unload the ship with four cranes."
    return resultstring
    
        
    



# 5. Container Manager
# --------------------

ContainerManager_year = 2023
ContainerManager_month = 1
ContainerManager_day = 27
ContainerManager_number = 0

# Generates and returns a new serial number
def ContainerManager_NewSerialNumber():
    global ContainerManager_year
    global ContainerManager_month
    global ContainerManager_day
    global ContainerManager_number
    ContainerManager_number += 1
    serialNumber = "{0:d}-{1:02d}-{2:d}-{3:04d}".format( \
        ContainerManager_year, ContainerManager_month, ContainerManager_day, ContainerManager_number)
    return serialNumber

# Generates and returns a random container
def ContainerManager_NewRandomContainer():
    serialNumber = ContainerManager_NewSerialNumber()
    isSmall = random.randint(0, 1)
    if isSmall==0:
        cargo = random.randint(0, 20)
        container = Container_NewSmall(serialNumber, cargo)
    else:
        cargo = random.randint(0, 22)
        container = Container_NewBig(serialNumber, cargo)
    return container

# Generates and returns a random set of containers
def ContainerManager_NewRandomContainerSet(amount):
    containers = []
    for i in range(amount):
        containers.append(ContainerManager_NewRandomContainer())
    return containers

# Returns the information about the input ship in a more readable way
def toString(ship):
    result = ""

    length = int(ship[0])
    width = int(ship[1])
    height = int(ship[2])
    dict_ship = ship[4]

    ship_matrix = [[["-" for _ in range(height)] for _ in range(width)] for _ in range(length)]

    for key, value in dict_ship.items():
        if value is not None:
            x, y, z = key
            if value[1] == 20:
                id = "S" + value[0][-4:]
            elif value[1] == 40:
                id = "L" + value[0][-4:]
            else:
                continue
            ship_matrix[x][y][z] = id

    for i in range(length):
        result += f"Level {i + 1}\n"
        for j in range(width):
            row = ""
            for k in range(height):
                row += ship_matrix[i][j][k] + " "
            result += row + "\n"
        result += "\n"

    result += f"Ship (length={ship[0]*2}, width={ship[1]}, height={ship[2]})\n"
    result += "------------------------\n"
    result += f"Total volume: {ship[1]*ship[2]*ship[0]*2} cubic units\n"
    result += f"Current cargo: {len(ship[3])} items\n"
    if ship[5]:
        result += "Ship is currently docked\n"
    else:
        result += "Ship is currently at sea\n"
    result += "Starboard load: " + str(LoadOfContainersStarboard(ship)) + "\n"
    result += "Portside load: " + str(LoadOfContainersPortside(ship)) + "\n"
    result += "Front load: " + str(LoadOfContainersFront(ship)) + "\n"
    result += "Middle load: " + str(LoadOfContainersMiddle(ship)) + "\n"
    result += "Rear load: " + str(LoadOfContainersRear(ship)) + "\n"
    result += "Total load: " + str(TotalLoadContainers(ship)) + "\n"
    result += LoadTimeOneCrane(ship)+ "\n"
    result += LoadTimeFourCranes(ship)+ "\n"
    return result

# X. Main
# -------

ship = Ship_New(12, 6, 10)

for i in range(12*6*10):
    container = ContainerManager_NewRandomContainer()
    Ship_LoadContainer(ship, container)

ShipLock(ship)
print(toString(ship))


WriteShipToFile("containers.txt", ship, ";")
ReadContainersFromFile("containers.txt", ";")

#print(LoadContainersFromFile("containers.txt", ";"))











