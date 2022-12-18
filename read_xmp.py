import glob
from libxmp import XMPFiles,consts
import csv
import sys

header =['Filename','CreateDate','Make','Model','GpsStatus','GpsLatitude','GpsLongitude','AbsoluteAltitude','RelativeAltitude','GimbalRollDegree','GimbalYawDegree','GimbalPitchDegree','FlightRollDegree','FlightYawDegree','FlightPitchDegree','FlightXSpeed','FlightYSpeed','FlightZSpeed','RtkFlag','RtkStdLon','RtkStdLat','RtkStdHgt','DroneModel']

args = sys.argv
path = "./sample/"
foldername = args[1].encode('utf_8')
# print(foldername)
print(type(foldername))
print(type(path))
'''
with open(foldername+".csv","w") as f:
	writer=csv.writer(f)
	writer.writerow(header)
	writer.writerow("/n")
# witer.writerow([1,2,3])
'''
files = glob.glob(path + foldername + "/*")
with open(path + foldername+".csv","w") as f:
	writer=csv.writer(f)
	writer.writerow(header)
	for file in files:
	    xmpfile = XMPFiles(file_path=file,open_forupdate=True)
	    xmp = xmpfile.get_xmp()

	    list=[]
	    list.append(file)
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("xmp"),"CreateDate"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("tiff"),"Make"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("tiff"),"Model"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"GpsStatus"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"GpsLatitude"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"GpsLongitude"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"AbsoluteAltitude"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"RelativeAltitude"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"GimbalRollDegree"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"GimbalYawDegree"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"GimbalPitchDegree"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"FlightRollDegree"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"FlightYawDegree"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"FlightPitchDegree"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"FlightXSpeed"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"FlightYSpeed"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"FlightZSpeed"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"RtkFlag"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"RtkStdLon"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"RtkStdLat"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"RtkStdHgt"))
	    list.append(xmp.get_property(xmp.get_namespace_for_prefix("drone-dji"),"DroneModel"))

	    writer.writerow(list) 
	    # print(list)
