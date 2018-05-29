import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot
import Tkinter as tk
from nibabel.testing import data_path

#volume_1 = os.path.join('datasets/Patients/Patient_1','Volume0new_Ultra.nii')
volume_2 = os.path.join('datasets/Patients/Patient_1','Labeled_CT_seg.nii')

#volume_brats_1 = os.path.join('datasets/Patients/Patient_brats','HGG147_Ultra.nii')
volume_brats_2 = os.path.join('datasets/Patients/Patient_brats','HGG147_seg.nii')


#img_1 = nib.load(volume_1)
img_2 = nib.load(volume_2)
#img_brats_1 = nib.load(volume_brats_1)
img_brats_2 = nib.load(volume_brats_2)
img_2.orthoview()
data = img_2.get_data()
new_data = data.copy()


new_data[new_data > 12] = 0
new_data[new_data > 11] = 1
new_data[new_data >1 ]  = 2

img_2.header['pixdim'] = img_brats_2.header['pixdim']
img_2.header['slice_start'] = img_brats_2.header['slice_start']
img_2.header['intent_code'] = img_brats_2.header['intent_code']
img_2.header['regular'] = img_brats_2.header['regular']
img_2.header['xyzt_units'] = img_brats_2.header['xyzt_units']
img_2.header['slice_duration'] = img_brats_2.header['slice_duration']



print(img_2)
print(".................")
print(img_brats_2)
#print(img_brats_2)
#print(new_data.max())

#thresholding now 

thresh_img = nib.Nifti1Image(new_data, img_2.affine, img_2.header)
print(thresh_img.get_data_dtype)
nib.save(thresh_img, 'datasets/Patients/Patient_1/Labeled_new_CT_seg.nii')

#print(img_2.get_data_dtype() == img_brats_2.get_data_dtype())


'''
print(img_2.shape)
print(img_brats_2.shape)

print(img_2.get_data_dtype())
print(img_brats_2.get_data_dtype())

a = img_1.get_data()
new_dtype = np.int16  # for example to cast to int16.
a = a.astype(new_dtype)
img_1.set_data_dtype(new_dtype)
#a[a >= 12] = 0
#print(img_1)

nib.save(img_1, 'datasets/Patients/Patient_1/Volume0_Ultra.nii')'''