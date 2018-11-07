import Characteristics

BLACK = 1
WHITE = 0

#checking the number of black pixels
def testCharOne():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    answer = Characteristics.checkCharOne(testData)

    if(answer == 1): return  1
    else: return 0

#checking number rows with black pixels
def testCharTwo():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[1,1] = BLACK
    testData[3,1] = BLACK
    answer = Characteristics.checkCharTwo(testData)

    if(answer == 3): return 1
    else: return 0

#checking the number of columns with a black pixel
def testCharThree():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[1,2] = BLACK
    testData[3,3] = BLACK
    answer = Characteristics.checkCharThree(testData)

    if(answer == 3): return 1
    else: return 0

#the ratio of pixels to columns
def testCharFour():
    #rows
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[1,1] = BLACK
    testData[3,1] = BLACK
    answerRows = Characteristics.checkCharTwo(testData)

    #cols
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[1,2] = BLACK
    testData[3,3] = BLACK
    answerCols = Characteristics.checkCharThree(testData)

    answer = Characteristics.checkCharFour(answerRows,answerCols)
    if(answer == 1): return 1
    else: return 0

#Number of rows with exactly one black pixe
def testCharFive():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[0,2] = BLACK
    testData[3,3] = BLACK
    answer = Characteristics.checkCharFive(testData)

    if(answer == 1) : return 1
    else: return 0

#Number of columns with exactly one black pixel
def testCharSix():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[0,1] = BLACK
    testData[3,3] = BLACK
    answer = Characteristics.checkCharSix(testData)

    if(answer == 1): return 0
    else: return 1

#Number of rows with five or more black pixels
def testCharSeven():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[0,2] = BLACK
    testData[0,3] = BLACK
    testData[0,4] = BLACK
    testData[0,5] = BLACK
    testData[1,5] = BLACK
    testData[2,5] = BLACK
    answer = Characteristics.checkCharSeven(testData)

    if(answer == 5): return 1
    else: return 0

#Number of columns with five or more black pixels
def testCharEight():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[1,1] = BLACK
    testData[1,2] = BLACK
    testData[1,3] = BLACK
    testData[1,4] = BLACK
    testData[1,5] = BLACK
    testData[3,5] = BLACK
    testData[2,5] = BLACK
    answer = Characteristics.checkCharEight(testData)

    if(answer == 5): return 1
    else: return 0

#Number of black pixels with exactly 1 neighbouring pixe
def testCharNine():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[1,1] = BLACK
    testData[1,2] = BLACK
    testData[3,10] = BLACK
    testData[4,10] = BLACK
    answer = Characteristics.checkCharNine(testData)

    if(answer == 2): return 1
    else: return 0

#Number of black pixels with 3 or more neighbours
def testCharTen():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[2,2] = BLACK
    testData[2,1] = BLACK
    testData[2,3] = BLACK
    testData[1,2] = BLACK
    answer = Characteristics.checkCharTen(testData)

    if(answer == 1): return 1
    else: return 0

#Number of black pixels with no neighbours in the lower-left, lower, or lower-right positions
def testCharEleven():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[5,2] = BLACK
    testData[6,1] = BLACK #left
    testData[6,15] = BLACK
    testData[7,14] = BLACK # lower left
    testData[12,13] = BLACK
    testData[11,12] = BLACK
    testData[17,10] = BLACK
    testData[17,11] = BLACK
    answer = Characteristics.checkCharEleven(testData)

    if(answer == 1): return 1
    else: return 0

#Number of black pixels with no neighbours in the upper-left, upper, or upper-right positions
def testCharTwelve():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[5,2] = BLACK
    testData[4,2] = BLACK #upper
    testData[6,14] = BLACK
    testData[5,15] = BLACK#upper right
    testData[12,13] = BLACK
    testData[11,12] = BLACK#upper left
    answer = Characteristics.checkCharTwelve(testData)

    if(answer == 1): return 1
    else: return 0

#Number of black pixels with no neighbours in the upper-left, left, or lower-left positions
def testCharThirteen():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[5,2] = BLACK
    testData[4,2] = BLACK #upper
    testData[6,14] = BLACK
    testData[5,15] = BLACK#upper right
    testData[12,13] = BLACK
    testData[11,12] = BLACK#upper left
    answer = Characteristics.checkCharThirteen(testData)

    if(answer == 1): return 1
    else: return 0



