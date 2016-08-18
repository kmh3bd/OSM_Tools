# ----------------------------------------------------------------------------------------------------------------------
# Name          :   OSM Metrics
# ArcGIS Version:   10.2+
#
# Purpose:  Gather metrics on OSM data. Add length field, Calculate lengh, provide length sum per road type
#
# Inputs: OSM roads
#
# Outputs: GDB Table
#
# ----------------------------------------------------------------------------------------------------------------------
import sys
import os
import arcpy
import numpy
import re
import traceback
from datetime import datetime

__author__ = "Kim Harris"
__version__ = "1.0"
__created__ = "August 17, 2016"
__modified__ = ""


# Set environment settings
arcpy.env.workspace = arcpy.GetParameterAsText(0)
in_featureclass = arcpy.GetParameterAsText(1)

# Variable for Add and Caluculate Field
fieldName = "length"
 
# Execute AddField & Calculate Field
arcpy.AddMessage("Adding length field")
arcpy.AddField_management(in_featureclass, fieldName, "DOUBLE")
arcpy.AddMessage("Length field added")

arcpy.AddMessage("Executing length calculation")
arcpy.CalculateField_management(in_featureclass, fieldName, "!SHAPE.LENGTH@METERS!", "PYTHON_9.3")
arcpy.AddMessage("Calculated length in meters")

# Variable for Frequency
outtable = "roads_sumstats"
casefield = "type"
statsFields = [["length", "SUM"]]

# Run the Summary Statistics tool with the stats list
arcpy.AddMessage("Performing summary statistics...")
arcpy.Statistics_analysis(in_featureclass, outtable, statsFields, casefield)
arcpy.AddMessage("Complete!")
