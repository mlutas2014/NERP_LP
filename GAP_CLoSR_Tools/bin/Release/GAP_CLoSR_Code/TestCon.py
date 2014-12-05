# ---------------------------------------------------------------------------
# 2a_ModifyVegetationLayer_Removal.py
# for use with GAP_CLoSR software.
# Based on ArcGIS 10 ModelBuilder model by Alex Lechner (alexmarklechner@yahoo.com.au)
# Script prepared by Michael Lacey (michael.lacey@utas.edu.au)
# Created on: 2014-07-28
#   
# The script expects 4 input arguments listed below
#   <Basefolder (string)>
#   <InputChangeLayer (string)>
#   <InputVegetationLayer (string)>
#   <OutputNewVegLayer (string)> 
#
# ---------------------------------------------------------------------------


# Import arcpy module
import arcpy, time, os, sys

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True # Overwrite pre-existing files

# Script arguments

Basefolder = r"G:\MCAS-S\GAP_CLoSR_App\Data\GAP_CLoSR_Tutorial_1.3\data"
InputChangeLayer = Basefolder +r"\OutputTest\changelayer"
InputVegetationLayer = Basefolder +r"\lh_cc"
OutputNewVegLayer1 = Basefolder +r"\OutputTest\lh_ccrem3"
OutputNewVegLayer2 = Basefolder +r"\OutputTest\lh_ccrem4"
OutputNewVegLayer3 = Basefolder +r"\OutputTest\lh_ccrem6"

#BaseFolder = r"G:\MCAS-S\GAP_CLoSR_App\Data\GAP_CLoSR_Tutorial_1.3\data"
#InputChangeLayer = Basefolder + r"\OutputTest\ChangeLayer"
#InputVegetationLayer = Basefolder + r"\lh_cc"
#OutputNewVegLayer = Basefolder + r"\OutputTest\lh_ccREM"

print "Base Folder: " + Basefolder
print "Input Change Layer: " + InputChangeLayer
print "Input Vegetation Layer: " + InputVegetationLayer
#print "Output New Veg. Layer1: " + OutputNewVegLayer1
#print "Output New Veg. Layer2: " + OutputNewVegLayer2
print "Output New Veg. Layer3: " + OutputNewVegLayer3

def main():
    # Local variables:
    #none
    
    print "\nGAP_CLoSR Scenario Tools"
    print "Modify Vegetation Layer - Removal"
    print "Starting at " + time.strftime('%d/%m/%y %H:%M:%S')
    StartT=time.time()

##    try:
##        #arcpy.gp.RasterCalculator_sa("Con(\"%Input: ChangeLayer%\"==1,0,\"%Input: Vegetation Layer%\")", Output__New_Veg_Layer)
##        # Process: Con
##        arcpy.gp.Con_sa(InputChangeLayer, "0", OutputNewVegLayer1, InputVegetationLayer, "\"VALUE\"=1")
##    except:
##        print "Error in creating raster1.\n"+ arcpy.GetMessages()
    try:
        # Process: Con
        outputRaster = arcpy.sa.Con(arcpy.Raster(InputChangeLayer) == 1, 0, InputVegetationLayer)
        outputRaster.save(OutputNewVegLayer3)
        #arcpy.gp.Con_sa("\""+InputChangeLayer+"\"==1", "0", OutputNewVegLayer2, InputVegetationLayer)
    except:
        print "Error in creating raster2.\n"+ arcpy.GetMessages()

    print "Time elapsed:" +str(time.time()- StartT) + " seconds"
    print "Finished at:"  +  time.strftime('%d/%m/%y %H:%M:%S')
    ##end of main()##


if __name__=='__main__':
    main()
