#!/bin/python

import sys,os,optparse



def extract_basename(input_path):

	basename = os.path.basename(input_path)
        return os.path.splitext(basename)[0]


# store inputs in an array
parser = optparse.OptionParser()
parser.add_option("--choice", dest="choice")
parser.add_option("--image", dest="image")
parser.add_option("--images", dest="images")
parser.add_option("--size", dest="size")
parser.add_option("--angle", dest="angle")
parser.add_option("--pdf", action="store_true", dest="pdf")
parser.add_option("--jpg", action="store_true", dest="jpg")
parser.add_option("--tiff", action="store_true", dest="tiff")
parser.add_option("--output", dest="output")

(options, args) = parser.parse_args()

# create the output dir
os.mkdir("result")

# create the log file
logfile= open(options.output, "w")

if options.choice == "resize":
	output = extract_basename(options.image)+".png"
	cmd="convert "+options.image+" -resize "+options.size+"% result/"+output
	logfile.write("cmd = "+cmd+"\n")

	# execute cmd
	os.system(cmd)


elif options.choice == "rotate":
	output = extract_basename(options.image)+".png"
	cmd="convert "+options.image+" -rotate "+options.angle+" result/"+output
	logfile.write("cmd = "+cmd+"\n")

	# execute cmd
	os.system(cmd)


elif options.choice == "append":
	
	images=" ".join(options.images.split(","))
	output = "image_append.png"
	cmd="convert -append "+images+" result/"+output
	logfile.write("cmd = "+cmd+"\n")

	# execute cmd
	os.system(cmd)

else:
	if options.pdf:
		output = extract_basename(options.image)+".pdf"
		cmd="convert "+options.image+" result/"+output
		logfile.write("cmd = "+cmd+"\n")

		# execute cmd
		os.system(cmd)

	if options.jpg:
		output = extract_basename(options.image)+".jpg"
		cmd="convert "+options.image+" result/"+output
		logfile.write("cmd = "+cmd+"\n")

		# execute cmd
                os.system(cmd)
	

	if options.tiff:
		output = extract_basename(options.image)+".tiff"
		cmd="convert "+options.image+" result/"+output	
		logfile.write("cmd = "+cmd+"\n")

		# execute cmd
                os.system(cmd)


# close logfile
logfile.close()
