import sys, tempfile, subprocess, glob
import os, re, shutil
import argparse
from os.path import basename

"""

Created by Cyril Monjeaud
Cyril.Monjeaud@irisa.fr


"""

def __main__():

        # retrieve arguments
	parser = argparse.ArgumentParser()
        parser.add_argument( '--list_file', dest='list_file' )
        parser.add_argument( '--type', dest='type' )
        parser.add_argument( '--output', dest='output')
        options = parser.parse_args()

	# fichier log
        outputfile=open(options.output, "w")

	# lecture de la liste des genes
	tabgene=[]
	files=options.list_file.split(",")
	for file in files:
		# ajout des genes dans un tableau
		genefile=open(file.strip(), "r")
		outputfile.write(file.strip()+"\n")
		for gene in genefile:
			tabgene.append(gene)
		genefile.close()

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
