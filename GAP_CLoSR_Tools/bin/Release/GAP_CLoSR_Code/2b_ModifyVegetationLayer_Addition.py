# ---------------------------------------------------------------------------
# 2b_ModifyVegetationLayer_Addition.py
# for use with GAP_CLoSR software.
# Based on ArcGIS 10 ModelBuilder model by Alex Lechner (alexmarklechner@yahoo.com.au)
# Script prepared by Michael Lacey (michael.lacey@utas.edu.au)
# Created on: 2014-07-28
#   
# The script expects 6 input arguments listed below
#   <Basefolder (string)>
#   <InputChangeLayer (string)>
#   <InputVegetationLayer (string)>
#   <InputLuse (string)>
#   <InputHydrologyLayerValue (string)>
#   <OutputNewVegLayer (string)> 
# 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, time, os, sys

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True # Overwrite pre-existing files

# Script arguments
if len (sys.argv) >2: #ie arguments provided
    Basefolder = str(sys.argv[1])
    InputChangeLayer = Basefolder +"/"+ str(sys.argv[2]) #assumes no path included
    InputVegetationLayer = Basefolder +"/"+ str(sys.argv[3]) #assumes no path included
    Input_luse = Basefolder +"/"+ str(sys.argv[4]) #assumes no path included
    InputHydrologyLayerValue = float(sys.argv[5])
    OutputNewVegLayer = Basefolder +"/"+ str(sys.argv[6]) #assumes no path included

    #Basefolder = r"G:\MCAS-S\GAP_CLoSR_App\Data\GAP_CLoSR_Tutorial_1.3\data"
    #InputChangeLayer = Basefolder + r"\OutputTest\ChangeLayer"
    #InputVegetationLayer = Basefolder + r"\lh_cc"
    #Input_luse = Basefolder + r"\OutputTest\luse"
    #InputHydrologyLayerValue = 10
    #OutputNewVegLayer = Basefolder + r"\OutputTest\lh_ccAdd"

    print"Running"+str(sys.argv[0])+" at "+time.strftime('%d/%m/%y %H:%M:%S')
    print "Basefolder: " + Basefolder
    print "InputChangeLayer: " + InputChangeLayer
    print "InputVegetationLayer: " + InputVegetationLayer
    print "Input_luse: " + Input_luse
    print "InputHydrologyLayerValue: " + str(InputHydrologyLayerValue)
    print "OutputNewVegLayer: " + OutputNewVegLayer


def main():
    # Local variables:
    #none

    print "\nGAP_CLoSR Scenario Tools"
    print "Modify Vegetation Layer - Addition"
    print "Starting at " + time.strftime('%d/%m/%y %H:%M:%S')
    StartT=time.time()
    
    try:
        #arcpy.gp.RasterCalculator_sa("Con((\"%Input: ChangeLayer%\"==1) & (\"%Input: luse%\" != %Input: Hydrology layer value%),1,\"%Input: Vegetation Layer%\")", Output__New_Veg_Layer)
        #
        outputRaster = arcpy.sa.Con((arcpy.Raster(InputChangeLayer) == 1) & (arcpy.Raster(Input_luse) != InputHydrologyLayerValue), 1, InputVegetationLayer)
        outputRaster.save(OutputNewVegLayer)

    except:
        print "\nError in creating raster.\n"+ arcpy.GetMessages()

    print "Time elapsed:" +str(time.time()- StartT) + " seconds"
    print "Finished at:"  +  time.strftime('%d/%m/%y %H:%M:%S')
    ##end of main()##


if __name__=='__main__':
    main()

