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
    testData[6,1] = BLACK #lower
    testData[6,15] = BLACK
    testData[7,14] = BLACK # lower left
    testData[12,13] = BLACK
    testData[11,14] = BLACK #lower right
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
    testData[19,1] = BLACK
    testData[19,2] = BLACK
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
    testData[6,1] = BLACK #lower left
    testData[6,14] = BLACK
    testData[5,13] = BLACK#upper left
    testData[12,13] = BLACK
    testData[12,11] = BLACK#left
    testData[19,1] = BLACK
    testData[19,2] = BLACK
    answer = Characteristics.checkCharThirteen(testData)

    if(answer == 1): return 1
    else: return 0

#Number of black pixels with no neighbours in the upper-right, right, or lower-right positions
def testCharFourteen():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[5,2] = BLACK
    testData[4,3] = BLACK #upper right
    testData[6,14] = BLACK
    testData[6,15] = BLACK #right
    testData[12,13] = BLACK
    testData[12,14] = BLACK#lower-right
    testData[6,15] = BLACK
    testData[6,14] = BLACK #left

    answer = Characteristics.checkCharFourteen(testData)

    if(answer == 1): return 1
    else: return 0

#Two black pixels A and B are connected if they are neighbours of each other, or if a black pixel neighbour of A is connected to B (this definition is actually symmetric); a connected region is a maximal set of black pixels
#which are connected to each other; this feature has the number of connected regions in the image
def testCharFifteen ():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[10,12] = BLACK
    testData[10,13] = BLACK
    testData[10,14] = BLACK
    answer = Characteristics.checkCharFifteen(testData)

    if(answer == 1): return 1
    else: return 0

#In a written character, an “eye” is a region of whitespace that is completely surrounded by lines of the character. For example, “A” contains one eye, “B” contains two eyes, and “C” contains no eyes. A
#region of whitespace is an eye if there is a ring of black pixels surrounding it which are all connected (i.e. they form a chain of neighbours). This
#feature is the number of eyes in the image.
def testCharSixteen ():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[10,12] = BLACK
    testData[10,13] = BLACK
    testData[10,14] = BLACK
    testData[11,12] = BLACK
    testData[11,14] = BLACK
    testData[12,12] = BLACK
    testData[12,13] = BLACK
    testData[12,14] = BLACK
    answer = Characteristics.checkCharSixteen(testData)

    if(answer == 1): return 1
    else: return 0
#Number of rows with at least five black pixels) minus (number of columns with at least five black pixels.
def testCharSeventeen():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[0,1] = BLACK
    testData[0,2] = BLACK
    testData[0,3] = BLACK
    testData[0,4] = BLACK
    testData[0,5] = BLACK

    testData[12,1] = BLACK
    testData[12,2] = BLACK
    testData[12,3] = BLACK
    testData[12,4] = BLACK
    testData[12,5] = BLACK

    answer = Characteristics.checkCharSeventeen(testData)
    if(answer == 0): return 1
    else: return 0

def testCharEighssteen():
    testData = [[]]
    for i in range(1,20):
        for j in range(1,20):
            testData[i,j] = WHITE

    testData[10,12] = BLACK
    testData[10,13] = BLACK
    testData[10,14] = BLACK
    testData[11,12] = BLACK
    testData[11,14] = BLACK
    testData[12,12] = BLACK
    testData[12,13] = BLACK
    testData[12,14] = BLACK

