# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ClipScriptArgV2.py
# Created on: 2014-07-02 16:47:40.00000
#    
# Description: If no arguments are given it prints out some text describing
#              what arguments are expected.
#              If three arguments are given these are expected to be names of
#              three shapefiles with paths. The final shapefile is to be produced
#              by clipping the first with the second.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import sys
#allow overwrite of existing outputs (helps avoid interrupting batch processing)
arcpy.env.overwriteOutput = 1    # 1 = yes 0 = no
#InpFolder="G:\\MCAS-S\\GAP_CLoSR_App\\AppDevelopment\\"

if len (sys.argv) >2: #ie no arguments provided
##    if len (sys.argv)==4:
    if len (sys.argv)>3:
        #print sys.argv[0] #script name
        
        # Local variables:
        #Shape1 = "G:\\MCAS-S\\GAP_CLoSR_App\\AppDevelopment\\Shape1.shp"
        #AnotherShape = "G:\\MCAS-S\\GAP_CLoSR_App\\AppDevelopment\\AnotherShape.shp"
        #ClippedShape1_shp = "G:\\MCAS-S\\GAP_CLoSR_App\\AppDevelopment\\ClippedShape1.shp"
        Shape1 = sys.argv[1]
        AnotherShape = sys.argv[2]
        ClippedShape1_shp = sys.argv[3]

        # Process: Clip
        arcpy.Clip_analysis(Shape1, AnotherShape, ClippedShape1_shp, "")
    else:
        print "Three arguments are needed each separated by a space"
        print "Arguments: target shapefile, clip shapefile, output shapefile"
        print "enter names including path and separated by a space."

else:
    print "Arguments: target shapefile, clip shapefile, output shapefile"
    print "enter names including path and separated by a space."
