#!/bin/python

import sys,os

# store inputs in an array
inputs = sys.argv[1].split(",")

# defined formats list
format_list = ["jpg", "tiff", "bmp", "pdf"]

# create the output dir
os.mkdir("convert")

# for each image
for image in inputs:
	
	# create the output basename from the dataset name
	basename = os.path.basename(image)
	basename_without_ext = os.path.splitext(basename)[0]

	# for each format, convert the image
	for format in format_list:
		# edit the command line
		cmd = "convert "+image+" convert/"+basename_without_ext+"."+format
		# print in a log file
		print cmd+"\n"
		os.system(cmd)		

