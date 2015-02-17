#!/bin/python

import sys,os

inputs = " ".join(sys.argv[1].split(","))
cmd = "convert -append "+inputs+" "+sys.argv[2]
os.system(cmd)

