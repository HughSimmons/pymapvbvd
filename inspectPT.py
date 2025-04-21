import numpy as np
#!pip install pymapvbvd
# import mapvbvd
import sys
sys.path.append('/home/zhg603/pymapvbvd-1')  # Replace with the actual path

import mapvbvd  # Replace with the actual module name (without the .py extension)


import matplotlib.pyplot as plt
# Load the Twix file


# invivogrepath = '/mnt/disk2Tssd/data/hugh/20241003/meas_MID00071_FID26942_ah_gre_smat3_CONTINOUS.dat'
invivogrepath = '/mnt/disk2Tssd/data/hugh/20241003/meas_MID00073_FID26944_ah_gre_smat3_CONTINOUS.dat'
filepathgre = invivogrepath


twix_data = mapvbvd.mapVBVD(filepathgre)


# Extract k-space data
twix_data.image.flagRemoveOS = False

k_space_data = twix_data.image['']
k_space_data2 = np.squeeze(k_space_data)
print("Shape is:" ,k_space_data2.shape)

timet = np.zeros([18,128])
timenimage = np.zeros([18,128,32,26])
for time in range(1):
# for time in range(k_space_data2.shape[-1]):
    timekspace = k_space_data2[:,:,:,:,time]
    
    image = np.fft.fftn(timekspace[:,:,:,:], axes=(0,2,3))
    image = np.fft.fftshift(image, axes=(0,2,3))
    image = abs(image)
    image = np.mean(image**2, axis=1)
    nimage = np.sqrt(image)
    
    
    # plt.imshow(image[32:96,16,:], cmap='gray')
    
    # plt.figure(figsize=(10,10))
    
    # plt.imshow(nimage[32:96,:,13], cmap='gray')
    # plt.figure()
    
    t = np.mean(nimage, axis=(1,2))
    # # print(t.shape)
    # # print(np.argmax(t))
    # ptpeaks[time] = t[np.argmax(t)]
    # downone[time] = t[np.argmax(t)-1]
    # downthree[time] = t[np.argmax(t)-3]
    # upone[time] = t[np.argmax(t)+1]
    # timet[time,:] = t
    # timenimage[time,:,:,:] = nimage
    plt.scatter(np.arange(len(t)), t[:])
    
    # plt.xlabel("Voxel Index")
    # plt.ylabel("Magnitude of Voxel (Meaned across other axes)")
    # plt.title("Image data with Pilot Tone GRE")# (Zoomed)")

print(nimage.shape)
plt.figure()
plt.imshow(nimage[:,:,13], cmap='gray')
plt.show()