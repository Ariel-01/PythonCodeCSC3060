import os
import Ciarans
BLACK = '1'
WHITE = '0'
MAX_ROWS = 20


# num 1, amount of black pixels
def checkCharOne(image):
    numBlack = 0
    for i in range(20):
        for j in range(20):
            if (image[i][j] == BLACK):
                numBlack += 1

    return numBlack


# num 2, number of rows containing one black pixel
def checkCharTwo(image):
    rowBlack = 0
    rowCounter = 0
    while (rowCounter < MAX_ROWS):
        for j in range(1, 20):
            if (image[rowCounter][j] == BLACK):
                rowBlack += 1
                break  # does break work like this in python?
        rowCounter += 1

    return rowBlack


# 3, number of columns containing at least one black pixel
def checkCharThree(image):
    colBlack = 0
    colCounter = 0
    while (colCounter < MAX_ROWS):
        for j in range(1, 20):
            if (image[j][colCounter] == BLACK):
                colBlack += 1
                break  # does break work like this in python?

        colCounter += 1

    return colBlack


# 4, ratio of height to width ft2/ft3
def checkCharFour(height, width):
    return (height / width)


# 5, the number of rows with exactly one black pixel
def checkCharFive(image):
    rowBlack = 0
    rowCounter = 0

    while (rowCounter < MAX_ROWS):
        blackCount = 0
        for j in range(1, 20):
            if (image[rowCounter][ j] == BLACK):
                blackCount += 1

        if (blackCount == 1): rowBlack += 1
        rowCounter += 1

    return rowBlack


# 6, the number of colums with exactly one black pixel
def checkCharSix(image):
    colBlack = 0
    colCounter = 0

    while (colCounter < MAX_ROWS):
        blackCount = 0
        for j in range(1, 20):
            if (image[j][ colCounter] == BLACK):
                blackCount += 1

        if (blackCount == 1): colBlack += 1
        colCounter += 1

    return colBlack


# 7,  number of rows with five or more black pixels
def checkCharSeven(image):
    rowBlack = 0
    rowCounter = 0

    while (rowCounter < MAX_ROWS):
        blackCount = 0
        for j in range(1, 20):
            if (image[rowCounter][j] == BLACK):
                blackCount += 1

        if (blackCount == 5): rowBlack += 1
        rowCounter += 1

    return rowBlack


# 8, number of columns with fiver or more black pixels
def checkCharEight(image):
    colBlack = 0
    colCounter = 0

    while (colCounter < MAX_ROWS):
        blackCount = 0
        for j in range(1, 20):
            if (image[j][colCounter] == BLACK):
                blackCount += 1

        if (blackCount == 5): colBlack += 1
        colBlack += 1

    return colBlack


# 9, number of black pixels with exactly one neighbouring pixel
def checkCharNine(image):
    noNeigh = 0
    for i in range(1, 20):
        for j in range(1, 20):
            hasBlack = False
            if (image[i][ j] == BLACK):
                if (j < 20):  # right section
                    if (image[i][(j + 1)] == BLACK):  # right
                        hasBlack = True
                        break
                    elif (i < 20):
                        if (image[(i + 1)][(j + 1)] == BLACK):  # upper right
                            hasBlack = True
                            break
                    elif (i > 1 == BLACK):
                        if (image[(i - 1)][ (j + 1)]):  # lower right
                            hasBlack = True
                            break
                if (j > 1):  # left section
                    if (image[i][(j - 1)] == BLACK):  # left
                        hasBlack = True
                        break
                    elif (i < 20 == BLACK):  # upper left
                        if (image[(i + 1)][ (j - 1)] == BLACK):
                            hasBlack = True
                            break
                    elif (i > 1) == BLACK:  # lower left
                        if (image[(i - 1)][ (j - 1)]):
                            hasBlack = True
                            break
                if (image[(i + 1), j] == BLACK):  # up
                    hasBlack = True
                    break
                if (image[(i - 1), j] == BLACK):  # down
                    hasBlack = True
                    break
            else:
                continue

            if (hasBlack): noNeigh += 1

    return noNeigh


# 10, number of black pixels with three or more neighbouring pixel
def checkCharTen(image):
    noNeigh = 0
    for i in range(1, 20):
        for j in range(1, 20):
            noBlack = 0
            if (image[i, j] == BLACK):
                if (j < 20):  # right section
                    if (image[i, (j + 1)] == BLACK):  # right
                        noBlack += 1
                        break
                    elif (i < 20):
                        if (image[(i + 1), (j + 1)] == BLACK):  # upper right
                            noBlack += 1
                            break
                    elif (i > 1):
                        if (image[(i - 1), (j + 1)] == BLACK):  # lower right
                            noBlack += 1
                            break
                if (j > 1):  # left section
                    if (image[i, (j - 1)] == BLACK):  # left
                        noBlack += 1
                        break
                    elif (i < 20):  # upper left
                        if (image[(i + 1), (j - 1)] == BLACK):
                            noBlack += 1
                            break
                    elif (i > 1 == BLACK):  # lower left
                        if (image[(i - 1), (j - 1)]):
                            noBlack += 1
                            break
                if (image[(i + 1), j] == BLACK):  # up
                    noBlack += 1
                    break
                if (image[(i - 1), j] == BLACK):  # down
                    noBlack += 1
                    break
            else:
                continue

            if (noBlack >= 3): noNeigh += 1

    return noNeigh


# 11, number of black pixels with no neighbours in the lower left or right positions(F)
def checkCharEleven(image):
    noNeigh = 0
    continueLoop = False
    for i in range(1, 20):
        for j in range(1, 20):
            if (image[i][j] == BLACK):
                if (j < 20):  # right section
                    if (i > 1):
                        if (image[(i - 1)][(j + 1)] != BLACK):  # lower right
                            continueLoop = True
                            break
                if(i > 1):
                    if (image[(i - 1)][ j] != BLACK):  # down
                        continueLoop = True
                        break
                if (j > 1):  # left section
                    if (i > 1):  # lower left
                        if (image[(i - 1)][ (j - 1)]):
                            continueLoop = True
                            break
        if(continueLoop): noNeigh +=1

    return noNeigh

#12, number of black pixels with no neighbours in the upper left, upper or upper right positions
def checkCharTwelve(image):
    noNeigh = 0
    continueLoop = False
    for i in range(1, 20):
        for j in range(1, 20):
            if (image[i][ j] == BLACK):
                if (j < 20):  # right section
                    if (i > 1):
                        if (image[(i - 1)][ (j + 1)] != BLACK):  # lower left
                            continueLoop = True
                            break
                if(i < 20):
                    if (image[(i + 1)][j] != BLACK):  # up
                        continueLoop = True
                        break
                if (j > 20):
                    if (i > 20):  # upper right
                        if (image[(i + 1)][ (j + 1)]):
                            continueLoop = True
                            break
        if(continueLoop): noNeigh +=1

    return noNeigh

#13, Number of black pixels with no neighbours in the upper left,left or lower left positions
def checkCharThirteen(image):
    noNeigh = 0
    continueLoop = False
    for i in range(1, 20):
        for j in range(1, 20):
            if (image[i][ j] == BLACK):
                if (j < 20):  # right section
                    if (i > 1):
                        if (image[(i + 1)][ (j - 1)] != BLACK):  # upper left
                            continueLoop = True
                            break
                if(j > 1):
                    if (image[i][ (j - 1)] != BLACK):  # left
                        continueLoop = True
                        break
                if (j > 1):
                    if (i > 1):  # lower left
                        if (image[(i - 1)][ (j - 1)]):
                            continueLoop = True
                            break
        if(continueLoop): noNeigh +=1

    return noNeigh

#14, Number of black pixels with no neighbours in the upper right, right or lower right postions
def checkCharFourteen(image):
    noNeigh = 0
    continueLoop = False
    for i in range(1, 20):
        for j in range(1, 20):
            if (image[i][ j] == BLACK):
                if (j < 20):  # right section
                    if (i > 1):
                        if (image[(i + 1)][ (j + 1)] != BLACK):  # upper right
                            continueLoop = True
                            break
                if(j > 1):
                    if (image[i][ (j + 1)] != BLACK):  # right
                        continueLoop = True
                        break
                if (j > 20):
                    if (i > 20):  # lower right
                        if (image[(i - 1)][ (j +1)]):
                            continueLoop = True
                            break
        if(continueLoop): noNeigh +=1

    return noNeigh

#15,Two black pixels A and B are connected if they are neighbours of each other, or if a black pixel neighbour of A is connected to B (this definition is actually symmetric); a connected region is a maximal set of black pixels
#  which are connected to each other; this feature has the number of connected regions in the image.

#a class which stores all of the members
def connectedManager():
    edgesInRegion = [];

    def checkEdge(edge):
        for i in range (1,len(edgesInRegion)):
            if(edge == i):
                return True

        return False

    def add(edge):
        isPresent = checkEdge(edge)
        if(isPresent == False): edgesInRegion.append(edge)


manager = connectedManager()

def checkConnected(image, row, col, parent):
    hasConnections = 0

    if(parent[0] == -1): #if this is the first black pixel in the graph
        if(row < 20):
            if(image[row + 1][col] == BLACK):hasConnections+=1
        if(row > 1):
            if(image[row - 1][ col] == BLACK): hasConnections+=1
        if(col > 1):
            if(image[row][ col - 1] == BLACK): hasConnections+=1
        if(col < 20):
            if(image[row][col + 1] == BLACK): hasConnections+=1
        if(col > 1 and row > 1):
            if(image[row - 1][ col - 1] == BLACK): hasConnections+=1
        if(col < 20 and row > 1):
            if(image[row - 1][ col + 1] == BLACK): hasConnections+=1
        if(col < 20 and row < 20):
            if(image[row + 1][ col + 1] == BLACK): hasConnections+=1
        if(col > 1 and row < 20):
            if(image[row + 1][ col - 1] == BLACK): hasConnections+=1
    else:
        if(row < 20 and (row + 1, col) != parent):
            if(image[row + 1][col] == BLACK):hasConnections+=1
        if(row > 1 and (row - 1, col) != parent):
            if(image[row - 1][ col] == BLACK): hasConnections+=1
        if(col > 1 and (row, col - 1) != parent):
            if(image[row][ col - 1] == BLACK): hasConnections+=1
        if(col < 20 and (row, col + 1) != parent):
            if(image[row][col + 1] == BLACK): hasConnections+=1
        if(col > 1 and row > 1 and (row - 1, col -1) != parent):
            if(image[row - 1][ col - 1] == BLACK): hasConnections+=1
        if(col < 20 and row > 1 and  (row - 1, col +1) != parent):
            if(image[row - 1][ col + 1] == BLACK): hasConnections+=1
        if(col < 20 and row < 20 and  (row + 1, col +1) != parent):
            if(image[row + 1][ col + 1] == BLACK): hasConnections+=1
        if(col > 1 and row < 20 and   (row + 1, col - 1) != parent):
            if(image[row + 1][ col - 1] == BLACK): hasConnections+=1


    return hasConnections

def getNeighbours(image, row, col):
    connections = []
    if(row < 20):
        if(image[row + 1][col] == BLACK):
            connections.append((row + 1,col))
        if(row > 1):
            if(image[row - 1][col] == BLACK):
                connections.append((row - 1,col))
        if(col > 1):
            if(image[row][col - 1] == BLACK):
                connections.append((row ,col- 1))
        if(col < 20):
            if(image[row][col + 1] == BLACK):
                 connections.append((row ,col+ 1))
        if(col > 1 and row > 1):
            if(image[row - 1][ col - 1] == BLACK):
                connections.append((row - 1,col - 1))
        if(col < 20 and row > 1):
            if(image[row - 1][ col + 1] == BLACK):
                connections.append((row - 1,col + 1))
        if(col < 20 and row < 20):
            if(image[row + 1][ col + 1] == BLACK):
                connections.append((row + 1,col + 1))
        if(col > 1 and row < 20):
            if(image[row + 1][col - 1] == BLACK):
                connections.append((row + 1,col - 1))

    return connections

def checkingConnections(image, stRow, stCol):
    neighbours = getNeighbours(image, stRow,stCol)
    for k in range(1,len(neighbours)):
        if(manager.checkEdge[neighbours[k]] == False): manager.add(neighbours[k])
        connections = (checkConnected(image,neighbours[k][0],neighbours[k][1],(stRow,stCol)))
        if(connections > 0): checkingConnections(image,neighbours[k][0],neighbours[k][1])


def checkCharFifteen(image):
    #figuring out connected
    noConnected = 0
    manager = connectedManager()
    for i in range(1,20):
        for j in range(1,20):
            numConnections = checkConnected(image,i,j,(-1,-1))
            if(numConnections == 0): continue; #no connections
            else:
                if(manager.checkEdge((i,j)) == True): continue;
                else: manager.add((i,j))
                checkingConnections(image,i,j)

    noConnected = len(manager)
    return noConnected

#checking if there's an eye
def eyeCheck(image, currentRow, currentCol, ignoreFlag):
    eyes = []

    #check left
    if(ignoreFlag != 'l' and currentCol > 1 ):
        if(image[currentRow, currentCol - 1] == WHITE):
            eyes.append((currentRow, (currentCol - 1)))
            addition = eyeCheck(image,currentRow, currentCol-1,'r')
            if(len(addition) > 0): eyes.append(addition)

    #check right
    if(ignoreFlag != 'r' and currentCol < 20 ):
        if(image[currentRow, currentCol + 1] == WHITE):
            eyes.append((currentRow, (currentCol + 1)))
            addition = eyeCheck(image,currentRow, currentCol+1,'l')
            if(len(addition) > 0): eyes.append(addition)

    #check up
    if(ignoreFlag != 'u' and currentRow < 20):
        if(image[currentRow+1,currentCol] == WHITE):
            eyes.append((currentRow+1,currentCol))
            addition = eyeCheck(image,currentRow+1, currentCol,'d')
            if(len(addition) > 0): eyes.append(addition)

    #check down
    if(ignoreFlag != 'd' and currentRow < 20):
        if(image[currentRow-1,currentCol] == WHITE):
            eyes.append((currentRow+1,currentCol))
            addition = eyeCheck(image,currentRow+1, currentCol,'u')
            if(len(addition) > 0): eyes.append(addition)

    return eyes

def alreadyThere(currentList, addition):
    for i in currentList:
        for j in addition:
            if(i == j): return False

    return True

#16, detecting eye
def checkCharSixteen(image):
    numEyes = 0
    pixelsInEye = []
    for i in range(1,20):
        for j in range(1,20):
            addition = eyeCheck(i,j,image)
            ans = alreadyThere(numEyes, pixelsInEye)
            if(ans): pixelsInEye.append(addition)


#17, num 5 black rows - num 5 black cols
def checkCharSeventeen(image):
    return (checkCharSeven(image) - checkCharEight(image))

def findLine(image):
    #to check for lines I check columns
    line = []
    for col in range(1,20):
        for row in range(1,20):
            if(image[row][col] == BLACK):
                if(col > 1 and col < 20):
                    if(image[row][col-1] == WHITE and image[row][col+1] == WHITE): line.append((row,col))
                if(col == 1):
                    if(image[row][col+1] == WHITE):line.append((row,col))
                if(col == 20):
                    if(image[row][col - 1] == WHITE): line.append((row,col))

            if(len(line) > 0): return line

    print("No line present")
    return line

#18, BD distingush
def checkCharEighteen(image):
    #find eye
    eye = []
    for i in range(1,20):
        for j in range(1,20):
            eye = eyeCheck(image,i,j,'N')
            if(len(eye) != 0 ): break

    if(len(eye) == 0):
        print("this isn't a b or d")
        return;

    line = findLine(image)

    for i in line:
        for j in eye:
            if(i == j):
                #this is where line ends and eye starts
                #check to the right of the circle
                if(eye[j+1] > i): return 'b'
                else: return 'd'

    return 'failed'

def main():
    print("tities")
