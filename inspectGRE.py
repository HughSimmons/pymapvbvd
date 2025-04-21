import numpy as np
#!pip install pymapvbvd
# import mapvbvd
import sys
sys.path.append('/home/zhg603/pymapvbvd-1')  # Replace with the actual path

import mapvbvd  # Replace with the actual module name (without the .py extension)


import matplotlib.pyplot as plt
# Load the Twix file

filepaths = ['/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00158_FID30366_ah_gre_smat3samecoordinatesfilept60db.dat', '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00163_FID30371_ah_gre_smat3samecoordinatesfilept55db.dat',
              '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00174_FID30382_ah_gre_smat3_CONTINOUS.dat', '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00181_FID30389_ah_gre_smat3samecoordinatesfilept60dbdiffposition.dat']

titlelist = ['old protocol, 60 db', 'old protocol, 55 db', 'new protocol, 60 db', 'old protocol, 60 db, antenna placed nearer']

fig, ax = plt.subplots(2,2)



# timet = np.zeros([18,128])
# timenimage = np.zeros([18,128,32,26])
for i in range(4):
    # Extract k-space data
    twix_data = mapvbvd.mapVBVD(filepaths[i])
    twix_data.image.flagRemoveOS = False
    k_space_data = twix_data.image['']
    k_space_data2 = np.squeeze(k_space_data)
    print("Shape is:" ,k_space_data2.shape)
# for time in range(k_space_data2.shape[-1]):
    if len(k_space_data2.shape)==5:
        timekspace = k_space_data2[:,:,:,:,0]
        print("time trigger", i)

    else:
        timekspace = k_space_data2
    
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
    zoomlength = (len(t)*6)//8
    t = t[zoomlength:]
    # timenimage[time,:,:,:] = nimage

    ax[i//2, i%2].scatter(np.arange(len(t)), t[:],s=2)
    ax[i//2, i%2].set_title(titlelist[i])
    ax[i//2, i%2].set_ylabel("Image Profile (Magnitude)")
    ax[i//2, i%2].set_xlabel("Voxel Number")
    # plt.xlabel("Voxel Index")
    # plt.ylabel("Magnitude of Voxel (Meaned across other axes)")
    # plt.title("Image data with Pilot Tone GRE")# (Zoomed)")

print(nimage.shape)
plt.suptitle("GRE_smat PT (Zoomed)")
#plt.figure()
#plt.imshow(nimage[:,:,13], cmap='gray')
plt.show()



fig, ax = plt.subplots(2,2)



# timet = np.zeros([18,128])
# timenimage = np.zeros([18,128,32,26])
for i in range(4):
    # Extract k-space data
    twix_data = mapvbvd.mapVBVD(filepaths[i])
    twix_data.image.flagRemoveOS = False
    k_space_data = twix_data.image['']
    k_space_data2 = np.squeeze(k_space_data)
    print("Shape is:" ,k_space_data2.shape)
# for time in range(k_space_data2.shape[-1]):
    if len(k_space_data2.shape)==5:
        timekspace = k_space_data2[:,:,:,:,0]
        print("time trigger", i)

    else:
        timekspace = k_space_data2
    
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
    zoomlength = (len(t)*6)//8
    t = t[zoomlength:]
    # timenimage[time,:,:,:] = nimage

    ax[i//2, i%2].imshow(nimage[:,16,:], cmap='gray')
    # ax[i//2, i%2].set_title(titlelist[i])
    # ax[i//2, i%2].set_ylabel("Image Profile (Magnitude)")
    # ax[i//2, i%2].set_xlabel("Voxel Number")
    # plt.xlabel("Voxel Index")
    # plt.ylabel("Magnitude of Voxel (Meaned across other axes)")
    # plt.title("Image data with Pilot Tone GRE")# (Zoomed)")

print(nimage.shape)
plt.suptitle("GRE_smat PT (Zoomed)")
#plt.figure()
#plt.imshow(nimage[:,:,13], cmap='gray')
plt.show()
# for i in range(4):

#     filepathmprage = basepath + filenames[i]

#     # twix_data = mapvbvd.mapVBVD(filepathgre)
#     twix_data = mapvbvd.mapVBVD(filepathmprage)


#     # Extract k-space data
#     twix_data.image.flagRemoveOS = False

#     k_space_data = twix_data.image['']
#     k_space_data2 = np.squeeze(k_space_data)
#     k_space_data2.shape


#     image = np.fft.fftn(k_space_data2[:,:,:,:], axes=(0,2,3))
#     image = np.fft.fftshift(image, axes=(0,2,3))
#     image = abs(image)
#     image = np.mean(image**2, axis=1)

#     nimage = np.sqrt(image)
#     print(nimage.shape)

#     #plt.imshow(nimage[:,140,:], cmap='gray')

#     #plt.figure()
#     t = np.mean(nimage, axis=(1,2))
#     ax[i//2, i%2].scatter(np.arange(len(t)),t, s=2)
#     #plt.show()
#     # ax[i//2, i%2].set_title(filenames[i])
#     ax[i//2, i%2].set_title(titlelist[i])
#     ax[i//2, i%2].set_ylabel("Image Profile (Meaned along all but one direction)")
#     ax[i//2, i%2].set_xlabel("Voxel Number")
# plt.suptitle("MPRAGE PT")
# plt.show()