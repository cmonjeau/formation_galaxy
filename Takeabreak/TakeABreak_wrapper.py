import sys, tempfile, subprocess, glob
import os, re, shutil
import optparse
from os.path import basename

"""

Created by Cyril Monjeaud
Cyril.Monjeaud@irisa.fr

WARNING :

TakeABreak_wrapper.py needs:

- dbgh5 & TakeABreak binaries in your $PATH
- an additional script (dependencies_dir) composed by :
                - TakeABreak.sh

All these files are available after compiling the sources of TakeABreak :

https://colibread.inria.fr/files/2014/01/TakeABreak-1.0.6-Source.tar_.gz

or with the galaxy_takeabreak dependency package in the toolshed

"""

def __main__():

	### CHANGE THIS VARIABLE WITH YOUR OWN DIRECTORY IF YOU ARE NOT USING THE TOOLSHED DEPENDENCIES###
        dependencies_dir=os.environ['INSTALL_DIR']

	# create a special dir inside job working dir
        tmp_dir = tempfile.mkdtemp()
        os.chdir(tmp_dir)

	# create an alternative TakeABreak.sh file
        run_script=open("TakeABreak.sh", "w")
        template_script=open(dependencies_dir+"/TakeABreak.sh", "r")
        for ligne in template_script:
                if re.search("^prefix_output=", ligne):
                        ligne = "prefix_output=galaxy\n"
                if re.search("./bin/dbgh5", ligne):
                        ligne = ligne.replace("./bin/dbgh5", "dbgh5")
                if re.search('./bin/TakeABreak', ligne):
  	                ligne = ligne.replace('./bin/TakeABreak', "TakeABreak")

                run_script.write(ligne)

        run_script.close()
        template_script.close()

        # retrieve arguments
        parser = optparse.OptionParser()
        parser.add_option("-r", dest="reads_files")
        parser.add_option("-k", dest="kmer")
        parser.add_option("-S", dest="kmersolid")

        parser.add_option("-g", dest="graph_file")
        parser.add_option("-c", dest="complexity")
        parser.add_option("-m", dest="maxsimprct")
        #parser.add_option("-r", dest="optimization")

        parser.add_option("--output_graph")
        parser.add_option("--output_fasta")
        parser.add_option("--output_log")

        (options, args) = parser.parse_args()
	

	if options.reads_files:
		# start the command line
	        cmd_line = "sh TakeABreak.sh -r "+options.reads_files+" -k "+options.kmer+" -S "+options.kmersolid
		
	else:
		# start the command line
                cmd_line = "sh TakeABreak.sh -g "+options.graph_file
		

	#cmd_line+= " -c "+options.complexity+" -m "+options.maxsimprct
	cmd_line+= " -c "+options.complexity
	
	# execute command line 
	print cmd_line
	proc = subprocess.Popen( args=cmd_line, shell=True )
        returncode = proc.wait()

	if options.reads_files:

                # create output h5
                cmd="cp galaxy.h5 "+options.output_graph
                proc = subprocess.Popen( args=cmd, shell=True )
                returncode = proc.wait()

        # create output fasta
        cmd="cp galaxy.fasta "+options.output_fasta
        proc = subprocess.Popen( args=cmd, shell=True )
        returncode = proc.wait()

        # create output log
        cmd="cp galaxy.log "+options.output_log
        proc = subprocess.Popen( args=cmd, shell=True )
        returncode = proc.wait()


if __name__ == "__main__": __main__()
