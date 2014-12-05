# ---------------------------------------------------------------------------
# CreateGapCrossingLayerOLD.py
# Based on ArcGIS 10 ModelBuilder model by Alex Lechner (alexmarklechner@yahoo.com.au)
# for use with GAP_CLoSR software.
# Script prepared by Michael Lacey (michael.lacey@utas.edu.au)
# Created on: 2014-07-25
#   
# The script expects 4 input arguments listed below
#   <Basefolder (string)>
#   <InputVegLayer (string)>
#   <OutputGapCrossingLayer (string)>
#   <InputCellMultiplier (float)>
# 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, time, os, sys

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True # Overwrite pre-existing files

# Script arguments
if len (sys.argv) >2: #ie arguments provided 
    Basefolder=str(sys.argv[1])
    InputVegLayer = Basefolder+"/"+ str(sys.argv[2]) #assumes no path included
    OutputGapCrossingLayer =Basefolder+"/"+ str(sys.argv[3]) #assumes no path included
    InputCellMultiplier = float(sys.argv[4])
    #expected format
    #BaseFolder="G:/MCAS-S/GAP_CLoSR_App/Data/GAP_CLoSR_Tutorial_1.3/data"
    #InputVegLayer = Basefolder + "/" + "lh_cc"
    #OutputGapCrossingLayer = Basefolder + "/OutputTest/gap_cross"
    #InputCellMultiplier = "40"

    print"Running"+str(sys.argv[0])+" at "+time.strftime('%d/%m/%y %H:%M:%S')
    print"Base folder: " + Basefolder
    print"Input vegetation layer: " + InputVegLayer
    print"Output gap-crossing raster: " + OutputGapCrossingLayer
    print"Input cell multiplier: " + str(InputCellMultiplier)
else:
    #
    print "This script is intended to be run with input arguments."

def main():
    #
    # Local variables:
    # temp folder
    TempFolder=Basefolder+"\\tmp_output\\"
    # temp rasters
    tempRaster=TempFolder+"temp1"
    tempRaster2=TempFolder+"temp2"


    print "\nGAP_CLoSR Default Tools"
    print "Create gap-crossing layer (old method)"
    print "Starting at " + time.strftime('%d/%m/%y %H:%M:%S')
    StartT=time.time()

    try:
        # Process: Aggregate
        arcpy.gp.Aggregate_sa(InputVegLayer, tempRaster, InputCellMultiplier, "SUM", "EXPAND", "DATA")
        # Process: Reclassify
        arcpy.gp.Reclassify_sa(tempRaster, "Value","1 1000000 1", tempRaster2, "DATA")
        # Process: Resample
        tempEnvironment0 = arcpy.env.snapRaster
        arcpy.env.snapRaster = InputVegLayer
        tempEnvironment1 = arcpy.env.extent
        arcpy.env.extent = InputVegLayer
        tempEnvironment2 = arcpy.env.cellSize
        arcpy.env.cellSize = InputVegLayer
        arcpy.Resample_management(tempRaster2, OutputGapCrossingLayer, "2.5 2.5", "NEAREST")
        arcpy.env.snapRaster = tempEnvironment0
        arcpy.env.extent = tempEnvironment1
        arcpy.env.cellSize = tempEnvironment2
    except:
        print "\nError in creating gap-crossing raster.\n"+ arcpy.GetMessages()

    print "Time elapsed:" +str(time.time()- StartT) + " seconds"
    print "Finished at:"  +  time.strftime('%d/%m/%y %H:%M:%S')
    ##end of main()##


if __name__=='__main__':
    main()
