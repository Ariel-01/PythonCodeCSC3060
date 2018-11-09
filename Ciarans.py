import os
import sys
import csv

directory = os.fsencode(os.path.dirname(os.path.realpath(__file__)))

def gatherData():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".pgm"):
            with open(filename, 'r') as fileData:
                data = fileData.read().replace('\n', ',')
                if "P2,# Created by GIMP version 2.10.6 PNM plug-in," in data:
                    data = data.replace("P2,# Created by GIMP version 2.10.6 PNM plug-in,", "")
                elif "P2,# Created by GIMP version 2.10.0 PNM plug-in," in data:
                    data = data.replace("P2,# Created by GIMP version 2.10.0 PNM plug-in,", "")
                newFile = ""
                dataList = data.replace("20 20,", "").split(",")
                i = 0
                x = 0
                y = len(dataList)
                for pixel in dataList:
                    newPixel = "1"
                    if pixel != "":
                        if int(pixel) >= 128:
                            newPixel = "0"
                        elif int(pixel) < 128:
                            newPixel = "1"

                        if i == 19:
                            x += 1
                            if i == 19 and x == 20:
                                i = 0
                                newFile += newPixel
                                break
                            else:
                                i = 0
                                newFile += newPixel + "\n"
                        else:
                            i += 1
                            newFile += newPixel + ","
                with open(filename.replace('.pgm', '.csv'),'wb') as csvFile:
                    csvFile.write(bytes(newFile, 'utf-8'))
                continue
            continue
        else:
            continue

