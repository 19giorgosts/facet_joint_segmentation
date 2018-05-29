import nibabel as nib
import numpy as np

image = nib.load('datasets/Patients/Patient_1/Volume0_Ultra.nii')

# to be extra sure of not overwriting data:
new_data = np.copy(image.get_data())
hd = image.header

# update data type:
new_dtype = np.int16  # for example to cast to int16.
new_data = new_data.astype(new_dtype)
image.set_data_dtype(new_dtype)
new_image = nib.Nifti1Image(new_data, image.affine, header=hd)
new_image.set_data_dtype(np.int16)

nib.save(new_image, 'datasets/Patients/Patient_1/Volume0_Ultra_NEW.nii')