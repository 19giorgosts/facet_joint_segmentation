%% preprocessing.m

% File for converting image from single to uint8 precision
% also adjusting the pixel values between [0,13]

% preprocessing of _seg images
Img = niftiread('Labeled_CT_seg.nii');
uint8Image = uint8(255/20 * mat2gray(Img));
uint8Image = uint8Image(1:64,1:64,1:64);
niftiwrite(uint8Image,'Labeled_new_CT_seg.nii');

% preprocessing of _Ultra images
Img2 = niftiread('Volume0_Ultra.nii');
Inew = int16(Img2);
Inew = Inew(1:64,1:64,1:64);
niftiwrite(Inew,'Volume0_new_Ultra.nii');