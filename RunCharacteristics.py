import Characteristics
import Ciarans
import os
import csv
import Characteristics
csvFiles = []

def collectFiles():
    directory = os.fsencode(os.path.dirname(os.path.realpath(__file__)))
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv") and filename != "40150865_features.csv":
            csvFiles.append(file)

    print(csvFiles)

def fileToArray(file):
    #defining image
    rows = 20
    cols = 20
    newImage = [[0 for j in range(cols)] for i in range(rows)]
    oldImage = [[]]
    with open(file, 'r') as fileData:
        oldImage = fileData.read().replace(',','')

    counter = 0
    for i in range(20):
       for j in range(20):
            if(oldImage[counter] != '\n'):
                newImage[i][j] = oldImage[counter]
                counter +=1
            else:
                counter +=1
                newImage[i][j] = oldImage[counter]
                counter +=1


    return newImage


def main():
    print("Gathering data...")
    Ciarans.gatherData()
    print("Collecting files...")
    collectFiles()

    myFile = open('40150865_features.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        for file in csvFiles:
            newRow = []
            for i in range(20): newRow.append(0)

            image = fileToArray(file)

            newRow[0] = str(Characteristics.checkCharOne(image)) + "\n"
            newRow[1] = str(Characteristics.checkCharTwo(image)) + "\n"
            newRow[2] = str(Characteristics.checkCharThree(image)) + "\n"
            newRow[3] = str(Characteristics.checkCharFour(image)) + "\n"
            newRow[4] = str(Characteristics.checkCharFive(image)) + "\n"
            newRow[5] = str(Characteristics.checkCharSix(image)) + "\n"
            newRow[6] = str(Characteristics.checkCharSeven(image)) + "\n"
            newRow[7] = str(Characteristics.checkCharEight(image)) + "\n"
            newRow[8] = str(Characteristics.checkCharNine(image)) + "\n"
            newRow[9] = str(Characteristics.checkCharTen(image)) + "\n"
            newRow[10] = str(Characteristics.checkCharEleven(image)) + "\n"
            print("Characteristics done.")

            writer.writerow(newRow)

    print("Finsihed.")
    myFile.close()

main()
