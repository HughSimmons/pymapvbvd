import numpy as np
#!pip install pymapvbvd
import sys
sys.path.append('/home/zhg603/pymapvbvd-1')  # Replace with the actual path

import mapvbvd

import matplotlib.pyplot as plt
# Load the Twix file
# twix_file = '/mnt/disk2Tssd/data/hugh/20240910_phantom/meas_MID00025_FID23793_ah_tfl_sandwich_3D_tiamo.dat'
#filepathgre = '/mnt/disk2Tssd/data/hugh/20240918/meas_MID00132_FID25031_ah_gre_smat3.dat'
#filepathgre = '/mnt/disk2Tssd/data/hugh/PTon_off/meas_MID00062_FID24509_ah_gre_smat3_60dbfshifted42khz_vop_pon.dat'
#filepathgre = '/mnt/disk2Tssd/data/hugh/20240926/meas_MID00023_FID26018_ah_gre_smat3.dat' #latest

#filepathgre = '/mnt/disk2Tssd/data/hugh/20240926/meas_MID00048_FID26043_ah_gre_smat3_CONTINOUS.dat'
filepathmprage = '/mnt/disk2Tssd/data/hugh/20240926/meas_MID00049_FID26044_cea_MPRAGE_UP.dat'
filepathmprage = '/mnt/disk2Tssd/data/hugh/20241016/meas_MID00030_FID28266_cea_MPRAGE_UP.dat' ##recent one





sandwichpaths = ['/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00157_FID30365_fmrib_tfl_sandwich_p3_pTx3Dsamecoordinatesfilept60db.dat', 
                 '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00161_FID30369_fmrib_tfl_sandwich_p3_pTx3Dsamecoordinatesfilept55db.dat',
                 '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00166_FID30374_fmrib_tfl_sandwich_p3_pTx3D_movingoct3.dat',
                  '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00180_FID30388_fmrib_tfl_sandwich_p3_pTx3Dsamecoordinatesfilept60dbdiffpositio.dat'] 
titlelist = ['old protocol, 60 db', 'old protocol, 55 db', 'new protocol, 60 db', 'old protocol, 60 db, antenna placed nearer']


# fig, ax = plt.subplots(3,4)
fig, ax = plt.subplots(2,2)







for i in range(4):
    print(i//4, i%4)

    # filepathsandwich = '/mnt/disk2Tssd/data/hugh/ptphantomexpts/meas_MID00157_FID30365_fmrib_tfl_sandwich_p3_pTx3Dsamecoordinatesfilept60db.dat'
    filepathsandwich = sandwichpaths[i]
    # twix_data = mapvbvd.mapVBVD(filepathgre)
    twix_data = mapvbvd.mapVBVD(filepathsandwich)


    # Extract k-space data
    twix_data.image.flagRemoveOS = False

    k_space_data = twix_data.image['']
    k_space_data2 = np.squeeze(k_space_data)
    print(k_space_data2.shape)

    # k_space_data2 = k_space_data2[:,:,:,:,0]
    image = np.fft.fftn(k_space_data2[:,:,:,:,:], axes=(0,2,3))
    image = np.fft.fftshift(image, axes=(0,2,3))
    image = abs(image)
    image = np.mean(image**2, axis=(1,4))

    nimage = np.sqrt(image)
    print(nimage.shape)
    # plt.imshow(nimage[:,16,:], cmap='gray')

    # plt.figure()
    t = np.mean(nimage, axis = (1,2))
    # t = t[80:]


    ax[i//2, i%2].scatter(np.arange(len(t)), t)
    # ax[i//2, i%2].set_ylim(0,0.005)

    # plt.scatter(np.arange(len(t)), t)
    # ax[i//4, i%4].imshow(nimage[:,16,:], cmap='gray')
    # ax[i//4, i%4].set_title(str(i))

    # #plt.figure()
    # t = np.mean(nimage, axis=(1,2))
    # ax[i//2, i%2].scatter(np.arange(len(t)),t, s=2)
    # #plt.show()
    # # ax[i//2, i%2].set_title(filenames[i])
    ax[i//2, i%2].set_title(titlelist[i])
    ax[i//2, i%2].set_ylabel("Image Profile")
    ax[i//2, i%2].set_xlabel("Voxel Number")
plt.suptitle("Sandwich Scans")
plt.show()