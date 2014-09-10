import sys, tempfile, subprocess, glob
import os, re, shutil
import argparse
from os.path import basename

"""

Created by Cyril Monjeaud
Cyril.Monjeaud@irisa.fr

Last modifications : 12/05/2013

"""

def __main__():

        # retrieve arguments
	parser = argparse.ArgumentParser()
        parser.add_argument( '--file', dest='file' )
        parser.add_argument( '--type', dest='type' )
        parser.add_argument( '--addgene', dest='addgene')
        parser.add_argument( '--output', dest='output')
        options = parser.parse_args()

	# ajout des genes dans un tableau
	genefile=open(options.file, "r")
	tabgene=[]
	for gene in genefile:
		tabgene.append(gene)
	genefile.close()

	if options.addgene != "None":
		tabgene.append(options.addgene+"\n")

	# tri du tableau
	if options.type == "ascend":
		tabgene.sort()
	else:
		tabgene.sort(reverse=True)

	#ecriture dans fichier output
	outputfile=open(options.output, "w")
	for gene in tabgene:
		outputfile.write(gene)
	outputfile.close()
				

if __name__ == "__main__": __main__()
