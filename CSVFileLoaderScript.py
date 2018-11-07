import csv

FILE_SIZE = 403

def main():
	directory = "40150865_37_2.pgm"
	new_file = open(directory, "r")

	#setting up writeable datafile
	data = []
	data = new_file.read().replace("\n", ",")

	#remove waste
	if "P2,# Created by GIMP version 2.10.6 PNM plug-in," in data:
		data = data.replace("P2,# Created by GIMP version 2.10.6 PNM plug-in,", "")
	elif "P2,# Created by GIMP version 2.10.0 PNM plug-in," in data:
		data = data.replace("P2,# Created by GIMP version 2.10.0 PNM plug-in,", "")

	data = data.replace("20 20","").split(",")
	print (data)
 	#append new row to csv file
	with open("new_yeet.csv","wb") as CSV_file:
		csv_file_string = ""
		data_indx = 1;
		new_row = []
		for item in data:
			if(item!= ''):
				if(int(item)>= 128):  item = "1"
				else: item = "0"

				csv_file_string+=item
				if(((data_indx+1) %20 == 0)):
					csv_file_string += (item + "\n")
				else:
					csv_file_string += item

			data_indx += 1

		CSV_file.write(bytes(csv_file_string, 'utf-8'))

	new_file.close()


main();
