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
	parser.add_argument( '--output_id', dest='output_id')
	parser.add_argument( '--new_file_path', dest='new_file_path')
        parser.add_argument( '--split_number', dest='split_number')
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


	# ecriture dans x fichiers selon le nombre de ligne max en entree (utilisation de list.pop([i])
	tabgene.reverse()
	file_num=0

	# tant que longueur du tableau strictement superieur au nombre de ligne
	while len(tabgene) > int(options.split_number):
		file_num+=1
		# creation du fichier extra dans new_file_path
		output_extra_file=open(options.new_file_path+"/primary_"+options.output_id+"_splitfile"+str(file_num)+"_visible_txt", "w")
		for i in range(int(options.split_number)):
			output_extra_file.write(tabgene.pop())
		output_extra_file.close()

	# completer le reste
	file_num+=1

        # creation du fichier extra dans new_file_path
        output_extra_file=open(options.new_file_path+"/primary_"+options.output_id+"_splitfile"+str(file_num)+"_visible_txt", "w")
	tabgene.reverse()
	for gene in tabgene:
		output_extra_file.write(gene)
	output_extra_file.close()

	# fermeture fichier de log					
        outputfile.close()


if __name__ == "__main__": __main__()
