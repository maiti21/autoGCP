# Import arcpy module
import os
import arcpy

#Make temporary directory
os.mkdir(r"D:\\SHP\\Temp")
os.mkdir(r"D:\\SHP\\Output")

# Local variables:
cl_line_shp = r"D:\\SHP\\test\\cl_line.shp"
cl_line_Buffer = r"D:\\SHP\\Temp\\BufferL.shp"
cl_line_Buffer_PolygonToLine = r"D:\\SHP\\Temp\\PolygonToLine.shp"
gcp_shp = r"D:\\SHP\\Output\\gcp_test.shp"
x = input ("Please enter the distance from road:")       #Please enter value in Meter
y = input ("Please enter the distance for GCP:")         #Please enter value in Meter
# Process: Buffer
arcpy.Buffer_analysis(cl_line_shp, cl_line_Buffer, x, "FULL", "FLAT", "NONE", "", "PLANAR")

# Process: Polygon To Line
arcpy.PolygonToLine_management(cl_line_Buffer, cl_line_Buffer_PolygonToLine, "IDENTIFY_NEIGHBORS")

# Process: Generate Points Along Lines
arcpy.GeneratePointsAlongLines_management(cl_line_Buffer_PolygonToLine, gcp_shp, "DISTANCE", y, "", "")

# Process: Add XY Coordinates
arcpy.AddXY_management(gcp_shp)

print "Completed Successfully!"

