import numpy as np
#!pip install pymapvbvd
import sys
import importlib
import importlib.util

# Define the path to the module file
# module_file_path = "/path/to/your/module/your_module_name.py"
module_file_path = '/home/zhg603/pymapvbvd-1/mapvbvd.py'

# Create a module specification
spec = importlib.util.spec_from_file_location("mapvbvd", module_file_path)

# Load the module
mapvbvd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mapvbvd)

# Now you can use the module
# your_module.some_function()
###########
# import mapvbvd

#import mapvbvd

import matplotlib.pyplot as plt

importlib.reload(mapvbvd)


filepathsand = '/mnt/disk2Tssd/data/hugh/20240918/meas_MID00138_FID25037_ah_tfl_sandwich3D_tiamo2.dat'
filepathmprage = '/mnt/disk2Tssd/data/hugh/20240918/meas_MID00121_FID25020_cea_MPRAGE_UP.dat'
filepathgre = '/mnt/disk2Tssd/data/hugh/20240918/meas_MID00132_FID25031_ah_gre_smat3.dat'


#twixObj = mapvbvd.mapVBVD(filepathsand)
#twixmprage = mapvbvd.mapVBVD(filepathmprage)
twixgre = mapvbvd.mapVBVD(filepathgre)
twixgre.vop.flagRemoveOS = False
realgreima = twixgre.vop.read_vop()




def readinfile(filepath):
    twixObj = mapvbvd.mapVBVD(filepath)
    twixObj.vop.flagRemoveOS = False
    ima = twixObj.vop.read_vop()
    return(ima)






def grescat(filepathmprage):
    ##only one pulse for gre
    greima = readinfile(filepathmprage)
    
    p1 = greima[0][0]
 
    pulse = p1


    len1 = pulse.shape[-1]
    scat = np.zeros([len1,8,8], dtype=complex)
    for pulseind in range(len1):
    
        chout = pulse[:,0::2,pulseind]
        chrec = pulse[:,1::2,pulseind]
    
        sol = np.linalg.lstsq(chout, chrec, rcond=None)
        scat[pulseind,:,:] = sol[0]


    return(scat)


#test = mpragescat(filepathmprage)
cgrescat = grescat(filepathgre)