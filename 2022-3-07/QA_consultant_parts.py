from datetime import datetime
import re
import csv

date = (datetime.now()).strftime("%Y_%m_%d")

field_name=['URL','Catalogue price','Net price','Brand,Part number','Date','Time','Stock','Website','Ref_no_space','Description']
file = input('Enter the input file :')
with open(file, 'r') as myfile:
		file_data = myfile.read()
		if 'null' in file_data:
			lines = file_data.split('\n')
		for line_number, line in enumerate(lines):
			error = ''
		val=input("wheather to check total number of lines :(yes/No)?")
		if val=="yes":
				print(line_number)

		lower=int(input("enter the  upperlimit :"))
		upper=int(input("enter the  lowerlimit :"))

		if lower<=line_number+1<=upper:
			print("line number matched")
    
		else:
			print("count unmatched")





