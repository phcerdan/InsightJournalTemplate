import SimpleITK as sitk
import numpy as np
np.core.arrayprint._line_width = 200

img = sitk.ReadImage("/home/phc/Software/ITK/build-dev-cpp98/ExternalData/Modules/Remote/IsotropicWavelets/test/Input/checkershadow_Lch_512x512.tiff")
#3D
# img = sitk.ReadImage("/home/phc/repository_local/ITKfilters/src/fixtures/collagen_64x64x16.tiff")
imgF=sitk.Cast(img,sitk.sitkFloat64)

############# DC Zero ###############
statsFilter = sitk.StatisticsImageFilter()
statsFilter.Execute(imgF)
mean = statsFilter.GetMean()
imgFz = sitk.Subtract(imgF, mean)

############# ForwardFFT ###############
fft = sitk.ForwardFFT(imgFz)
# fft= sitk.FFTShift(fft)
inverseFFT = sitk.InverseFFT(fft)
afft = sitk.GetArrayFromImage(sitk.ComplexToReal(fft))
ar = afft
# Fold frequency
sx = ar.shape[0] / 2
sy = ar.shape[1] / 2
c00 = ar[0:sx, 0:sy]
c10 = ar[sx:, 0:sy]
c01 = ar[0:sx , sy:]
c11 = ar[sx : , sy:]
afold = (c00 + c01 + c10 + c11) * 0.25
fold = sitk.GetImageFromArray(afold)
foldc=sitk.Cast(fold,sitk.sitkComplexFloat64)
inverseFoldShift = sitk.InverseFFT(sitk.FFTShift(foldc))
inverseFold = sitk.InverseFFT(foldc)
# Folding but right freq
c00t = c00
c10t = c10[:, ::-1]
c01t = c01[::-1,:]
c11t = c11[::-1,::-1]
afoldt = (c00t + c01t + c10t + c11t) * 0.25
foldt = sitk.GetImageFromArray(afoldt)
foldtc=sitk.Cast(foldt,sitk.sitkComplexFloat64)
# inverseFoldShift = sitk.InverseFFT(sitk.FFTShift(foldtc))
inverseFoldt = sitk.InverseFFT(foldtc)

# lp = -1593433.9685793633107
# lpOpp = 663521.62642128230073
p128_1 = 15821.565044998889789
lp = p128_1
op = np.transpose(np.isclose(ar,lp).nonzero())
p128_255 = -7512.1918671552557498
lpOpp = p128_255
opc = np.transpose(np.isclose(ar,lpOpp).nonzero())

# Test with diagonal image. Folding in frequency domain works......... WTF!
osize = 16
# diagonal = np.array([float(i==j or i == osize - j -1 or j == osize - 1 - i)  for j in np.arange(osize) for i in np.arange(osize)]);
diagonal = np.array([float(i==j or i == osize - j - 1  or j == osize - i - 1)  for j in np.arange(osize) for i in np.arange(osize)]);
diagonal.shape = (osize,osize)
diagImg = sitk.GetImageFromArray(diagonal)
# sitk.Show(diagImg)
diagFFT = sitk.ForwardFFT(diagImg)
diagFFT = sitk.FFTShift(diagFFT)
diagFFTreal = sitk.ComplexToReal(diagFFT)
diagFFTimag = sitk.ComplexToImaginary(diagFFT)
# fai = sitk.GetArrayFromImage(diagFFTimag)
far = sitk.GetArrayFromImage(diagFFTreal)
mx = osize/2;
my = osize/2;
b00 = far[:mx,:my ]
b10 = far[mx:,:my]
b01 = far[:mx,my:]
b11 = far[mx:,my:]
farMod = (b00 + b10 +b01 +b11 ) / 4.0

b00t = b00
b10t = b10[:, ::-1]
b01t = b01[::-1,:]
# b10t = b10[::-1,:]
# b01t = b01[:, ::-1]
b11t = b11[::-1,::-1]
farModt = (b00t + b10t +b01t +b11t ) / 4.0

fai = np.zeros([mx,my])
diagFFTrealMod = sitk.GetImageFromArray(farMod)
diagFFTimagMod = sitk.GetImageFromArray(fai)
composed = sitk.RealAndImaginaryToComplex(diagFFTrealMod, diagFFTimagMod)
# composed = sitk.FFTShift(composed)
diagRecons = sitk.InverseFFT(composed)
sitk.Show(diagRecons)

# 8x8 rnd image to test
a8rnd = np.array([np.random.random_sample() for i in np.arange(64)]);
a8rnd.shape = (8,8)
mx = 4;
my = 4;
b00 = a8rnd[:mx,:my ]
b10 = a8rnd[mx:,:my]
b01 = a8rnd[:mx,my:]
b11 = a8rnd[mx:,my:]

b00t = b00
b10t = b10[:, ::-1]
b01t = b01[::-1,:]
b11t = b11[::-1,::-1]

i8rnd = sitk.GetImageFromArray(a8rnd)
fft8rnd = sitk.ForwardFFT(i8rnd)
fft8rndreal = sitk.ComplexToReal(fft8rnd)
fft8rndimag = sitk.ComplexToImaginary(fft8rnd)
