#python test script for GAP_CLoSR_GUI
#
# This script can be used to test the GAP_CLoSR_GUI.exe application
# It accepts nine arguments in the following order passed from the GUI:
# RootDir; input_CC; input_gap_cross; input_luse; original_pixel_size;
# new_pixel_size; Max_cost; Max_distance; reclass_txt.
# Two preceeding arguments: the python application and the script name
# have also been used by the GUI to run the script but not passed to the script.
#
# Michael Lacey, 24th July, 2014
# Michae.Lacey@utas.edu.au


#imports to check for compatibility of python installation
import time
import arcpy
from arcpy import env 
from arcpy.sa import *
import numpy as np
import os
import sys
import scipy as scipy
#from scipy import ndimage
from collections import Counter
import pylab
import csv
import string
arcpy.CheckOutExtension("spatial")

#Example settings as passed by the GUI
#Use \ as path separator
#
#RootDir = "D:\GAP_CLoSR_Tutorial\Python_Processing" # does not need to include quotes
#input_CC =  lh_cc            # do not include quotes
#input_gap_cross = gap_cross  # do not include quotes
#input_luse =  luse           # do not include quotes
#original_pixel_size = 2.5
#new_pixel_size = 25
#Max_cost = 75 # highest value a pixel can have not including those pixels with infinite value
#Max_distance = 1
#reclass_txt = "D:\GAP_CLoSR_Tutorial\Python_Processing\InputRasters\luse_reclass.txt" # does not need to include quotes

if len (sys.argv) >2: #ie no arguments provided
    """Filenames and location"""
    RootDir = str(sys.argv[1])
    input_CC =  str(sys.argv[2])
    input_gap_cross = str(sys.argv[3])
    input_luse =  str(sys.argv[4])
    """Processing parameters"""
    original_pixel_size = float(sys.argv[5])
    new_pixel_size = int(sys.argv[6])
    Max_cost = int(sys.argv[7])
    Max_distance = int(sys.argv[8])
    reclass_txt = str(sys.argv[9])
    
    print "RootDir: " + RootDir
    print "input_CC: " + input_CC 
    print "input_gap_cross: " + input_gap_cross
    print "input_luse: " + input_luse
    print "original_pixel_size: " + str(original_pixel_size)
    print "new_pixel_size: " + str(new_pixel_size)
    print "Max_cost: " + str(Max_cost)
    print "Max_distance: " + str(Max_distance)
    print "reclass_txt: " + str(reclass_txt)

else:
    #return "Missing Arguments"
    print "This script is intended to be run with input arguments."
