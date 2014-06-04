import csv
import json
import sys

fieldnames =["Tennis Lessons","Stroke","Comments"]

def convert(file):
	# Get the CSV filename and open the file
	filename = file[0]
	print "Reading File: " ,filename
	with open(filename, 'rU') as f:
		reader = csv.reader(f, dialect=csv.excel)
		csv_reader = csv.DictReader(f,fieldnames)
		
	# JSON
		json_filename = filename.split(".")[0]+".json"
		with open(json_filename, 'wb') as jsonf:
			data = json.dumps([r for r in csv_reader])
			jsonf.write(data)
	
	# Close files
			f.close()
			jsonf.close()
	print "Save JSON file: ", json_filename
	
if __name__=="__main__":
	convert(sys.argv[1:])
	
