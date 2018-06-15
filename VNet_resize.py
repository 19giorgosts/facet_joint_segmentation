import nibabel as nib
import os
import numpy as np
import nibabel.processing as nip
from nibabel.testing import data_path
import pylab as plt
import matplotlib.image as mpimg


## processing of volume0
file1 = os.path.join('datasets/Patients/Patient_1/nibproc', 'Labeled_CT_bin_seg.nii')
file2 = os.path.join('datasets/Patients/Patient_1/nibproc', 'Volume0_Ultra.nii')

img1 = nib.load(file1)
img2 = nib.load(file2)

img1=np.resize(128,128,64)
img2=np.resize(128,128,64)


nib.save(img1, 'datasets/Patients/Patient_1/nibproc/Labeled_CT_0_seg.nii')
nib.save(img2, 'datasets/Patients/Patient_1/nibproc/Labeled_CT_0_seg.nii')

